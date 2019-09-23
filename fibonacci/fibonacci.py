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
    """A recursive way to calculate the nth fibonacci's number.

    Args:
         int n: The fibonacci number to be calculated
    Return:
        int: The nth fibonacci number
    """
    return 1 if n <= 2 else fib_recursive(n-1) + fib_recursive(n-2)


@memoized
def fib_recursive_memo(n):
    """A recursive way to calculate the nth fibonacci's number
    utilizing memoization to avoid duplicate calculations.

    Args:
         int n: The fibonacci number to be calculated
    Returns:
        int: The nth fibonacci number
    """
    return 1 if n <= 2 else fib_recursive_memo(n-1) + fib_recursive_memo(n-2)


def fib_iterative(n):
    """An iterative way to calculate the nth fibonacci's number.

    Args:
         int n: The fibonacci number to be calculated
    Returns:
        int: The nth fibonacci number
    """
    nums = [None] * n
    for num in range(n):
        nums[num] = 1 if num <= 1 else nums[num-1] + nums[num-2]
    return nums[-1]


def fib_dynamic(n):
    """An iterative way to calculate the nth fibonacci's number.
    Also reduces stored variables to a minimum in order to minimize
    space complexity.

    Args:
         int n: The fibonacci number to be calculated
    Returns:
        int: The nth fibonacci number
    """
    nums = [1, 1]
    for num in range(n-2):
        new_num = sum(nums)
        nums[0] = nums[1]
        nums[1] = new_num
    return nums[-1]


@timed
def fibonacci(n, method="recursive"):
    """A helper method, used to dispatch fibonaci number calculations
    to different calculation methods while tracking execution time.

    Args:
         int n: The fibonacci number to be calculated
         str method:
            - recursive: Simple recursive solution, incurs duplicate
            calculations.
            - memoization: Advanced recursive solution, stores results
            in order to avoid dulicate calculations. Much more efficient
            than the simple recursive method.
            - iterative: Simple iterative solution, does not incur
            duplicate calculations.
            - dynamic: Advanced iterative solution, does not incur duplicate
             calculations. Also reduces the stored variables to a minimum,
             resulting in a smaller memory fingerprint.
    Returns:
        int: The nth fibonacci number
    """
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
