from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import timedelta

@dataclass
class TripDetails:
    distance: float
    cost: float
    time: timedelta

class Planner(ABC):

    def __init__(self):
        self._distance = 0.0
        self._cost = 0.0
        self._time = timedelta(days=0, hours=0, minutes=0)


    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @distance.deleter
    def distance(self):
        del self.distance

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @cost.deleter
    def cost(self):
        del self.cost

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @time.deleter
    def time(self):
        del self.time

    @abstractmethod
    def calculate_trip(self, point_a: str, point_b: str):
        """
        calculate trip uses class variables point_a and point_b to calculate
        trip details, using other planner objects as needed to create an
        end-to-end trip
        :param point_a: starting point of trip
        :param point_b: ending point of trip
        :return: None; function should set distance, cost, and time
        """
        pass

    def get_trip_details(self) -> TripDetails:
        """
        returns @TripDetails object of trip details
        """
        return TripDetails(self.distance, self.cost, self.time)

    def clear(self):
        """
        Clears class values
        """
        print(f"Clearing {self.__class__.__name__} data")
        del self.distance, self.cost, self.time
