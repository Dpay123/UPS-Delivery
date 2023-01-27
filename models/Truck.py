# A Truck contains a list of packages and a name (ex. "Truck 1")
# Trucks load packages from the hub and unload them at a Location
class Truck:
    # each truck has a current location, and all trucks start at the hub
    def __init__(self, name):
        self.name = name
        self.location = "4001 South 700 East"
        # cargo to hold packages
        self.priority_cargo = []
        self.cargo = []

    # check package priority and load
    def load_package(self, package):
        if package.deadline != "EOD":
            self.priority_cargo.append(package)
        else :
            self.cargo.append(package)

    def unload_package(self, package):
        package.status = "Delivered"
        self.location = package.address
        if package in self.priority_cargo:
            self.priority_cargo.remove(package)
        elif package in self.cargo:
            self.cargo.remove(package)
        else:
            print("package not found")
        print("delivered: " + str(package))

    # given a package to deliver, simulate "traveling" to that destination
    # unload the package at that destination
    # update the truck location and mileage
    def deliver(self, package):
        self.location = package.address

    # prints an overview of the truck status, including name, location, packages held
    # then prints priority packages held
    # then prints remaining packages held
    def print(self):
        print("%s | Location: %s | Packages Held: %s" % (self.name, self.location, len(self.cargo) + len(self.priority_cargo)))
        for p in range(len(self.priority_cargo)):
            print("---priority package", self.priority_cargo[p])
        for p in range(len(self.cargo)):
            print("---package", self.cargo[p])
        print()