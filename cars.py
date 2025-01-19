from interfaces import Planner

class CarPlanner(Planner):

    def calculate_trip(self, point_a: str, point_b: str):
        # see flights.py for brief explanation
        pass


if __name__ == '__main__':
    # example usage
    cp = CarPlanner()
    cp.calculate_trip(point_a="New York City", point_b="Chicago")
    print(cp.get_trip_details())