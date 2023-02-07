import csv
from models.Package import Package

# DATA STRUCTURE
# A MyHashTable stores Packages at the hub by package id
# Packages are transferred from this data structure to the trucks for delivery
# Designed for 1-to-1 mapping with no collisions based upon the initial capacity provided (ex. 40 packages)
class MyHashTable:
    def __init__(self, initial_capacity):
        # initialize table
        self.table = []
        # add n buckets (n = initial_capacity)
        for i in range(initial_capacity):
            self.table.append([])

    # Loads the package data from .csv into the hashtable
    # Time Complexity: O(n) - it is O(1) for accessing .csv, O(n) for n rows/packages to read, and O(1) for inserting
    # Space Complexity: O(n) - for n rows/packages in the .csv
    def load_package_data(self):
        # open the .csv file containing the package info
        with open("static/WGUPS Package File.csv") as file:
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

    # Apply hash to the passed item and return the bucket
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_bucket(self, item):
        bucket = hash(item-1) % len(self.table)
        # retrieve bucket
        return self.table[bucket]

    # Insert an item into the hash table
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert(self, item):
        # get bucket
        bucket = self.get_bucket(item.id)
        # insert item into bucket
        bucket.append(item)

    # Search for item by specifying the key (Package id)
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def search(self, key):
        # get bucket
        bucket = self.get_bucket(key)
        # return bucket contents if exists
        if bucket:
            return bucket[0]
        else:
            return None

    # remove an item with matching key
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def remove(self, key):
        # get bucket
        bucket = self.get_bucket(key)
        return bucket.pop(0)

    # return the current # of items held
    # Time Complexity: O(n) - iterates n buckets
    # Space Complexity: O(1)
    def capacity(self):
        count = 0
        for row in self.table:
            if row:
                count += 1
        return count

    # Print method to display for GUI
    def print(self):
        print("-----Packages-----")
        for row in self.table:
            for p in row:
                print(p)
        print()
