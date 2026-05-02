import time
import json
import logging
from logging.handlers import RotatingFileHandler
from collector import get_system_metrics

logger = logging.getLogger("gobsoc_agent")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(

    "agent.log",
    maxBytes=1_000_000, #1MB
    backupCount=3   # keep 3 old logs
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

def run_agent():
    logging.info("GobSOC Agent Starting...")

    try:
        while True:
            metrics = get_system_metrics()

            logger.info(json.dumps(metrics))

            print(json.dumps(metrics, indent=2))

            time.sleep(2)

    except KeyboardInterrupt:
        logger.info("GobSOC Agent stopped cleanly.")
        print("\nAgent Stopped Successfully.")

if __name__ == "__main__":
    run_agent()
        