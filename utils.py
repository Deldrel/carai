import time


def try_catch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('Exception in function {} with args {} and kwargs {}'.format(func.__name__, args, kwargs))
            print('Exception: {}'.format(e))
            exit(1)

    return wrapper


@try_catch
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('Execution time of {} is {} seconds'.format(func.__name__, time.time() - start))
        return result

    return wrapper
