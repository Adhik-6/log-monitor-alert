import os, smtplib, time
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.configLoader import loadConfig
from collections import defaultdict

load_dotenv()
config = loadConfig()

# Track alerts
lastSentTime = {}
pendingCounts = defaultdict(int)
rateLimit = config['email']['rate_limit_seconds']  # e.g. 60s

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_EMAIL_PASS = os.getenv('SENDER_EMAIL_PASS')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

def _sendEmail(subject, body):
    if not all([SENDER_EMAIL, SENDER_EMAIL_PASS, RECEIVER_EMAIL]):
        print("❌ Email config missing.")
        return

    msg = MIMEMultipart("alternative")
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject

    html_body = f"""
    <html>
      <body>
        <h3 style="color:red;">{subject}</h3>
        <pre style="background:#f0f0f0; padding:10px;">{body}</pre>
      </body>
    </html>
    """

    msg.attach(MIMEText(html_body, 'html'))
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_EMAIL_PASS)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print(f"✅ Email sent: {subject}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


def sendEmailAlerts(line):
  now = time.time()
  lastTime = lastSentTime.get(line)
  # print(f"Captured Log: {line}")

  if not lastTime or now - lastTime >= rateLimit:
      # If new OR cooldown expired → send immediately
      count = pendingCounts[line]
      if count > 0:
          # Send summary first (deduped)
          _sendEmail("🚨 Repeated Log Alerts", f"{line} (x{count+1})")
          pendingCounts[line] = 0
      else:
          # First occurrence
          _sendEmail("🚨 Log Alert", line)
      lastSentTime[line] = now
  else:
      # Within cooldown → count it instead of spamming
      pendingCounts[line] += 1
      print(f"⏳ Suppressed duplicate: {line} (count={pendingCounts[line]})")
