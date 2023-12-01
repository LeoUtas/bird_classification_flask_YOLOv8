import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "Bird_classification"

list_of_files = [
    f"{project_name}",
    f"{project_name}/models",
    f"{project_name}/data_ingestion.py",
    f"{project_name}/get_prediction.py",
    f"{project_name}/data",
    "templates",
    "templates/index.html",
    "static",
    "static/images",
    "static/styles",
    "main.py",
    "app.py",
    "logger.py",
    "exception.py",
    "requirements.txt",
]

for file_path in list_of_files:
    file_path = Path(file_path)

    # if it's a directory or doesn't have a dot (assuming it's a directory)
    if file_path.is_dir() or "." not in file_path.name:
        if not file_path.exists():
            os.makedirs(file_path, exist_ok=True)
            logging.info(f"Created directory: {file_path}")
        else:
            logging.info(
                f"Directory {file_path} already exists => re-creating ignored."
            )
    else:
        file_dir, file_name = os.path.split(file_path)

        if file_dir != "" and not Path(file_dir).exists():
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Created directory: {file_dir} for the file {file_name}")

        # if the file does not exist or it's not empty (i.e., its size is 0)
        if not file_path.exists() or file_path.stat().st_size == 0:
            with open(file_path, "w") as f:
                pass
            logging.info(f"Created an empty file: {file_name}")
        else:
            logging.info(
                f"File {file_name} already exists and is not empty => re-creating ignored."
            )
