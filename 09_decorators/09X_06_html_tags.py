def tags(tag):
    def decorator(function_to_decorate):
        def wrapper(*args):
            result = function_to_decorate(*args)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
