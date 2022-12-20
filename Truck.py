from MyHashTable import MyHashTable


class Truck:
    # each truck contains a list of packages and a name (ex. "Truck 1")
    # each truck has a current location, and all trucks start at the hub
    def __init__(self, name):
        self.name = name
        self.location = "4001 South 700 East"
        # initialize a blank table to hold packages on the truck
        self.cargo = MyHashTable(40)

    def load_package(self, package):
        if self.cargo.capacity() < 16:
            self.cargo.insert(package.id, package)

    def unload_package(self, address):
        for package in self.cargo:
            if package.address == self.location:
                self.cargo.remove(package)

    def print(self):
        print("%s | Location: %s | Packages Held: %s\n" % (self.name, self.location, self.cargo.capacity()))
        self.cargo.print()