from MyHashTable import MyHashTable


class Truck:
    # each truck contains a list of packages and a name (ex. "Truck 1")
    # each truck has a current location, and all trucks start at the hub
    def __init__(self, name):
        self.name = name
        self.location = "4001 South 700 East"
        # cargo to hold packages
        self.cargo = []

    def load_package(self, package):
        self.cargo.append(package)

    def unload_package(self, address):
        for package in self.cargo:
            if package.address == self.location:
                self.cargo.remove(package)

    def print(self):
        print("%s | Location: %s | Packages Held: %s" % (self.name, self.location, len(self.cargo)))
        for p in range(len(self.cargo)):
            print("---package", self.cargo[p])
        print()