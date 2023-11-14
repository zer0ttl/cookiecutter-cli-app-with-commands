import logging

from argparse import _SubParsersAction

from decorators import timer

logger = logging.getLogger(__name__)

# @timer
def run(*args, **kwargs):
    # Logic for {{cookiecutter.command}}
    logger.info(f"Command {{cookiecutter.command}} ran with arg1 {kwargs.get('args').arg1} and flag1 {kwargs.get('args').flag1}")
    logger.info(f"Api key is {kwargs.get('api_key')}")
    logger.debug(f"Debug info about add")
    print(f"Running add with arg: {kwargs.get('args').arg1}")


def setup_add(command_subparser: _SubParsersAction):
    parser = command_subparser.add_parser("{{cookiecutter.command}}", help="Add two or more numbers")
    # Add arguments and flags specific to command {{cookiecutter.command}}
    parser.add_argument("arg1", help="Argument for {{cookiecutter.command}}")
    parser.add_argument("--flag1", help="Flag for {{cookiecutter.command}}")
    parser.set_defaults(func=run)
