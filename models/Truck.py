# A Truck contains a list of packages and a name (ex. "Truck 1")
# Trucks load packages from the hub and unload them at a Location
from models.Graph import Graph


class Truck:
    # each truck has a current location, and all trucks start at the hub
    def __init__(self, name):
        self.name = name
        self.location = "4001 South 700 East"
        # cargo to hold packages
        self.priority_cargo = []
        self.cargo = []
        self.delivered = []
        self.mileage = 0
        self.routes = Graph()

    # check package priority and load
    def load_package(self, package):
        if package.deadline != "EOD":
            self.priority_cargo.append(package)
        else :
            self.cargo.append(package)

    def unload_package(self, package):
        packages = []
        if self.priority_cargo:
            packages = self.priority_cargo
        else:
            packages = self.cargo
        package.status = "Delivered at %f miles" % (self.mileage)
        packages.remove(package)
        self.delivered.append(package)


    # implement the Greedy Algorithm - making the most optimal choice at a given point without concern for big picture
    # travel to the closest destination from each current destination until no more packages
    def deliver(self):
        # deliver priority
        while len(self.priority_cargo) > 0:
            # get the package that has the next closest delivery
            next = self.next_closest(self.location, self.priority_cargo)
            # "move" the truck to the next location and update mileage
            self.mileage += self.routes.distance_between(self.location, next.address)
            self.location = next.address
            # "deliver" the package
            self.unload_package(next)
        # deliver all remaining packages
        while len(self.cargo) > 0:
            next = self.next_closest(self.location, self.cargo)
            self.mileage += self.routes.distance_between(self.location, next.address)
            self.location = next.address
            # "deliver" the package
            self.unload_package(next)

    def next_closest(self, location, packages):
        next = packages[0]
        min_distance = self.routes.distance_between(location, packages[0].address)
        for p in packages:
            p_distance = self.routes.distance_between(location, p.address)
            if p_distance < min_distance:
                min_distance = p_distance
                next = p
        return next


    # prints an overview of the truck status, including name, location, packages held
    # then prints priority packages held
    # then prints remaining packages held
    def print(self):
        print("%s | Location: %s | Mileage: %f | Packages Held: %s | Delivered: " % (self.name, self.location, self.mileage, len(self.cargo) + len(self.priority_cargo)), len(self.delivered))
        if self.priority_cargo:
            print("Priority Cargo:")
            for p in range(len(self.priority_cargo)):
                print("---package", self.priority_cargo[p])
        if self.cargo:
            print("Cargo:")
            for p in range(len(self.cargo)):
                print("---package", self.cargo[p])
        if self.delivered:
            print("Delivered:")
            for p in self.delivered:
                print("---package " + str(p.id) + ": " + p.status)
        print()