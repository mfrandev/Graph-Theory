import unittest
import math

from edge import edge
from bellman_ford import bellman_ford

# Many graph examples in this test class were taken or adapted from this video: https://www.youtube.com/watch?v=09_LlHjoEiY
# Between timestamps 1:51:07 and 2:05:23

class bellman_ford_test(unittest.TestCase):

    def test_bellman_ford_no_negative_cycles(self):
        '''
            Test that the bellman_ford implementation returns the shortest path from a starting node
            to all other nodes in a graph. 

            Note that the ordering of edges in the graph can be chosen arbitrarily, so the algorithm
            is tested on 3 different orderings of the same graph.
        '''

        # Shortest path from start to each node
        expected_ordering = [0, 4, 7, 10, 4, 6, 2]

        # Ordering 1
        graph = [
            edge(4, 5, 2),
            edge(6, 4, 2),
            edge(0, 1, 4),
            edge(3, 5, -2),
            edge(2, 4, 1),
            edge(0, 6, 2),
            edge(1, 2, 3),
            edge(2, 3, 3)
        ]
        shortest_paths = bellman_ford(graph, 7, 0)
        self.assertListEqual(shortest_paths, expected_ordering)

        # Ordering 2
        graph = [
            edge(3, 5, -2),
            edge(4, 5, 2),
            edge(6, 4, 2),
            edge(0, 1, 4),
            edge(0, 6, 2),
            edge(2, 4, 1),
            edge(1, 2, 3),
            edge(2, 3, 3)
        ]
        shortest_paths = bellman_ford(graph, 7, 0)
        self.assertListEqual(shortest_paths, expected_ordering)

        # Ordering 3
        graph = [
            edge(1, 2, 3),
            edge(0, 1, 4),
            edge(0, 6, 2),
            edge(2, 3, 3),
            edge(3, 5, -2),
            edge(2, 4, 1),
            edge(6, 4, 2),
            edge(4, 5, 2)
        ]
        shortest_paths = bellman_ford(graph, 7, 0)
        self.assertListEqual(shortest_paths, expected_ordering)
        

    def test_bellman_ford_one_self_contained_negative_cycle(self):
        '''
            Test that bellman_ford can detect a negative cycle and set all nodes and 
            reachable components affected by the cycle to a path cost of negative infinity.

            Note that the edges in this graph are the same as the previous test with the addition 
            of a self-contained negative cycle, edge(1, 1, -1).
        '''
        graph = [
            edge(3, 5, -2),
            edge(2, 4, 1),
            edge(4, 5, 2),
            edge(6, 4, 2),
            edge(0, 1, 4),
            edge(0, 6, 2),
            edge(1, 1, -1),
            edge(1, 2, 3),
            edge(2, 3, 3)
        ]
        shortest_paths = bellman_ford(graph, 7, 0)
        self.assertListEqual(shortest_paths, [0, -(math.inf), -(math.inf), -(math.inf), -(math.inf), -(math.inf), 2])

    def test_bellman_ford_starting_at_end(self):
        '''
            Test that bellman_ford only modifies the starting position if there are no outgoing edges.
        '''

        graph = [
            edge(3, 5, -2),
            edge(2, 4, 1),
            edge(4, 5, 2),
            edge(6, 4, 2),
            edge(0, 1, 4),
            edge(0, 6, 2),
            edge(1, 1, -1),
            edge(1, 2, 3),
            edge(2, 3, 3)
        ]
        shortest_paths = bellman_ford(graph, 7, 5)
        self.assertListEqual(shortest_paths, [math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf])

    def test_bellman_ford_starting_in_middle(self):
        '''
            Test that bellman_ford returns positive infinity for all edges
            that it cannot reach from the starting point.

            In this example, starting at node 2 in the graph means nodes 0, 1, and 6 are unreachable.
        '''

        graph = [
            edge(3, 5, -2),
            edge(2, 4, 1),
            edge(4, 5, 2),
            edge(6, 4, 2),
            edge(0, 1, 4),
            edge(0, 6, 2),
            edge(1, 1, -1),
            edge(1, 2, 3),
            edge(2, 3, 3)
        ]
        shortest_paths = bellman_ford(graph, 7, 2)
        self.assertListEqual(shortest_paths, [math.inf, math.inf, 0, 3, 1, 1, math.inf])

if __name__ == '__main__':
    unittest.main()