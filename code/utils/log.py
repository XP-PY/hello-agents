import logging
from pathlib import Path

def setup_logging(log_path: Path) -> None:
    # log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf8"),
            logging.StreamHandler(),
        ],
    )

def log_info(message: str) -> None:
    logging.info(message)