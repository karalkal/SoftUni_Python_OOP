from datetime import datetime


def exec_time(func_to_measure):
    def wrapper(*args):
        start_time = datetime.now()
        func_to_measure(*args)
        end_time = datetime.now()
        return (end_time - start_time).total_seconds()

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
