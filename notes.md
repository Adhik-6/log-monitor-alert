

## TODO
- [ ] Integration with ELK Stack, Splunk, or Graylog
- [ ] Use logrotate to archive old logs and compress them securely
- [ ] Store alerts and logs in structured directories with proper permissions
- [ ] Harden log access using chmod, auditctl, or SELinux contexts


### Getting started

1. Pull from github [log_monitoring_and_alert](https://github.com/Adhik-6/log-monitor-alert)




(Optional) Create a virtualenv:

cd /opt/logmonitor
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt  