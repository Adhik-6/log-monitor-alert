

<div id="readme-top" align="center">

  <h1>LogMon</h1>

  <p>LogMon is a log monitoring and alerting tool designed to help you keep track of your system logs and receive notifications for important events.</p>


   <!-- Badges -->
  <p>
    <a href="https://github.com/Adhik-6/log-monitor-alert/graphs/contributors">
      <img src="https://img.shields.io/github/contributors/Adhik-6/log-monitor-alert" alt="contributors" />
    </a>
    <a href="https://github.com/Adhik-6/log-monitor-alert">
      <img src="https://img.shields.io/github/last-commit/Adhik-6/log-monitor-alert" alt="last update" />
    </a>
    <a href="https://github.com/Adhik-6/log-monitor-alert/network/members">
      <img src="https://img.shields.io/github/forks/Adhik-6/log-monitor-alert" alt="forks" />
    </a>
    <a href="https://github.com/Adhik-6/log-monitor-alert/stargazers">
      <img src="https://img.shields.io/github/stars/Adhik-6/log-monitor-alert" alt="stars" />
    </a>
    <a href="https://github.com/Adhik-6/log-monitor-alert/issues/">
      <img src="https://img.shields.io/github/issues/Adhik-6/log-monitor-alert" alt="open issues" />
    </a>
    <a href="https://github.com/Adhik-6/log-monitor-alert/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/Adhik-6/log-monitor-alert.svg" alt="license" />
    </a>
  </p>

  <!-- Links -->
  <h4>
    <a href="https://github.com/Adhik-6/log-monitor-alert">Documentation</a>
    <span> · </span>
    <a href="https://github.com/Adhik-6/log-monitor-alert/issues/">Report Bug</a>
    <span> · </span>
    <a href="https://github.com/Adhik-6/log-monitor-alert/issues/">Request Feature</a>
  </h4>

</div>

<p align="center">
The LogMon is a lightweight Python-based tool that continuously watches Linux system logs in real time using <code>journalctl -f</code>. It automatically detects suspicious activity (e.g., failed login attempts, brute-force attacks, privilege escalation) and notifies the system administrator via email using Python's SMTP service. To prevent alert fatigue, it includes rate-limiting and de-duplication: repeated identical log entries trigger only one alert initially, with a summary email sent after a cooldown period. This ensures timely, actionable, and noise-free monitoring for system security.
</p>

<br />


<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents <!-- omit in toc -->

- [:star2: About the Project](#star2-about-the-project)
- [🛠️ Tech Stack](#️-tech-stack)
  - [:dart: Features](#dart-features)
  - [:key: Environment Variables](#key-environment-variables)
- [:toolbox: Getting Started](#toolbox-getting-started)
  - [:bangbang: Prerequisites](#bangbang-prerequisites)
  - [:gear: Installation](#gear-installation)
  - [:running: Setup](#running-setup)
  - [:test\_tube: Running Tests](#test_tube-running-tests)
- [:eyes: Usage](#eyes-usage)
- [:compass: Roadmap](#compass-roadmap)
- [:wave: Contributing](#wave-contributing)
- [:grey\_question: FAQ](#grey_question-faq)
- [:gem: Acknowledgements](#gem-acknowledgements)

<!-- About the Project -->
## :star2: About the Project
System administrators often face the challenge of detecting suspicious activity in real time without being overwhelmed by log noise. Traditional log monitoring solutions can either be too heavy (full SIEMs) or too noisy (raw log tailing).

The **Log Monitoring and Alert System** is designed as a lightweight, Python-powered solution that continuously monitors Linux logs using `journalctl -f`. Whenever a suspicious event such as failed login attempts, brute-force patterns, or privilege escalation is detected, the system sends **real-time email alerts** to the administrator using Python’s SMTP service.

What makes this tool effective is its **intelligent alerting mechanism**:
  - It avoids spamming the admin’s mailbox by implementing **rate-limiting** and **de-duplication**.
  - A log entry triggers an email only once per cooldown window (`rate_limit_seconds`).
  - Repeated identical entries are counted silently and summarized in a **single follow-up email** once the cooldown expires.

This ensures that the admin is **alerted instantly to new threats** while still receiving a **concise summary of recurring issues** — striking the right balance between **responsiveness** and **signal-to-noise ratio**.


<!-- TechStack -->
## 🛠️ Tech Stack

| Platform       | Technologies Used                                |
|----------------|--------------------------------------------------|
| Language       | Python                                           |
| Core Modules   | `subprocess` (to run journalctl), `smtplib` (for email alerts), `time`, `collections` |
| System Tools   | `journalctl -f` (real-time log monitoring, Linux systemd logs) |
| Platform       | Oracle VM VirtualBox, Kali Linux (systemd-based distributions) |
| Email Service  | Python SMTP (configurable with Gmail/Custom SMTP servers) |


<!-- Features -->
### :dart: Features

- 🔍 Real-time Log Monitoring – Continuously tracks Linux system logs using `journalctl -f`.
- 🚨 Immediate Email Alerts – Notifies the system administrator via SMTP when suspicious logs are detected.
- 📦 Rate-Limiting & De-duplication – Prevents mailbox spam by suppressing duplicate alerts during a cooldown period.
- 📊 Summary Emails – Sends a single digest summarizing how many times a log line repeated during cooldown.
- 🛡️ Brute-Force Attack Detection – Captures multiple failed login attempts and alerts efficiently.
- ⚡ Lightweight & Fast – Pure Python with no heavy dependencies; uses built-in modules (`subprocess`, `smtplib`, etc.).
- 🖥️ Linux-Specific – Designed for systemd-based distributions, making use of `journalctl` for log access.
- ⚙️ Configurable – Adjustable rate-limit duration, email settings, and monitored log patterns.

<!-- Env Variables -->
### :key: Environment Variables

To run this project, you will need to add the following environment variables. Keep them ready and proceed with [getting started](#'Getting Started')

```env
SENDER_EMAIL=from@example.com
SENDER_EMAIL_PASS=aaaa bbbb cccc dddd
RECEIVER_EMAIL=receiver@example.com
```

<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

- 🐍 Python 3.8+ installed
- 📦 pip (Python package manager)
- 🐧 Linux system with systemd (project relies on journalctl)
- 📬 SMTP-enabled email account (e.g., Gmail, Outlook, or custom SMTP server)
- 🔑 App Password / SMTP credentials (if using Gmail or a secured mail provider)
- 🛠️ A virtual environment (venv or virtualenv) to keep dependencies isolated.
- 📡 Internet access (to send email notifications).


<!-- Installation -->
### :gear: Installation

Clone the repository [log_monitoring_and_alert](https://github.com/Adhik-6/log-monitor-alert) in `/opt/logmonitor`
```bash
sudo mkdir -p /opt/logmonitor
sudo git clone https://github.com/Adhik-6/log-monitor-alert /opt/logmonitor
```

(*Optional*) Create a virtual environment:
```bash
cd /opt/logmonitor
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt  
```
   

<!-- Run Locally -->
### :running: Setup

**1. Create a dedicated service user**

Keeps things safer than running as root.
```bash
sudo useradd --system --no-create-home --shell /usr/sbin/nologin logmon
sudo chown -R logmon:logmon /opt/logmonitor
```
A dedicated service user has been created for running the log monitoring service with no home directory and a restricted shell. We then give ownership of the log monitoring directory to this user for better security.

**2. Give the service user permission to read the journal**

Depending on distro, it’s either systemd-journal or adm. Add to both safely:
```bash
getent group systemd-journal && sudo usermod -aG systemd-journal logmon
getent group adm && sudo usermod -aG adm logmon
```

**3. Put secrets in an env file**

Make sure your env file contains all the below specified variables.
```bash
sudo bash -c 'cat >/etc/default/logmonitor <<EOF
SENDER_EMAIL=from@example.com
SENDER_EMAIL_PASS=aaaa bbbb cccc dddd
RECEIVER_EMAIL=receiver@example.com
EOF'
sudo chmod 600 /etc/default/logmonitor
sudo chown root:root /etc/default/logmonitor
```

**4. Create the systemd unit file**

```bash
sudo bash -c 'cat >/etc/systemd/system/logmonitor.service << "EOF"
[Unit]
Description=Log Monitor (journalctl follower with email batching)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
# If using venv:
ExecStart=/opt/logmonitor/.venv/bin/python /opt/logmonitor/run.py
WorkingDirectory=/opt/logmonitor
User=logmon
Group=logmon
EnvironmentFile=-/etc/default/logmonitor
Environment=PYTHONUNBUFFERED=1
Restart=always
RestartSec=3
# Send your app logs to the journal
StandardOutput=journal
StandardError=journal
# Mild hardening:
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=full
ProtectHome=yes
ReadWritePaths=/opt/logmonitor
# Networking is needed for email, so do not over-restrict AFs here.

[Install]
WantedBy=multi-user.target
EOF'
```
> If you didn’t use a venv, point ExecStart to `/usr/bin/python3 /opt/logmonitor/run.py`
> Also, Make sure to change the `EnvironmentFile` to point to the correct location of your env file.

**5. Start and enable the service**
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now logmonitor
systemctl status logmonitor
sudo systemctl restart logmonitor # Restart the service if needed
```

**6. Monitor logs**
```bash
journalctl -u logmonitor -f
```

**7. Stop the service**
```bash
sudo systemctl stop logmonitor # Stop the currently running service
sudo systemctl disable logmonitor # Disable the service from starting on boot *Does not stop if currently running*
```

<!-- Running Tests -->
### :test_tube: Running Tests

To run tests, run the following command
```bash
# Open another terminal
su - # trying to login in as root
# Enter wrong password
```


<!-- Usage -->
## :eyes: Usage

The Log Monitoring and Alert System is designed for system administrators who want real-time visibility into critical log events without being glued to the terminal.

Once started, the script will:
- Continuously monitor system logs (`journalctl -f`).
- Detect suspicious entries such as **failed login attempts**, **sudo misuse**, or **segfaults**.
- Send an **immediate email alert** when a new issue appears.
- Apply **rate-limiting** to avoid mailbox spam during brute-force attacks.
- Summarize repeated log lines into a **single digest email** after the cooldown.

This makes it useful for:
- 🔐 Securing Linux servers against brute-force attacks
- 📊 Monitoring privilege escalation attempts
- 💾 Detecting kernel crashes, OOM (Out-of-Memory) events, and segfaults
- 📬 Keeping system admins in the loop even when they’re away from the server


<!-- ROADMAP -->
## :compass: Roadmap

- [ ] Add support for multiple alert channels (Slack, Discord, Telegram, SMS) in addition to email
- [ ] Build a dashboard GUI to view logs, alerts, and suppression stats in real time
- [ ] Introduce machine learning–based anomaly detection to catch unusual log patterns
- [ ] Add support for non-systemd systems (like syslog or custom log files)
- [ ] Implement a containerized version (Docker) for easier deployment
- [ ] Provide pre-built packages (.deb, .rpm, PyPI release) for easy installation

See the [open issues](https://github.com/Adhik-6/log-monitor-alert/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## :wave: Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- FAQ -->
## :grey_question: FAQ

- Do I need root privileges to run this tool?
  + Not always. If your user has permission to read logs via `journalctl`, you’re good. Otherwise, you may need to run with `sudo`.

- Will this work on Windows or macOS?
  + No. This project is **Linux-specific** because it relies on `journalctl` (systemd). For other platforms, you’d need to adapt it to their log systems.

- Can I use this with Gmail/Outlook for alerts?
  + Yes! Just configure your SMTP credentials. For Gmail, you may need an **App Password**.

- Won’t my inbox get flooded during brute-force attacks?
  + Nope 🚫📬. The tool has **rate-limiting** + **de-duplication**, so repeated identical log entries are suppressed and summarized into a single email after the cooldown.

- What happens if my server loses internet temporarily?
  + The script won’t be able to send emails during downtime, but it will continue monitoring logs. Once the connection is restored, it resumes sending alerts.
  
- How do I stop the tool if it’s running?
  + Just press `sudo systemctl disable logmonitor` in the terminal to stop monitoring.


<!-- Acknowledgments -->
## :gem: Acknowledgements

 - [ChartGPT](https://chatgpt.com)
 - [Shields.io](https://shields.io/)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [Readme Template](https://github.com/othneildrew/Best-README-Template)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
