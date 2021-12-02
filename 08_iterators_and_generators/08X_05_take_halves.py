def solution():
    def integers():
        number = 1
        yield number
        while True:
            number += 1
            yield number

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            # num = next(halves())
            num = next(seq)
            result.append(num)
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
