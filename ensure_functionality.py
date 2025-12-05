from functools import wraps

class FunctionalityError(Exception):
    """Custom exception raised when a decorated function fails to meet expectations."""
    pass

def ensure_functionality(expected_value=None, check_condition=None, error_message="Function did not perform as expected."):
    """
    A decorator that raises an error if the decorated function's result or behavior
    does not meet the specified criteria.

    Args:
        expected_value: The value the function is expected to return.
        check_condition: A callable that takes the function's result as an argument
                         and returns True if the condition is met, False otherwise.
        error_message: The message to include with the FunctionalityError.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if expected_value is not None and result != expected_value:
                raise FunctionalityError(f"{error_message} Expected: {expected_value}, Got: {result}")

            if check_condition is not None and not check_condition(result):
                raise FunctionalityError(f"{error_message} Condition failed for result: {result}")

            return result
        return wrapper
    return decorator

