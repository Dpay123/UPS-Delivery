import csv
from Package import Package


class MyHashTable:
    # Constructor
    def __init__(self, initial_capacity):
        # initialize table
        self.table = []
        # add n buckets (n = initial_capacity)
        for i in range(initial_capacity):
            self.table.append([])

    # Loads the package data into a hashtable
    def load_package_data(self):
        # open the .csv file containing the package info
        with open("WGUPS Package File.csv") as file:
            # create a dictionary reader object to iterate over each row
            reader = csv.DictReader(file)
            # iterate each row, parse the data, and create a new Package object
            for row in reader:
                package = Package(row["Package ID"].strip(),
                                  row["Address"].strip(),
                                  row["City"].strip(),
                                  row["State"].strip(),
                                  row["Zip"].strip(),
                                  row["Delivery Deadline"].strip(),
                                  row["Mass KILO"].strip())
                # store the Package object in the hashtable
                self.insert(package)

    def get_bucket(self, item):
        # apply hash to get the bucket
        bucket = hash(item-1) % len(self.table)
        # retrieve bucket
        return self.table[bucket]

    # Insert an item
    def insert(self, item):
        bucket = self.get_bucket(item.id)
        # insert item into bucket
        bucket.append(item)

    # Search for item by specifying the key
    def search(self, key):
        bucket = self.get_bucket(key)
        if bucket:
            return bucket[0]
        else:
            return None

    # remove an item with matching key
    def remove(self, key):
        bucket = self.get_bucket(key)
        if key in bucket:
            return bucket.pop(0)

    def capacity(self):
        count = 0
        for row in self.table:
            if row:
                count += 1
        return count

    # string rep
    def print(self):
        string = "-----Packages-----\n"
        for row in self.table:
            for p in row:
                string = string + str(p) + "\n"
        print(string)
