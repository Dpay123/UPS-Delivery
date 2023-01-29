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

        # holds the mileage driven by trucks
        self.mileage = 0
        # create three trucks (in reality, the third truck will be whichever of truck 1/2 returns to hub)
        self.truck1 = Truck("Truck 1")
        self.truck2 = Truck("Truck 2")

    # Remove a package from the hub and add to the specified truck
    def transfer_package_to_truck(self, package_id, truck):
        # remove package from hub
        p = self.hub.remove(package_id)
        # set package status
        p.status = "En Route"
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

    # After truck 1/2 are done delivered, they currently reside at their last delivery point
    # we want to recall the CLOSEST truck back to the hub to minimize mileage
    def load_third_truck(self):
        # identify which truck is closer and recall it
        truck1_distance_to_hub = self.routes.distance_between("4001 South 700 East", self.truck1.location)
        truck2_distance_to_hub = self.routes.distance_between("4001 South 700 East", self.truck2.location)
        recall_distance = 0

        if truck1_distance_to_hub < truck2_distance_to_hub:
            self.truck3 = self.truck1
            recall_distance += truck1_distance_to_hub
        else:
            self.truck3 = self.truck2
            recall_distance += truck2_distance_to_hub

        # change the name of the truck to be recalled for printing methods
        self.truck3.name = "Truck 3"

        # Bring that truck back to the hub and reset its mileage and deliveries
        self.truck3.location = "4001 South 700 East"
        self.mileage += recall_distance
        self.truck3.mileage = 0
        self.truck3.delivered.clear()

        # simply load the remaining packages at hub
        for i in range(40):
            if self.hub.table[i]:
                self.transfer_package_to_truck(i+1, self.truck3)

    def run(self):
        self.truck1.deliver()
        self.truck2.deliver()
        self.mileage += self.truck1.mileage + self.truck2.mileage
        self.load_third_truck()
        self.truck3.deliver()
        self.mileage += self.truck3.mileage
        self.status()

    def status(self):
        if self.hub:
            self.hub.print()
        self.truck1.print()
        self.truck2.print()
        print("Miles Traveled: %f" % self.mileage)
        print()
