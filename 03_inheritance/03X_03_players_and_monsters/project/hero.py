class Hero:
    def __init__(self, username, level: int):
        self.username = username
        self.level = level
        self.class_name = type(self).__name__

    def __str__(self):
        return f"{self.username} of type {self.class_name} has level {self.level}"
