def squares(param):
    for num in range(1, param + 1):
        yield num ** 2


print(list(squares(5)))
