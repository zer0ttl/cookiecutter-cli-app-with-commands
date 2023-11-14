import logging

from argparse import ArgumentParser, Namespace

from commands import {{cookiecutter.command}}

logger = logging.getLogger(__name__)

def parse_arguments() -> Namespace:
    """Function to parse command line arguments"""

    # Create the main parser
    parser = ArgumentParser(
        description="some description about the program/script",
        usage="%(prog)s"
    )

    # Create subparsers for different commands
    command_subparser = parser.add_subparsers(title="Commands")

    # Add your custom commands here:
    # Add the "{{cookiecutter.command}}" command to the command parser
    {{cookiecutter.command}}.setup_add(command_subparser)

    # These are the arguments for the main parser
    # config file
    config_file = ".config"
    parser.add_argument(
        "-c",
        "--config",
        help=f"Path to the config file in ini format. default: {config_file}",
        default=config_file,
        nargs="?"
    )

    # These are the arguments for the main parser
    # Optional Arguments: argument that modifies the script/program's behavior
    # version
    parser.add_argument(
        # -v is usually used for verbose
        "--version",
        action="version",
        version="%(prog)s 0.1"
    )
    return parser.parse_args()