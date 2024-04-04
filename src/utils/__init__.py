"""
Basic functions are located here which are used in the project.
"""

from .base.libraries import wraps, time

def retry(exceptions, total_tries=4, initial_wait=0.5, backoff_factor=2, logger=None):
    def retry_decorator(f):
        @wraps(f)
        def func_with_retries(*args, **kwargs):
            _tries, _delay = total_tries + 1, initial_wait
            while _tries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    _tries -= 1
                    print_args = ', '.join(map(str, args)) if args else 'No args'
                    func_name = f.__name__
                    exc_message = repr(e)
                    if _tries == 1:
                        msg = "Function:" + func_name + "\n" + \
                            "Failed despite best efforts after" + str(total_tries) + "tries." + "\n" \
                            "Arguments:" + print_args + "\n" + \
                            "Kwargs:" + str(kwargs) + "\n" + \
                            "Exception:" + exc_message
                        logger.error(msg)
                        raise

                    # Using Same for the retry message
                    msg = "Function:" + func_name + "\n" + \
                        "Failed with exception:" + exc_message + "\n" + \
                        "Retrying in" + str(_delay) + "seconds..." + "\n" + \
                        "Arguments:" + print_args + "\n" + \
                        "Kwargs:" + str(kwargs) + "\n" + \
                        "Attempts left:" + str(_tries)
                    logger.warning(f"msg: {msg}")
                    time.sleep(_delay)

                    _delay *= backoff_factor    # wait longer before retrying

        return func_with_retries
    return retry_decorator
