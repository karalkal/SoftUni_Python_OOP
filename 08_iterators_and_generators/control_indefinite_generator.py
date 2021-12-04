def first():
    number = 0
    while True:
        yield number
        number += 1


def second(times):
    result = []
    # for num in first():
    #     if times == 0:
    #         return result
    #
    #     result.append(num * 10)
    #     times -= 1
# SAME AS
    for num in first():
            if times == 0:
                break
            result.append(num * 10)
            times -= 1
    return result


print(second(8))
