from interfaces import Planner

class BusPlanner(Planner):

    def calculate_trip(self, point_a: str, point_b: str):
        # see flights.py for a brief explanation
        pass

if __name__ == '__main__':
    bp = BusPlanner()
    bp.calculate_trip(point_a="New York City", point_b="Chicago")
    print(bp.get_trip_details())
    bp.cost = 156.87
    print(bp.cost)