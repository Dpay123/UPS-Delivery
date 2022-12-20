class Truck:
    # each truck contains a list of packages and a name (ex. "Truck 1")
    def __int__(self, name):
        self.name = name
        self.cargo = []

    def load_package(self, package):
        if len(self.cargo) < 16:
            self.cargo.append(package)
