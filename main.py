from Location import Location
from MyHashTable import MyHashTable
from Package import Package
from Graphs import Graph, Vertex
import csv

# Loads the package data into a hashtable
def load_package_data(table):
    # open the .csv file containing the package info
    with open("WGUPS Package File.csv") as file:
        # create a dictionary reader object to iterate over each row
        reader = csv.DictReader(file)
        # iterate each row, parse the data, and create a new Package object
        for row in reader:
            package = Package(row["Package ID"],
                              row["Address"],
                              row["City"],
                              row["State"],
                              row["Zip"],
                              row["Delivery Deadline"],
                              row["Mass KILO"])
            # store the Package object in the hashtable
            table.insert(package)

# load the location data file
# returns a list of Location objects that each belong to a location
# each Location object appears in the index that corresponds to its location id
def load_location_data():
    # open the .csv file containing the location data
    with open("WGUPS Location Table.csv") as file:
        # create a list of locations to return
        locations = []
        # create a dictionary reader object to iterate over each row
        reader = csv.DictReader(file)
        # iterate each row, parse the data, and create a new Location object
        for row in reader:
            location = Location(row["Id"],
                                row["Location"],
                                row["Street"],
                                row["Zip"])
            # store the Location object in the locations list
            locations.append(location)
    return locations

# load the distance data file
# returns a dictionary of location id (key) and distances to other location id (value)
# the index of the value list represents the id of the location that the distance is of
def load_distance_data():
    # open the .csv file containing the distance data
    with open("WGUPS Distance Table.csv") as file:
        reader = csv.reader(file, delimiter=',')
        # skip the header row
        header = next(reader)
        # create a dictionary to hold id of location and list of distances
        distances = {}
        for row in reader:
            # separate the distances from the first cell and remove blanks
            distance_data = [x for x in row[1:] if x != '']
            # add to dictionary - id becomes key, distance list is value
            distances[row[0]] = distance_data
        return distances

# Main application functionality
if __name__ == '__main__':
    # create hash table and load data
    table = MyHashTable(40)
    load_package_data(table)
    # create location list and load data
    locations = load_location_data()
    # create distance dictionary and load the data
    distances = load_distance_data()
    # create a graph to map the locations
    graph = Graph()
    # add each location as a vertex to the graph
    for location in locations:
        graph.add_vertex(Vertex(location))
    # for each vertex, add an undirected edge to all vertices it connects to
    for vertex in graph.adjacency_list.keys():
        # retrieve the location id contained in the vertex
        location_id = vertex.id
        # retrieve the associated list of connections of that location id
        # will return a list such as [3.4, 5.6, ....]
        connections = distances.get(location_id)
        for idx, connection in enumerate(connections):
            idx = str(idx)
            graph.add_undirected_edge(vertex, graph.get_vertex(idx), connection)
    graph.print()
