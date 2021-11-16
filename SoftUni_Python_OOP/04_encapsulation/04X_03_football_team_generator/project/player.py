class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return f"""Player: {self.name}
Sprint: {self.__sprint}
Dribble: {self.__dribble}
Passing: {self.__passing}
Shooting: {self.__shooting}"""
