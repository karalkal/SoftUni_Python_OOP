def even_parameters(function_to_decorate):
    def wrapper(*args):
        error_message = "Please use only even numbers!"
        result = ""
        invalid = False
        for ch in args:
            if not isinstance(ch, int):
                result = error_message
                invalid = True
                break
            elif int(ch) % 2 == 1:
                result = error_message
                invalid = True
                break
        if not invalid:
            result = function_to_decorate(*args)
        return result

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
