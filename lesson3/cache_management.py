@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with some args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
        return _f
