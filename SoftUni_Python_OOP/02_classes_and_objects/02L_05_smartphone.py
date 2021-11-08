class Smartphone:

    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if True:  # not True is True => False, not not True is True => True
            self.is_on = True

    def install(self, application: str, memory_required: int):
        if not self.is_on:
            return f"Turn on your phone to install {application}"
        if memory_required > self.memory:
            return f"Not enough memory to install {application}"
        # if none of the above
        self.apps.append(application)
        self.memory -= memory_required
        return f"Installing {application}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
