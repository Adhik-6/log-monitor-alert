
from src.logMonitor import LogMonitor
from utils.configLoader import loadConfig

def main():
  config = loadConfig()
  print("Log monitor running")
  patterns = config['patterns'] if 'patterns' in config else []

  monitor = LogMonitor(patterns)

  try:
    monitor.checkLogs()
  except KeyboardInterrupt:
    print("\nLog monitoring stopped.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()