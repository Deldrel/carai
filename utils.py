import time
import traceback


def try_catch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('Exception in function {} with args {} and kwargs {}'.format(func.__name__, args, kwargs))
            traceback.print_exc()
            raise e

    return wrapper


@try_catch
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('Execution time of {} is {} seconds'.format(func.__name__, time.time() - start))
        return result

    return wrapper


@try_catch
def map_range(value, low1, high1, low2, high2):
    return low2 + (value - low1) * (high2 - low2) / (high1 - low1)


@try_catch
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
