import functools
import logging
import sys
import time

from signal import signal, SIGINT, default_int_handler

logger = logging.getLogger(__name__)

def timer(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        start_time = time.perf_counter()
        
        output = func(*args, **kwargs)
        
        # Do something after
        end_time = time.perf_counter()
        run_time = end_time - start_time
        # breakpoint()
        logger.debug(f'Finished {func.__name__!r} from {func.__module__} in {run_time:.4f} secs.')
        return output
    return wrapper_decorator

def signal_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        def signal_handler(received_signal, frame):
            """Function to handle Ctrl-C and Keyboard interrupts
            
            Args:
                received_signal:
                frame: 
            """
            logging.info(f"SIGINT or CTRL-C detected. Exiting gracefully...")
            # Restore the default Ctrl+C signal handler after the function is executed
            signal(SIGINT, default_int_handler)
            sys.exit(1)

        # Change the signal handler to signal_handler before function execution
        signal(SIGINT, signal_handler)

        # Original function call
        result = func(*args, **kwargs)

        return result

    return wrapper