# import logging
# from pathlib import Path

# def setup_logging(log_path: Path) -> None:
#     # log_path.parent.mkdir(parents=True, exist_ok=True)
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s",
#         handlers=[
#             logging.FileHandler(log_path, encoding="utf8"),
#             logging.StreamHandler(),
#         ],
#     )

# def log_info(message: str) -> None:
#     logging.info(message)

import logging
from pathlib import Path

logger = logging.getLogger("my_log")

def setup_logging(log_path: Path) -> None:
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(log_path, encoding="utf8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

def log_info(message: str) -> None:
    logger.info(message)