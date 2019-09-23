import datetime


def timed(func):
    def wrapper(*args, **kwargs):
        time_pre   = datetime.datetime.now()
        result     = func(*args, **kwargs)
        time_post  = datetime.datetime.now()
        time_delta = time_post - time_pre

        print("Executing {} took {}.".format(func.__name__, time_delta))
        return result
    return wrapper


def memoized(func):
    cache = {}

    def wrapper(arg):
        if arg not in cache:
            cache[arg] = func(arg)

        return cache[arg]
    return wrapper


def fib_recursive(n):
    return 1 if n <= 2 else fib_recursive(n-1) + fib_recursive(n-2)


@memoized
def fib_recursive_memo(n):
    return 1 if n <= 2 else fib_recursive_memo(n-1) + fib_recursive_memo(n-2)


def fib_iterative(n):
    nums = [None] * n
    for num in range(n):
        nums[num] = 1 if num <= 1 else nums[num-1] + nums[num-2]
    return nums[-1]


def fib_dynamic(n):
    nums = [1, 1]
    for num in range(n-2):
        new_num = sum(nums)
        nums[0] = nums[1]
        nums[1] = new_num
    return nums[-1]


@timed
def fibonacci(n, method="recursive"):
    if method == "recursive":
        return fib_recursive(n)
    elif method == "memoization":
        return fib_recursive_memo(n)
    elif method == "iterative":
        return fib_iterative(n)
    elif method == "dynamic":
        return fib_dynamic(n)


if __name__ == "__main__":
    print(fibonacci(30, method="recursive"))
    print(fibonacci(307, method="memoization"))
    print(fibonacci(307, method="iterative"))
    print(fibonacci(307, method="dynamic"))
