from interfaces import Planner

class FlightPlanner(Planner):
    """
    Because this class inherits from Planner, all concrete methods/properties will be available. Anything marked with
    @abstractmethod will require implementation by the inheriting class
    """

    def calculate_trip(self, point_a: str, point_b: str):
        """
        Note: all the hard work will be done from this function. If your trip will require another kind of planner to
        complete, it needs to have an instance of that planner stood up to complete the trip. Example: a drive to the
        airport might be trivial, but not in all cases. FlightPlanner should account for that when calculating the trip.
        This will require the other classes to be complete and in working order, but you can write your code to follow
        the same interface you're designing: CarPlanner will have a calculate_trip() function and distance, cost, and
        time attributes.

        """
        pass

if __name__ == '__main__':
    # example of how to use this class
    fp = FlightPlanner()
    fp.calculate_trip(point_a="New York City", point_b="Chicago")
    print(fp.get_trip_details())
