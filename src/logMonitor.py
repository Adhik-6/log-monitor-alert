import re, subprocess
from alerts.emailAlerts import sendEmailAlerts

class LogMonitor:

    def __init__(self, pattern=None, since="1h"):
        """
        :param pattern: List of regex patterns to match.
        :param since: Time frame for journalctl (e.g., '1h', '30m', 'today').
        """
        self.patterns = [re.compile(x, re.I) for x in pattern] if pattern else []
        self.since = since

    def checkLogs(self):
        try:
            process = subprocess.Popen(
                ["journalctl", "-f", "--since=now", "--output=short-iso"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            for line in process.stdout:
                if self._checkPatterns(line):
                    print(f"Alert: {line.strip()}")
                    # sendEmailAlerts(line.strip())

        except subprocess.CalledProcessError as e:
            print(f"Error running journalctl: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _checkPatterns(self, line):
        return any(pattern.search(line) for pattern in self.patterns)
