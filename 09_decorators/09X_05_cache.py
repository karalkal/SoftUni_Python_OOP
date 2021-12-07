def cache(func):
    log = {}

    def wrapper(number):
        if number in log:
            return log[number]
        else:
            value = func(number)
            log[number] = value
            return value

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
