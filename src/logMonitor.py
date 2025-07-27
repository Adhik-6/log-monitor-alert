import re
from alerts.emailAlerts import sendEmailAlerts

class LogMonitor:

  def __init__(self, log_file, pattern=None):
    self.log_file = log_file
    self.patterns = [ re.compile(x, re.I) for x in pattern ] if pattern else []
    self.last_position = 0
  
  def checkLog(self):
    try: 
      with open(self.log_file, 'r') as f:
        f.seek(self.last_position)
        newLines = f.readlines()
        self.last_position = f.tell()

        for line in newLines:
          if self._checkPatterns(line):
            print(f"Alert: {line.strip()}")
            # sendEmailAlerts(line.strip())

    except FileNotFoundError:
      print(f"Log file {self.log_file} not found.")
    except Exception as e:
      print(f"An error occurred: {e}")

  def _checkPatterns(self, line):
    return any(re.search(pattern, line) for pattern in self.patterns)