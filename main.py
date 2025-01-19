"""
Main file that will start our program
Any initialization will be run here (db, flat files, etc.)
GUI will be kicked off here
"""

import os
import pandas as pd
from dataclasses import dataclass
from gui import Ui
from flights import FlightPlanner
from cars import CarPlanner
from buses import BusPlanner

def main():
    # code here
    gui = Ui()
    flight_planner = FlightPlanner()
    car_planner = CarPlanner()
    bus_planner = BusPlanner()
    print("Running the Program")

if __name__ == "__main__":
    main()