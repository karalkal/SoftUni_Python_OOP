class Glass:
    capacity = 250

    def __init__(self, content=0):
        self.content = content

    def fill(self, to_add):
        if self.content + to_add <= Glass.capacity:
            self.content += to_add
            return f"Glass filled with {to_add} ml"

        return f"Cannot add {to_add} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
