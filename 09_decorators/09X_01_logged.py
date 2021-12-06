def logged(function):
    def wrapper(*args):
        string_to_return = function(*args)
        func_name_and_params = f"{function.__name__}{(args)}"

        return f"you called {func_name_and_params}\nit returned {string_to_return}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
