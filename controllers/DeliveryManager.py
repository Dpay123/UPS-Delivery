import datetime
from sqlite3 import Time

from models.Graph import Graph
from models.MyHashTable import MyHashTable
from models.Truck import Truck

# This is the class that delivers the main functionality of the program
# Upon initialization, data is read from the .CSV and loaded into the manager
# creates the package hash table and the distance graph
class DeliveryManager:
    def __init__(self):
        # create and load the inventory of packages
        self.hub = MyHashTable(40)
        self.hub.load_package_data()
        # create and load the graph with the distance/location data
        self.routes = Graph()
        # holds the mileage driven cumulatively by all trucks
        self.mileage = 0
        # create three trucks
        self.truck1 = Truck("Truck 1")
        self.truck2 = Truck("Truck 2")
        self.truck3 = Truck("Truck 3")

    # Remove a package from the hub and add to the specified truck
    def transfer_package_to_truck(self, package_id, truck):
        # remove package from hub
        p = self.hub.remove(package_id)
        # set package status
        p.status = "En Route via %s" % truck.name
        # load package to truck
        truck.load_package(p)

    # Load truck 1 and truck 2 based upon manual determination
    # NOTE: future improvement possible by developing a self-adjusting loading algorithm
    def load_first_trucks(self):
        # manual load packages to truck 1
        truck1 = [1, 2, 5, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 33, 40]
        for id in truck1:
            self.transfer_package_to_truck(id, self.truck1)

        # manual load packages to truck 2
        truck2 = [3, 4, 6, 17, 18, 24, 25, 26, 29, 30, 31, 32, 34, 36, 37, 38]
        for id in truck2:
            self.transfer_package_to_truck(id, self.truck2)

    # recall the CLOSEST truck back to the hub to minimize mileage
    # load the third truck with the remaining packages at the hub
    def load_third_truck(self):
        # identify which truck is closer and recall it
        truck1_distance_to_hub = self.routes.distance_between("4001 South 700 East", self.truck1.location)
        truck2_distance_to_hub = self.routes.distance_between("4001 South 700 East", self.truck2.location)

        if truck1_distance_to_hub < truck2_distance_to_hub:
            self.truck1.mileage += truck1_distance_to_hub
            self.truck1.location = "4001 South 700 East"
            self.mileage += self.truck1.mileage
        else:
            self.truck2.mileage += truck2_distance_to_hub
            self.truck2.location = "4001 South 700 East"
            self.mileage += self.truck2.mileage

        # load the remaining packages at hub
        for i in range(40):
            if self.hub.table[i]:
                self.transfer_package_to_truck(i+1, self.truck3)

    # return a datetime object representation of a time based upon mileage traveled
    def time_at_miles(self, miles):
        # calculate hours elapsed based upon known speed of 18mph
        travel_time = datetime.timedelta(hours=miles / 18)
        # the start time is given to us as 8am
        start_time = datetime.datetime(year=1900, month=1, day=1, hour=8, minute=0)
        return start_time + travel_time

    # Simulate total delivery of all packages
    def run(self):
        self.load_first_trucks()
        # truck 1 starts delivery at 0 offset (8am)
        self.truck1.deliver(0)
        # truck 2 starts delivery at 19.5 offset (9:05am)
        self.truck2.deliver(19.5)
        # truck 3 starts delivery after truck 1 and 2
        self.load_third_truck()
        # truck 3 starts at offset of mileage of first returned truck
        self.truck3.deliver(self.mileage)
        # total mileage of all trucks
        self.mileage = self.truck1.mileage + self.truck2.mileage + self.truck3.mileage

    # print a condensed summary of the delivery
    def print_summary(self):
        print("-----Delivery Summary-----")
        print("Miles Traveled: %f" % self.mileage)
        print("Deliveries Completed by: %s\n"
              % self.time_at_miles(self.truck3.mileage + self.truck3.embark_mileage).strftime("%H:%M"))

    # GUI option to print summary
    def status(self):
        self.print_summary()
        self.truck1.print()
        self.truck2.print()
        self.truck3.print()
        print("Simulation Completed...Returning to Main Menu")

    # Set each package status at the given time
    # Each Package can either be at the hub, loaded/en route, or delivered
    def status_with_time(self, time):
        packages = []
        # go through delivered packages of each truck and set each package status based upon the time
        for truck in [self.truck1, self.truck2, self.truck3]:
            load_time = self.time_at_miles(truck.embark_mileage)
            for package in truck.delivered:
                if time < load_time:
                    package.status = "At the Hub"
                elif time < package.delivered_at:
                    package.status = "En route via %s" % truck.name
            packages += truck.delivered

        # sort the packages based upon id for cleaner look
        packages.sort(key=lambda p: p.id)

        print("-----Package Summary at %s-----" % time.strftime("%H:%M"))
        for p in packages:
            print(p)

    # Set the given package (based upon input id) status at the given time
    def package_status(self, id, time):
        for truck in [self.truck1, self.truck2, self.truck3]:
            packages = truck.delivered
            for p in packages:
                if p.id == id:
                    load_time = self.time_at_miles(truck.embark_mileage)
                    if time < load_time:
                        p.status = "At the Hub"
                    elif time < p.delivered_at:
                        p.status = "En route via %s" % truck.name
                    print("-----Package %d Status at %s-----" % (id, time.strftime("%H:%M")))
                    print(p)
                    return
        print("Package not found")
