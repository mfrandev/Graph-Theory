import math

def bellman_ford(graph, number_of_vertices, start):
    '''
        Performs the Bellman-Ford algorithm (Single Source Shortest Path) on a graph

        Parameters:
            1. graph (dictionary): List of directed edges representing the graph
            2. number_of_vertices: Number of nodes in the graph
            3. start (any): Key existing in the graph from which to begin the algorithm

        Returns shortest_distances (number array): shortest distance from the start node to every position in the graph
            Note: 
            Positive infinity means node cannot be reached from starting node
            Negative infinity means node is part of or connected to a negative cycle

    '''

    # Stores the shortest distance from the start node to each node
    shortest_distances = []

    # Fill the whole graph with positive infinity so distances will always initially decrease when
    # doing Math.max or equivalent operation
    shortest_distances.extend([math.inf for _ in range(number_of_vertices)])

    # Set initial position to distance 0
    shortest_distances[start] = 0

    # Shortest distance found after num(vertices) - 1 iterations
    for _ in range(0, number_of_vertices - 1):

        # Check every edge in the graph
        for edge in graph:

            # If a better distance than the currently saved one is found, update the saved distance
            if shortest_distances[edge.source] + edge.cost < shortest_distances[edge.destination]:
                shortest_distances[edge.destination] = shortest_distances[edge.source] + edge.cost

    # Do the algorithm again (for complexity O(2 * VE) which reduces to O(VE))
    for _ in range(0, number_of_vertices - 1):

        #Check every edge in the graph
        for edge in graph:

            # If a better distances was found, this node is part of or connected to a negative cycle
            if shortest_distances[edge.source] + edge.cost < shortest_distances[edge.destination]:

                # Denote negative cycles as negative infinity
                shortest_distances[edge.destination] = -(math.inf)

    # Return the shortest distance from start to every node
    return shortest_distances