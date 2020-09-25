from functools import wraps


def make_html(element):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return f'<{element}>{function(*args)}</{element}>'

        return wrapper

    return decorator
