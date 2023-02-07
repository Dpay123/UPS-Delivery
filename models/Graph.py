import csv
from models.Location import Location

# A Graph stores Locations as vertices and distances between locations as edges
# used for calculating distance between Locations
class Graph:
    def __init__(self):
        # initialize a dictionary to hold vertices
        self.adjacency_list = {}
        # initialize a dictionary to hold edges connecting vertices
        self.edge_weights = {}
        # load the data and initialize the graph upon creation of the Graph object
        self.load()

    # load the location data file
    # returns a list of Location objects that each belong to a location
    # each Location object appears in the index that corresponds to its location id
    # Time Complexity: O(n) - it is O(1) for accessing .csv, O(n) for n rows/locations to read, and O(1) for inserting
    # Space Complexity: O(n) - for n rows/locations in the .csv
    def load_location_data(self):
        # open the .csv file containing the location data
        with open("static/WGUPS Location Table.csv") as file:
            # create a list of locations to return
            locations = []
            # create a dictionary reader object to iterate over each row
            reader = csv.DictReader(file)
            # iterate each row, parse the data, and create a new Location object
            for row in reader:
                location = Location(row["Id"].strip(),
                                    row["Location"].strip(),
                                    row["Street"].strip(),
                                    row["Zip"].strip())
                # store the Location object in the locations list
                locations.append(location)
        return locations

    # load the distance data file
    # returns a dictionary of location id (key) and distances to other location id (value)
    # the index of the value list represents the id of the location that the distance is of
    # Time Complexity: O(n^2) - for n rows/packages in the .csv, each having n locations affiliated with
    # Space Complexity: O(n^2) - for n rows/packages in the .csv, each having n locations affiliated with
    def load_distance_data(self):
        # open the .csv file containing the distance data
        with open("static/WGUPS Distance Table.csv") as file:
            reader = csv.reader(file, delimiter=',')
            # skip the header row
            header = next(reader)
            # create a dictionary to hold id of location and list of distances
            distances = {}
            for row in reader:
                # separate the distances from the first cell and remove blanks
                distance_data = [x for x in row[1:] if x != '']
                # add to dictionary - id becomes key, distance list is value
                distances[int(row[0])] = distance_data
            return distances

    # Calls self methods to load list of Location objects and a dictionary of distances
    # each location is added as a vertex in the graph
    # each connection between vertices is added as an edge
    # Time Complexity: O(n^2) - for n rows/packages in the .csv, each having n locations affiliated with
    # Space Complexity: O(n^2) - for n rows/packages in the .csv, each having n locations affiliated with
    def load(self):
        locations = self.load_location_data()
        distances = self.load_distance_data()

        # add each location as a vertex to the graph
        for location in locations:
            self.add_vertex(location)

        # for each vertex, add an undirected edge to all vertices it connects to
        for vertex in self.adjacency_list.keys():
            # retrieve the associated list of connections of that location id
            # will return a list such as [3.4, 5.6, ....]
            connections = distances.get(vertex.id)
            for idx, connection in enumerate(connections):
                self.add_undirected_edge(vertex, self.get_vertex_by_id(idx), connection)

    # adds a vertex to the graph
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_vertex(self, location):
        self.adjacency_list[location] = []

    # retrieve a vertex using given id
    # Time Complexity: O(n) - iterates through n vertices
    # Space Complexity: O(1)
    def get_vertex_by_id(self, id):
        for vertex in self.adjacency_list.keys():
            if vertex.id == id:
                return vertex

    # retrieve a vertex using given address
    # Time Complexity: O(n) - iterates through n vertices
    # Space Complexity: O(1)
    def get_vertex_by_address(self, address):
        for vertex in self.adjacency_list.keys():
            if vertex.street == address:
                return vertex

    # adds a directed edge between two vertices
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_directed_edge(self, from_location, to_location, distance = 1.0):
        self.edge_weights[(from_location, to_location)] = float(distance)
        self.adjacency_list[from_location].append(to_location)

    # adds an undirected edge between two vertices
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_undirected_edge(self, location_a, location_b, distance = 1.0):
        self.add_directed_edge(location_a, location_b, distance)
        self.add_directed_edge(location_b, location_a, distance)

    # Given two string addresses, return the distance between them
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def distance_between(self, address_a, address_b):
        vertex_a = self.get_vertex_by_address(address_a)
        vertex_b = self.get_vertex_by_address(address_b)
        return self.edge_weights[(vertex_a, vertex_b)]

    # DEBUGGING - check to ensure that all vertices and edges are working properly
    # there should be 27 distinct vertices (0 - 26); each should have a corresponding location
    # there should be 729 possible edges:
        # total edges in a connected graph = 27(27-1) / 2 = 351
        # because my program records an edge in both directions, total = 351*2 = 702
        # each vertex also connects to itself (with 0 distance) so add an edge for each vertex
        # 702 + 27 = 729
    def print(self):
        print("-----Vertices-----")
        for vertex in self.adjacency_list:
            print(vertex)
        print("-----Edges-----")
        count = 0
        for k, v in self.edge_weights.items():
            count += 1
            if (v != 'O'):
                print("From vertex %s to vertex %s: %s miles" % (k[0].id, k[1].id, v))
        print("Count: 729 expected, %s counted" % count)