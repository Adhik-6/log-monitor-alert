import re, subprocess
from alerts.emailAlerts import sendEmailAlerts

class LogMonitor:

    def __init__(self, pattern=None):
        self.patterns = [re.compile(x, re.I) for x in pattern] if pattern else []

    def checkLogs(self):
        try:
            process = subprocess.Popen(
    		[
		    "journalctl", "-x", "-f",
		    "--since=now",
		    # "-o", "json",
		    "SYSLOG_FACILITY=4",  # auth
		    "+",
		    "SYSLOG_FACILITY=10", # authpriv
		],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            for line in process.stdout:
                if self._checkPatterns(line):
                    print(f"Log alert:- {line.strip()}")
                    sendEmailAlerts(line.strip())

        except subprocess.CalledProcessError as e:
            print(f"Error running journalctl: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _checkPatterns(self, line):
        return any(pattern.search(line) for pattern in self.patterns)
