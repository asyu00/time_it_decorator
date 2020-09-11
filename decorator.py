def time_it(func):
    def wrapper(*arg, **kw):
        import datetime
        t1 = datetime.datetime.now()
        print(f'Start to time {func.__name__}: {t1}', flush=True)
        res = func(*arg, **kw)
        t2 = datetime.datetime.now()
        print(f'{func.__name__} executed: {t2}', flush=True)
        print(f'Elapsed Time for {func.__name__}: {(t2 - t1)}', flush=True)
        return res
    return wrapper
