def type_check(var_type):
    def decorator(function):
        def wrapper(*args):
            valid_args = True
            for ch in args:
                if type(ch) != var_type:
                    valid_args = False
                    return "Bad Type"
            if valid_args:
                return function(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
