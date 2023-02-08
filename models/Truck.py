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
    # Time complexity: O(1)
    # Space complexity: O(1)
    def load_package(self, package):
        if package.deadline == "DELAY":
            self.delayed_cargo.append(package)
        elif package.deadline != "EOD":
            self.priority_cargo.append(package)
        else:
            self.cargo.append(package)

    # transfer a package from held cargo to delivered cargo, simulating "delivery"
    # Time : O(n)
    # Space: O(1)
    def unload_package(self, package, p_list):
        # calculate simulated "time" based upon mileage and update the package status
        package.delivered_at = self.time_at_miles(self.mileage + self.embark_mileage)
        package.status = "Delivered by %s at %s" % (self.name, package.delivered_at.strftime("%H:%M"))
        # transfer package from held cargo to delivered cargo
        p_list.remove(package)
        self.delivered.append(package)

    # return a datetime object representation of a time based upon mileage traveled
    def time_at_miles(self, miles):
        # calculate hours elapsed based upon known speed of 18mph
        travel_time = datetime.timedelta(hours=miles / 18)
        # the start time is given to us as 8am
        start_time = datetime.datetime(year=1900, month=1, day=1, hour=8, minute=0)
        return start_time + travel_time

    # Implement the Nearest Neighbor Greedy Algorithm - making the most optimal choice at a given
    # point without concern for big picture
    # Each package held is delivered on a nearest distance basis until all packages have been delivered
    # the parameter embark_mileage is passed in to mimic the "embark time" and will be used to calculate delivery times
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def deliver(self, embark_mileage):
        # set embark mileage of trucks
        self.embark_mileage = embark_mileage
        # deliver all packages in order of priority-->cargo-->delayed
        for p_list in [self.priority_cargo, self.cargo, self.delayed_cargo]:
            while len(p_list) > 0:
                # get the package that has the next closest delivery
                next = self.next_closest(self.location, p_list)
                # "move" the truck to the next location and update mileage
                self.mileage += self.routes.distance_between(self.location, next.address)
                self.location = next.address
                # "deliver" the package
                self.unload_package(next, p_list)

    # Return the package with the closest location from the current truck location
    # The parameter packages is used to pass in distinct cargo lists (priority, cargo, delayed)
    # This is the core of the Greedy Algorithm - always searches for the next most optimal path
    def next_closest(self, location, packages):
        next = packages[0]
        min_distance = self.routes.distance_between(location, packages[0].address)
        for p in packages:
            p_distance = self.routes.distance_between(location, p.address)
            if p_distance < min_distance:
                min_distance = p_distance
                next = p
        return next

    # Return a string representation of condensed truck status
    def get_stats(self):
        print("%s | Embarked: %s | Location: %s | Mileage: %f | Packages Held: %s | Delivered: "
              % (self.name, self.time_at_miles(self.embark_mileage).strftime("%H:%M"),
                 self.location, self.mileage, len(self.cargo) + len(self.priority_cargo)), len(self.delivered))

    # Print expanded truck status
    def print(self):
        # print condensed truck status
        self.get_stats()
        # print packages on truck
        for p in self.delivered:
            print(p)
        print()
