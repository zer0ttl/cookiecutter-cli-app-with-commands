import atexit
import logging
import sys
import time 

from configparser import ConfigParser, NoOptionError, NoSectionError
from pathlib import Path
from traceback import format_exc

from cli import parse_arguments
from decorators import signal_handler, timer
from errors import *
from logger import setup_logging

@atexit.register
def cleanup() -> None:
    """Function to perform cleanup activities"""
    elapsed_time = time.perf_counter() - start_time
    logging.debug(f"Time taken to run: {elapsed_time:0.2f} seconds.")

def load_configuration(config_file: str) -> ConfigParser:
    """Load configuration from a file and handle errors"""
    config = ConfigParser()
    config_file = Path(__file__).parent / f"{config_file}"
    try:
        logging.info(f"Reading config file - {config_file}")
        config.read_file(open(config_file))
        return config
    except FileNotFoundError as e:
        logging.error(f"Error reading config file {config_file}. {e}")
        return None

def get_option(config: ConfigParser, section: str, option: str):
    """Function to get option value from config file"""
    try:
        option_value = config.get(section=section, option=option)
        return option_value
    except (NoSectionError) as e:
        logging.error(f"Error reading section {section}. {e}")
        return None
    except (NoOptionError) as e:
        logging.error(f"Error reading option {option}. {e}")
        return None

@signal_handler
def main(args):

    logging.debug(f"--------------------------------------------------------")
    logging.debug(f"Script Execution Started.")

    # reading config file
    config = load_configuration(args.config)
    if not config:
        logging.error(f"The file {args.config} was not found. Please create a new file in the app/.config location. Exiting...")
        sys.exit(CONFIG_FILE_NOT_FOUND)

    api_key = get_option(config, section="api", option="api-key")
    if not api_key:
        logging.error(f"The config file does not contain a valid API key")
        sys.exit(INVALID_API_KEY)

    if hasattr(args, "func"):
        args.func(args=args, api_key=api_key)

if __name__ == "__main__":
    global start_time
    start_time = time.perf_counter()

    setup_logging()
    args = parse_arguments()
    try:   
        main(args)
    except SystemExit as e:
        logging.error(f"[!] SystemExit Code: {e}")
    except:
        logging.error("[!] Uncaught exception")
        logging.error(format_exc())