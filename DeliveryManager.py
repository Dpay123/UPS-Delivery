from Truck import Truck


class DeliveryManager:
    def __init__(self, packages, graph):
        # holds the inventory of packages
        self.packages = packages
        # holds the graph with the distance/location data
        self.routes = graph
        # holds the mileage driven by trucks
        self.mileage = 0
        # create two trucks
        self.truck1 = Truck("Truck 1")
        self.truck2 = Truck("Truck 2")

    def truck_deliver_packages(self, truck):
        # TODO
        return

    def status(self):
        self.packages.print()
        self.truck1.print()
        self.truck2.print()
        print("Miles Traveled: %d" % self.mileage)
