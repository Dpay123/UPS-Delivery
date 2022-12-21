from DeliveryManager import DeliveryManager
from Location import Location
from MyHashTable import MyHashTable
from Package import Package
from Graphs import Graph
import csv

from Truck import Truck

# Main application functionality
if __name__ == '__main__':

    # create a DeliveryManager
    dm = DeliveryManager()

    # implement functionality using manager
    dm.load_first_trucks()

    # print status
    dm.status()
