def genrange(start, end):
    for number in range(start, end + 1):
        yield number


print(list(genrange(1, 10)))
