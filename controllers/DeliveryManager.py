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
        # create two trucks
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

    # when either truck 1 or truck 2 returns, load the remaining packages onto that truck
    def load_third_truck(self, truck):
        # simply load the remaining packages at hub
        for i in range(40):
            if self.hub.table[i]:
                self.transfer_package_to_truck(i+1, truck)
        truck.name = "Truck 3"

    # implement the Greedy Algorithm - making the most optimal choice at a given point without concern for big picture
    # travel to the closest destination from each current destination until no more packages
    # return the mileage traveled by the truck
    def truck_deliver_packages(self, truck):
        # deliver all priority packages
        while len(truck.priority_cargo) > 0:
            # get the package that has the next closest delivery address
            next = self.next_closest(truck.location, truck.priority_cargo)
            # "move" the truck to the next location and update mileage
            self.mileage += self.routes.distance_between(truck.location, next.address)
            # "deliver" the package
            truck.unload_package(next)
        # deliver all remaining packages
        while len(truck.cargo) > 0:
            next = self.next_closest(truck.location, truck.cargo)
            self.mileage += self.routes.distance_between(truck.location, next.address)
            truck.unload_package(next)

    # From the trucks current location, determine the closest package delivery
    # from the given list of packages held by the truck
    def next_closest(self, truck_location, packages):
        next = packages[0]
        min_distance = self.routes.distance_between(truck_location, packages[0].address)
        for p in packages:
            p_distance = self.routes.distance_between(truck_location, p.address)
            if p_distance < min_distance:
                min_distance = p_distance
                next = p
        return next

    def status(self):
        self.hub.print()
        self.truck1.print()
        self.truck2.print()
        print("Miles Traveled: %f" % self.mileage)
        print()
