
## TODO
- [ ] check logmon's group (adm or systemd-journal)
- [ ] permission & ownership of /etc/default/logmonitor
- [ ] make sure brute-force attacks, privilege escalation are detected
- [ ] Integration with ELK Stack, Splunk, or Graylog
- [ ] Use logrotate to archive old logs and compress them securely
- [ ] Store alerts and logs in structured directories with proper permissions
- [ ] Harden log access using chmod, auditctl, or SELinux contexts

## Report doubt
1. Title page
   - month name 
2. Bonafide page
   - From and To month 
   - Internal Guide inital & studies. HOD details 

## Note
- Cron is Not suitable here so we are using this as a systemd Service.


### Getting started

1. Clone the repository [log_monitoring_and_alert](https://github.com/Adhik-6/log-monitor-alert) in `/opt/logmonitor`

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

2) Create a dedicated service user

Keeps things safer than running as root.

```bash
sudo useradd --system --no-create-home --shell /usr/sbin/nologin logmon
sudo chown -R logmon:logmon /opt/logmonitor
```

A dedicated service user has been created for running the log monitoring service with no home directory and a restricted shell. We then give ownership of the log monitoring directory to this user for better security.


3) Give the service user permission to read the journal

Depending on distro, it’s either systemd-journal or adm. Add to both safely:
```bash
getent group systemd-journal && sudo usermod -aG systemd-journal logmon
getent group adm && sudo usermod -aG adm logmon
```


4) Put secrets in an env file

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

5) Create the systemd unit file
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
> Make sure to change the `EnvironmentFile` to point to the correct location of your env file.

6) Start and enable the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now logmonitor
systemctl status logmonitor
sudo systemctl restart logmonitor # Restart the service if needed
```

7) Monitor logs
```bash
journalctl -u logmonitor -f
```

8) Stop the service
```bash
sudo systemctl stop logmonitor # Stop the currently running service
sudo systemctl disable logmonitor # Disable the service from starting on boot *Does not stop if currently running*
```

9) Testing
```bash
# Open another terminal
su - # trying to login in as root
# Enter wrong password
```