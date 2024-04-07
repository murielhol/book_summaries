def profile(func):
    """
    Decorator that profiles the cimpute time of the decorated function.
    """
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        from line_profiler import LineProfiler

        prof = LineProfiler()
        try:
            return prof(func)(*args, **kwargs)
        finally:
            prof.print_stats()

    return wrapper


def mem_profile(func):
    """
    Decorator that profiles the memory usage of the decorated function.
    """
    # Apply the memory_profiler profile decorator to the function
    from memory_profiler import profile
    func = profile(func)
    def wrapper(*args, **kwargs):
        # Call the decorated function
        return func(*args, **kwargs)
    return wrapper