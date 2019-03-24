from functools import wraps


def _maybe_substitute_exc(exc, errors_map, func, *args, **kwargs):
    new_error = errors_map.get(exc.__class__)

    if new_error:
        if callable(new_error):
            raise new_error()
        else:
            raise new_error

    else:
        raise exc


def map_errors(errors_map: dict):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return _maybe_substitute_exc(e, errors_map, func, *args, **kwargs)
        return wrapper
    return decorator
