# Python CLI App

- CLI app that accepts commands and some arguments.

## Usage



## Executing the script

The script can be run as follows:

```bash
python {{cookiecutter.directory_name}}/{{cookiecutter.file_name}}.py
```

```text
$ python3 {{cookiecutter.directory_name}}/{{cookiecutter.file_name}}.py add test1 --flag1 testflag1
2023-11-11 08:04:37,922 MDT - INFO - root - Reading config file - /tmp/my-awesome-app/app/.config
2023-11-11 08:04:37,923 MDT - INFO - commands.add - Command add ran with arg1 testarg1 and flag1 testflag1
2023-11-11 08:04:37,923 MDT - INFO - commands.add - Api key is 1234abcd-1234-abcd-abcd-1234abcd
Running add with arg: testarg1
```

## Folder Structure

Now, let's look at the structure of the project and its components:

- `{{cookiecutter.directory_name}}/`: This is the root folder of your command-line application.
- `{{cookiecutter.directory_name}}/__init__.py`: This file marks the app directory as a Python package. It can be empty or contain package-level imports.
- `{{cookiecutter.directory_name}}/{{cookiecutter.file_name}}.py`: This file contains the core logic and entry point for your command-line application. It's responsible for defining the main CLI interface, creating commands, and parsing command-line arguments using a library like argparse.
- `{{cookiecutter.directory_name}}/cli.py`: This file contains the parsers and subparsers for your commands.
- `{{cookiecutter.directory_name}}/errors.py`: This file contains custom erros codes to be used in the app.
- `{{cookiecutter.directory_name}}/decorators.py`: This file contains the decorators to be used in your script. It contains some example decorators.
- `{{cookiecutter.directory_name}}/logger.py`: This file confgiures the logging using the `logger.yaml` file.
- `{{cookiecutter.directory_name}}/.config`: This file contains the config that will be used in your script. This can contain urls, api-keys, other information. The default config is `.config`. You can change this from the `cli.py` file.
- `{{cookiecutter.directory_name}}/commands/`: This directory is where you organize your commands. Each command has its own Python file (e.g., `command1.py`, `command2.py`). This modular approach allows you to add more commands by simply creating additional Python files in this directory.
- `tests/`: This directory holds your unit tests for the commands. There's a separate test file for each command, following the naming convention `test_commandX.py`.
- `setup.py`: This file is for packaging and distribution. You can use it to package your CLI application for distribution through tools like pip.
- `requirements.txt`: This file lists the required dependencies for your CLI application. You can manage it using tools like pip and virtualenv.
- `README.md`: Provide documentation and usage instructions for your CLI application.

## App Structure

- The `{{cookiecutter.directory_name}}/{{cookiecutter.file_name}}.py` contains the main function.
    - It sets up the logging.
    - Configuration is read from `.config` file.
        - Use the `get_option(config, section, option)` to read a config option from the file.
        - A simple `api_key` configuration is provided as an example in `{{cookiecutter.directory_name}}/{{cookiecutter.file_name}}.py`
    - Cleanup functionality is implmeneted in `cleanup()`. It is decorated using `@atexit.register` which makes it run before normal interpreter termination.
- The script supports *commands* using subparsers with `ArgumentParser`.
    - The `{{cookiecutter.directory_name}}/cli.py` contains the main parser and the subparser for commands.
    - Each command is implemented in their own module in `{{cookiecutter.directory_name}}/commands/command_name.py`.
    - The arguments for each command are implemented via `setup_add()` in `{{cookiecutter.directory_name}}/commands/command_name.py`.
    - The main logic of the command is implemented via `run()` in `{{cookiecutter.directory_name}}/commands/command_name.py`.
    - A simple *command* is implemented which showcases techniques to access the arguments, flags, and parameters from the config file.

### Errors

- The `{{cookiecutter.directory_name}}/errors.py` contains custom error codes to be used in the app.
- You can add additional codes to this file and use them in your code.

- Add the custom error code to `error.py`
```python
MY_NEW_ERROR_CODE = 1234567890
```
- Use the new error code in your code.
```python
sys.exit(MY_NEW_ERROR_CODE)
```

### Decorators

- Decorators are implemented in `{{cookiecutter.directory_name}}/decorators.py`.
- Two in-built decorators are provided.
    - `timer()`: Useful for profiling function calls.
    - `signal_handler()`: Handles `Ctrl + C` anywhere in the script.
- You can use these decorators in your code as follows:
```python
@timer
def my_awesome_function():
    ...
    pass
```

### Logging

- Logs are written to `{{cookiecutter.directory_name}}/logs` directory.
- Logging is implemented via `{{cookiecutter.directory_name}}/logger.py`.
- All logs will be written to `{{cookiecutter.directory_name}}/logs` directory. The directory will be created if not present.
- Every script execution will be logged to a separate file in the format `logs/YYYMMDD-HhhmmssZ.log`.
- All debug information is stored in a single file `logs/debug.log`.
- The name, location, size, other parameters are configurable via `logger.yaml`.
- You can configure logging in any of your modules or scripts using the following two lines.
```python
import logging
logger = logging.netLogger(__name__)
```
- Then you add your logging calls.
```python
logging.info("Some info logs")
logging.debug("Some debug logs")
```

#### Logging Configuration

- Logging is configured via `{{cookiecutter.directory_name}}/logger.yaml`.
    - 3 handlers are configured: `console`, `singleFileHandler`, and `rotatingFileHandler`.
    - INFO and above are logged to console.
    - INFO and above are logged to single files. Everytime the script is run, a new log file for that script session is generated in `{{cookiecutter.directory_name}}/logs/YYYMMDD-HhhmmssZ.log`.
        - If the script is launched with just `-h` or `--help`, logs are not generated using the `delay: 5` config under `singleFileHandler`. 
        - Timing information is logged in local time format.
        - You can modify the time format under `formatters` section.
    - DEBUG and above logs are logged to `{{cookiecutter.directory_name}}/logs/debug.log` file. The `debug.log` file is rotated after 10 Mb. Backup count is 20.
        - Timing information is logged in UTC format.

### Configuration

- Configuration options for the app can be saved to `{{cookiecutter.directory_name}}/.config`.
- The configuration is in `ini` format.

#### Configuration Parsing

- Configuration parsing is implemented via `ConfigParser`
- You can add your new configration as follows. You can add a new section and a new option.
```ini
[my-new-section]
my-new-option = some-value-here
```
- Get the value of the new section/option as follows:
1. Add a custom error code for the option to `errors.py`, if required.
```python
INVALID_NEW_OPTION = 10003
```

2. Get the option value
```python
my_new_option = get_option(config, section="my-new-section", option="my-new-option")
if not my_new_option:
    logging.error(f"The config file does not contain a valid my_new_option")
    sys.exit(INVALID_NEW_OPTION)
```

### Commands

- The script supports *commands* using subparsers with `ArgumentParser`.
    - The `{{cookiecutter.directory_name}}/cli.py` contains the main parser and the subparser for commands.
    - Each command is implemented in their own module in `{{cookiecutter.directory_name}}/commands/command_name.py`.
    - The arguments for each command are implemented via `setup_add()` in `{{cookiecutter.directory_name}}/commands/command_name.py`.
    - The main logic of the command is implemented via `run()` in `{{cookiecutter.directory_name}}/commands/command_name.py`.
    - A simple *command* is implemented which showcases techniques to access the arguments, flags, and parameters from the config file.

### Steps to add new commands


1. Add a new file `{{cookiecutter.directory_name}}/commands/my_new_command.py`.
2. Add the command arguments to `setup_add()`.
3. Implement the command logic in `run()`.
4. Import the new command and add to the `command_parser` in `{{cookiecutter.directory_name}}/cli.py`.

Say you want to implement a new command in your script `get_food`. It accepts an argument `arg1` and a flag `flag1`.

- Create command file. Add the following to the file `get_food.py`
```bash
touch {{cookiecutter.directory_name}}/commands/get_food.py
```

```python
import logging

from argparse import _SubParsersAction

from decorators import timer

logger = logging.getLogger(__name__)
```

- Add command arguments via `setup_add()`
```python
def setup_add(command_subparser: _SubParsersAction):
    parser = command_subparser.add_parser("get_food", help="Get Food")
    # Add arguments and flags specific to command get_food
    parser.add_argument("arg1", help="Argument for get_food")
    parser.add_argument("--flag1", help="Flag for get_food")
    parser.set_defaults(func=run)
```

- Implement the command logic in `run()`
```python
def run(*args, **kwargs):
    # Logic for add
    logger.info(f"Command get_food ran with arg1 {kwargs.get('args').arg1} and flag1 {kwargs.get('args').flag1}")
    logger.info(f"Api key is {kwargs.get('api_key')}")
    logger.debug(f"Debug info about add")
    print(f"Running add with arg: {kwargs.get('args').arg1}")
```

### Argument Parsing

- `argparse` is used for parsing arguments.
- The main parser `parser` is responsible for flags/optional arguments for the main app.
    - Be default, it support the `-c` (config) and -`v` (version) flags.
- The commands are parsed using a subparser `command_parser`.
    - Command specific arguments are flags are implmeneted in the respective `command_name.py` files.