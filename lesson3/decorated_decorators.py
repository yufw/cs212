def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

## QUIZ: DOES THIS WORK? (YES)

def decorator(d):
    "Make function d a decorator: d wraps a function fn. @author Darius Bacon"
    return lambda fn: update_wrapper(d(fn), fn)

decorator = decorator(decorator)
