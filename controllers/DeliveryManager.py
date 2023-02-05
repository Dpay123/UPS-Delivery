import datetime
from sqlite3 import Time

from models.Graph import Graph
from models.MyHashTable import MyHashTable
from models.Truck import Truck

# This is the class that handles the main functionality of the program
# Upon initialization, data is read from the .CSV and loaded into the manager
# creates the package hash table and the distance graph
class DeliveryManager:
    def __init__(self):
        # create and load the inventory of packages
        self.hub = MyHashTable(40)
        self.hub.load_package_data()
        # create and load the graph with the distance/location data
        self.routes = Graph()
        # holds the mileage driven cumulatively by all trucks
        self.mileage = 0
        # create three trucks
        self.truck1 = Truck("Truck 1")
        self.truck2 = Truck("Truck 2")
        self.truck3 = Truck("Truck 3")

    # Remove a package from the hub and add to the specified truck
    def transfer_package_to_truck(self, package_id, truck):
        # remove package from hub
        p = self.hub.remove(package_id)
        # set package status
        p.status = "En Route via %s" % truck.name
        # load package to truck
        truck.load_package(p)

    # Load truck 1 and truck 2
    def load_first_trucks(self):
        # manual load packages to truck 1
        truck1 = [1, 2, 5, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 33, 40]
        for id in truck1:
            self.transfer_package_to_truck(id, self.truck1)

        # manual load packages to truck 2
        truck2 = [3, 4, 6, 17, 18, 24, 25, 26, 29, 30, 31, 32, 34, 36, 37, 38]
        for id in truck2:
            self.transfer_package_to_truck(id, self.truck2)

    # recall the CLOSEST truck back to the hub to minimize mileage
    # load the third truck with the remaining packages at the hub
    def load_third_truck(self):
        # identify which truck is closer and recall it
        truck1_distance_to_hub = self.routes.distance_between("4001 South 700 East", self.truck1.location)
        truck2_distance_to_hub = self.routes.distance_between("4001 South 700 East", self.truck2.location)

        if truck1_distance_to_hub < truck2_distance_to_hub:
            self.truck1.mileage += truck1_distance_to_hub
            self.truck1.location = "4001 South 700 East"
            self.mileage += self.truck1.mileage
        else:
            self.truck2.mileage += truck2_distance_to_hub
            self.truck2.location = "4001 South 700 East"
            self.mileage += self.truck2.mileage

        # load the remaining packages at hub
        for i in range(40):
            if self.hub.table[i]:
                self.transfer_package_to_truck(i+1, self.truck3)

    # calculate the time elapsed based upon mileage traveled
    def time_at_miles(self, miles):
        time = miles / 18
        return str(datetime.timedelta(hours=time+8))

    def run(self):
        self.load_first_trucks()
        # truck 1 starts delivery at 0 offset (8am)
        self.truck1.deliver(0)
        # truck 2 starts delivery at 19.5 offset (9:05am)
        self.truck2.deliver(19.5)
        self.load_third_truck()
        # truck 3 starts at offset of mileage of first returned truck
        self.truck3.deliver(self.mileage)
        # total mileage of all trucks
        self.mileage = self.truck1.mileage + self.truck2.mileage + self.truck3.mileage
        self.status()

    def status(self):
        self.truck1.get_stats()
        self.truck2.get_stats()
        self.truck3.get_stats()
        print("Miles Traveled: %f" % self.mileage)
        print("Deliveries Completed by: %s" % self.time_at_miles(self.truck3.mileage + self.truck3.embark_mileage))
        breakdown = input("Would you like to see a complete breakdown of the packages delivered? (enter 'y' or 'n') ")
        if breakdown == "y":
            self.truck1.print()
            self.truck2.print()
            self.truck3.print()
            print("Miles Traveled: %f" % self.mileage)
            print("Deliveries Completed by: %s" % self.time_at_miles(self.truck3.mileage + self.truck3.embark_mileage))
        else:
            print("Simulation Completed...Returning to Main Menu")
