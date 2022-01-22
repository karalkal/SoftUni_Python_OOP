from abc import ABC, abstractmethod


class Car(ABC):
    min_speed_limit = 0
    max_speed_limit = 8888

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False  # One car can be driven by ONLY one driver.

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.min_speed_limit or value > self.max_speed_limit:
            raise ValueError(f"Invalid speed limit! Must be between {self.min_speed_limit} and {self.max_speed_limit}!")
        self.__speed_limit = value
