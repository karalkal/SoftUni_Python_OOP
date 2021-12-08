class store_results:
    def __init__(self, func_to_decorate):
        self.func_to_decorate = func_to_decorate

    def __call__(self, *args, **kwargs):
        # print(self.func_to_decorate.__name__)
        # print(self.func_to_decorate(*args))
        func_name = self.func_to_decorate.__name__
        func_result = self.func_to_decorate(*args)
        # print(f"Function '{func_name}' was called. Result: {func_result}")
        line = f"Function '{func_name}' was called. Result: {func_result}"
        with open("09X_08_stored_results.txt", "a") as records:
            records.write(line + "\n")

@store_results
def add(a, b):
    return a + b

add(2, 2)


@store_results
def mult(a, b):
    return a * b

mult(6, 4)