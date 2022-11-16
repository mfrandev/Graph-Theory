from min_heap import min_heap

import math

# Simple implementation of Dijkstra's Algorithm
# Does not use a fancy priority queue, so implementation could be improved
# by adding an indexed heap so values can be internally updated, not duplicated

def dijkstra_lazy(edges, number_of_nodes, start, end=None):
    '''
        Performs the lazy version of Dijkstra's algorithm (Single Source Shortest Path) on a graph
        Reminder that Dijkstra's algo does not work in graphs with negative cycles

        Parameters:
            1. Edges (list): List of directed edges representing the graph
            2. number_of_nodes: Number of nodes in the graph
            3. start (any): Key existing in the graph from which to begin the algorithm
            4. end (optional): Key existing in the graph at which to trigger an early stop

        Returns shortest_distances (number array): shortest distance from the start node to every position in the graph
            Note: 
            Positive infinity means node cannot be reached from starting node

    '''

    # Derive the adjacency list for the input edges
    adj_list = make_adjacency_list(edges)

    # Store the shortest distance to each node from the start in this array
    shortest_distances = []

    # Set the initial shortest distance to infinity so it will always be updated 
    shortest_distances.extend([math.inf for _ in range(number_of_nodes)])

    # Obvious no distance from start to start
    shortest_distances[start] = 0

    # Create the priority queue using my min_heap implementation
    priority_queue = min_heap()

    # Add the starting position to the queue
    priority_queue.offer((start, 0))

    # Save whether or not a node has been visited
    visited = []

    # Initially, no one has been visited
    visited.extend([False for _ in range(number_of_nodes)])

    while priority_queue.length > 0:

        # Withdraw the edge with the smallest remaining cost
        (current_destination, current_cost) = priority_queue.poll()

        # Mark the destination as true
        visited[current_destination] = True

        # If the withdrawn edge does not provide a potentially more optimal path, skip it
        if shortest_distances[current_destination] < current_cost: continue

        # If there are no outgoing edges from the current node, skip it
        if(current_destination not in adj_list): continue

        # Check each outgoing edge from the current node
        for (next_destination, next_cost) in adj_list[current_destination]:

            # If the selected node is already visited, skip it
            if(visited[next_destination] == True): continue

            # Calculate the cost going to the next node from the current path
            next_total_cost = next_cost + shortest_distances[current_destination]

            # If the calculated cost is less than the currently recorded cost
            if next_total_cost < shortest_distances[next_destination]:
                
                # Update it and add it to the queue
                shortest_distances[next_destination] = next_total_cost
                priority_queue.offer((next_destination, next_total_cost))

    # Return the solution
    return shortest_distances
            


def make_adjacency_list(edges):
    '''
        Take a list of edges and output an adjacency list representing the graph

        Parameters:
        1. edges: List of edge (from edge.py), a triple (source, destination, cost)

        Output:
        1. adj_list: Adjacency list where each key is a node, and its value is the set of outgoing edges
    '''

    # Initialize the graph
    adj_list = {}

    # Iterate over all edges
    for edge in edges:

        # If the edge is not in the graph
        if edge.source not in adj_list:

            # Add it
            adj_list[edge.source] = [(edge.destination, edge.cost)]
        else:

            # Otherwise append to the existing list
            adj_list[edge.source].append((edge.destination, edge.cost))

    # Return the graph
    return adj_list
        
