class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"

    # def tell_me(self):
    #     return type(self.data)


test_code = Stack()
print(test_code.is_empty())
test_code.data.append("bb")
test_code.data.append("jh")
test_code.data.append("lq")
test_code.data.append("kq")
print(test_code.is_empty())
# print(test_code.tell_me())
print(test_code)
