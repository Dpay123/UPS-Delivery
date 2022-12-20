
# a collection of Vertices and edges between
# represents Locations and Distances
class Graph:
    def __init__(self):
        # initialize a dictionary to hold vertices
        self.adjacency_list = {}
        # initialize a dictionary to hold edges connecting vertices
        self.edge_weights = {}

    # adds a vertex to the graph
    def add_vertex(self, location):
        self.adjacency_list[location] = []

    # retrieve a vertex using given id
    def get_vertex_by_id(self, id):
        for vertex in self.adjacency_list.keys():
            if vertex.id == id:
                return vertex

    # retrieve a vertex using given address
    def get_vertex_by_address(self, address):
        for vertex in self.adjacency_list.keys():
            if vertex.street == address:
                return vertex

    # adds a directed edge between two vertices
    def add_directed_edge(self, from_location, to_location, distance = 1.0):
        self.edge_weights[(from_location, to_location)] = distance
        self.adjacency_list[from_location].append(to_location)

    # adds an undirected edge between two vertices
    def add_undirected_edge(self, location_a, location_b, distance = 1.0):
        self.add_directed_edge(location_a, location_b, distance)
        self.add_directed_edge(location_b, location_a, distance)

    # given two string addresses, return the distance between them
    # could be used to find the distance between the addresses of two packages

    # Accepts a list of Location objects and a dictionary of distances
    # each location is added as a vertex
    # each connection between locations is added as an edge
    def load(self, locations, distances):
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

    def distance_between(self, address_a, address_b):
        vertex_a = self.get_vertex_by_address(address_a)
        vertex_b = self.get_vertex_by_address(address_b)
        return self.edge_weights[(vertex_a, vertex_b)]

    # I used this for debugging
    # check to ensure that all vertices and edges are working properly
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
        print("Count: 729 expexted, %s counted" % count)