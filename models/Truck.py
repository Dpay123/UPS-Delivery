import datetime

from models.Graph import Graph

# A Truck loads, holds and delivers Packages
# Packages are loaded at the hub as priority, regular cargo, or delayed
# As a truck delivers packages, it accumulates Mileage
# Mileage is determined based on the routes between the locations
class Truck:
    # each truck has a current location, and all trucks start at the hub with 0 mileage
    # delivered packages are kept track of in a list
    # distance is calculated using a graph of loaded location data
    # each truck has access to a Graph for planning routes/distances
    def __init__(self, name):
        self.name = name
        self.location = "4001 South 700 East"
        # embark mileage will be assigned on truck delivery
        self.embark_mileage = 0
        self.mileage = 0
        self.routes = Graph()
        # lists to hold packages
        self.priority_cargo = []
        self.cargo = []
        self.delayed_cargo = []
        self.delivered = []

    # check package priority and load onto truck from hub
    # a package has priority if it has a delivery requirement such as time
    def load_package(self, package):
        if package.deadline == "DELAY":
            self.delayed_cargo.append(package)
        elif package.deadline != "EOD":
            self.priority_cargo.append(package)
        else:
            self.cargo.append(package)

    # transfer a package from held cargo to delivered cargo, simulating "delivery"
    def unload_package(self, package):
        # priority packages are always delivered first; if none, then regular cargo; if none, then delayed cargo
        packages = []
        if self.priority_cargo:
            packages = self.priority_cargo
        elif self.cargo:
            packages = self.cargo
        else:
            packages = self.delayed_cargo

        # change package status to mark delivery
        package.delivered_at = self.time_at_miles(self.mileage + self.embark_mileage)
        package.status = "Delivered by %s at %s" % (self.name, package.delivered_at.strftime("%H:%M"))

        # transfer package from held cargo to delivered cargo
        packages.remove(package)
        self.delivered.append(package)

    # calculate the time elapsed based upon mileage traveled
    def time_at_miles(self, miles):
        travel_time = datetime.timedelta(hours=miles / 18)
        start_time = datetime.datetime(year=1900, month=1, day=1, hour=8, minute=0)
        return start_time + travel_time


    # when delivery begins, mark the embark mileage (used to calculate individual time of delivery
    # implement the Greedy Algorithm - making the most optimal choice at a given point without concern for big picture
    # travel to the closest destination from each current destination until no more packages
    def deliver(self, embark_mileage):
        # set embark mileage of trucks and
        self.embark_mileage += embark_mileage
        # deliver priority packages first
        while len(self.priority_cargo) > 0:
            # get the package that has the next closest delivery
            next = self.next_closest(self.location, self.priority_cargo)
            # "move" the truck to the next location and update mileage
            self.mileage += self.routes.distance_between(self.location, next.address)
            self.location = next.address
            # "deliver" the package
            self.unload_package(next)
        # deliver regular packages
        while len(self.cargo) > 0:
            next = self.next_closest(self.location, self.cargo)
            self.mileage += self.routes.distance_between(self.location, next.address)
            self.location = next.address
            # "deliver" the package
            self.unload_package(next)
        # deliver delayed packages
        while len(self.delayed_cargo) > 0:
            next = self.next_closest(self.location, self.delayed_cargo)
            self.mileage += self.routes.distance_between(self.location, next.address)
            self.location = next.address
            # "deliver" the package
            self.unload_package(next)

    # return the package with delivery to the closest location from the current truck location
    def next_closest(self, location, packages):
        next = packages[0]
        min_distance = self.routes.distance_between(location, packages[0].address)
        for p in packages:
            p_distance = self.routes.distance_between(location, p.address)
            if p_distance < min_distance:
                min_distance = p_distance
                next = p
        return next

    def get_stats(self):
        print("%s | Embarked: %s | Location: %s | Mileage: %f | Packages Held: %s | Delivered: "
              % (self.name, self.time_at_miles(self.embark_mileage).strftime("%H:%M"), self.location, self.mileage, len(self.cargo) + len(self.priority_cargo)), len(self.delivered))

    # print an overview of the truck status
    def print(self):
        # print truck overview
        self.get_stats()

        for p in self.delivered:
            print(p)
        print()
