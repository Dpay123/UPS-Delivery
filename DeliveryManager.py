import csv

from Graphs import Graph
from Location import Location
from MyHashTable import MyHashTable
from Truck import Truck
import datetime

# This is the class that handles the main functionality of the program
# Upon initialization, data is read from the .CSV and loaded into the manager
# creates the package hash table and the distance graph
class DeliveryManager:
    def __init__(self):
        # create and load the inventory of packages
        self.packages = MyHashTable(40)
        self.packages.load_package_data()
        # create and load the graph with the distance/location data
        self.routes = Graph()

        # holds the mileage driven by trucks
        self.mileage = 0
        # create two trucks
        self.truck1 = Truck("Truck 1")
        self.truck2 = Truck("Truck 2")
        # keep track of time
        self.time = datetime.timedelta(hours=8, minutes=0, seconds=0)

    # Remove a package from the hub and add to the specified truck
    def transfer_package_to_truck(self, package_id, truck):
        # remove package from hub
        p = self.packages.remove(package_id)
        # set package status
        p.status = "En Route"
        # load package to truck
        truck.load_package(p)

    # Load truck 1 and truck 2
    def load_first_trucks(self):
        # manual load packages to truck 1
        self.transfer_package_to_truck(1, self.truck1)
        self.transfer_package_to_truck(2, self.truck1)
        self.transfer_package_to_truck(5, self.truck1)
        self.transfer_package_to_truck(11, self.truck1)
        self.transfer_package_to_truck(12, self.truck1)
        self.transfer_package_to_truck(13, self.truck1)
        self.transfer_package_to_truck(14, self.truck1)
        self.transfer_package_to_truck(15, self.truck1)
        self.transfer_package_to_truck(16, self.truck1)
        self.transfer_package_to_truck(19, self.truck1)
        self.transfer_package_to_truck(20, self.truck1)
        self.transfer_package_to_truck(21, self.truck1)
        self.transfer_package_to_truck(22, self.truck1)
        self.transfer_package_to_truck(23, self.truck1)
        self.transfer_package_to_truck(33, self.truck1)
        self.transfer_package_to_truck(40, self.truck1)
        # manual load packages to truck 2
        self.transfer_package_to_truck(3, self.truck2)
        self.transfer_package_to_truck(4, self.truck2)
        self.transfer_package_to_truck(6, self.truck2)
        self.transfer_package_to_truck(17, self.truck2)
        self.transfer_package_to_truck(18, self.truck2)
        self.transfer_package_to_truck(24, self.truck2)
        self.transfer_package_to_truck(25, self.truck2)
        self.transfer_package_to_truck(26, self.truck2)
        self.transfer_package_to_truck(29, self.truck2)
        self.transfer_package_to_truck(30, self.truck2)
        self.transfer_package_to_truck(31, self.truck2)
        self.transfer_package_to_truck(32, self.truck2)
        self.transfer_package_to_truck(34, self.truck2)
        self.transfer_package_to_truck(36, self.truck2)
        self.transfer_package_to_truck(37, self.truck2)
        self.transfer_package_to_truck(38, self.truck2)

    # when either truck 1 or truck 2 returns, load the remaining packages onto that truck
    def load_third_truck(self, truck):
        # simply load the remaining packages at hub
        for i in range(40):
            if self.packages.table[i]:
                self.transfer_package_to_truck(i+1, truck)

    def truck_deliver_packages(self, truck):
        # TODO
        return

    def status(self):
        self.packages.print()
        self.truck1.print()
        self.truck2.print()
        print("Time: ", self.time)
        print("Miles Traveled: %d" % self.mileage)
        print()
