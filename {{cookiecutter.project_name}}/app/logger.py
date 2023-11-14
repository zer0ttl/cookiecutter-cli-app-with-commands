import logging
import logging.config
import sys
import time
import yaml
from pathlib import Path
from datetime import datetime


class UTCFormatter(logging.Formatter):
    """Format logging asctime to UTC"""
    converter = time.gmtime


def setup_log_dirs():
    """Creates logging directories and log files.

    Returns:
        log_file (Path): The Path object for the log file generated on every run of the script.
        rotating_log_file (Path): The Path object for the rotating log file. 
    """
    log_dir = Path(__file__).parent / "logs" # Log directory name
    log_dir.mkdir(parents=True, exist_ok=True)
    fmt_date = datetime.utcnow().strftime('%Y%m%d-%H%M%SZ')
    log_file = log_dir / (fmt_date + ".log") # Single Log file name
    rotating_log_file = log_dir / "debug.log" # Rotating Log file name
    return log_file, rotating_log_file

def setup_logging():
    """Configures logging using settings from the yaml config file."""
    log_file, rotating_log_file = setup_log_dirs()
    log_config_file = Path(__file__).parent / "logger.yaml" # Log configuration file

    if not log_config_file.exists():
        sys.exit(1)
    
    with open(log_config_file, 'rt') as file:
        config_log = yaml.safe_load(file.read())
        config_log['handlers']['rotatingFileHandler']['filename'] = rotating_log_file # Doing this because I cannot find a way to input python code into yaml.
        config_log['handlers']['singleFileHandler']['filename'] = log_file
        logging.config.dictConfig(config_log)