
from src.logMonitor import LogMonitor
from utils.configLoader import loadConfig
import time

def main():
  config = loadConfig()
  # print("Configuration loaded:", config['log_paths'])
  print("Log monitor running")
  # logFiles = config['log_paths'][0]
  patterns = config['patterns'] if 'patterns' in config else []
  # patterns = [ r"error", r"failed", r"unauthorized", r"denied", r"segfault" ]
  # r"Failed password", r"invalid user .* from .*", r"session opened for user"

  monitor = LogMonitor(patterns)

  try:
    # while True:
    monitor.checkLogs()
      # time.sleep(config['system_settings']['sleep_interval'])
  except KeyboardInterrupt:
    print("Log monitoring stopped.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()