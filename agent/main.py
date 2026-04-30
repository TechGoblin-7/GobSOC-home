import time
import json
from collector import get_system_metrics

def run_agent():
    try:
        while True:
            metrics = get_system_metrics()

            print(json.dumps(metrics, indent=2))

            time.sleep(2)
    except KeyboardInterrupt:
        print("Agent Stopped Successfully.")

if __name__ == "__main__":
    run_agent()
        