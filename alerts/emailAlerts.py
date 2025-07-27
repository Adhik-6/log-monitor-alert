import os, smtplib, time
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.configLoader import loadConfig

load_dotenv()
config = loadConfig()

lastSentTime = {}
rateLimit = config['email']['rate_limit_seconds']


def sendEmailAlerts(body):
  now = time.time()

  lastTime = lastSentTime.get(body)
  if lastTime and now - lastTime < rateLimit:
    print("⚠️ Rate limit reached. Email not sent.")
    return
  
  lastSentTime[body] = now

  SENDER_EMAIL = os.getenv('SENDER_EMAIL')
  SENDER_EMAIL_PASS = os.getenv('SENDER_EMAIL_PASS')
  RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

  if not all([SENDER_EMAIL, SENDER_EMAIL_PASS, RECEIVER_EMAIL]):
    print("❌ Email config missing. Check your .env file.")
    return
  
  msg = MIMEMultipart("alternative")
  msg['From'] = SENDER_EMAIL
  msg['To'] = RECEIVER_EMAIL
  msg['Subject'] = "Log Alert"

  html_body = f"""
    <html><body>
    <h3 style="color:red;">Log issue detected</h3>
    <pre style="background:#f0f0f0; padding:10px;">{body}</pre>
    </body></html>
    """

  msg.attach(MIMEText(html_body, 'html'))
  msg.attach(MIMEText(body, 'plain'))

  try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_EMAIL_PASS)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    server.quit()
    print("✅ Alert email sent successfully.")
  except Exception as e:
    print(f"❌ Failed to send email: {e}")