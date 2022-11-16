import unittest

from edge import edge
from dijkstra_lazy import dijkstra_lazy

class dijkstra_lazy_test(unittest.TestCase):

    # Basic test from https://www.youtube.com/watch?v=09_LlHjoEiY: (1:27:00)
    def test1(self):
        edges = [
            edge(0, 1, 4),
            edge(0, 2, 1),
            edge(1, 3, 1),
            edge(2, 1, 2),
            edge(2, 3, 5),
            edge(3, 4, 3)
        ]

        shortest_path_to_each_node = dijkstra_lazy(edges, 5, 0)
        expected = [0, 3, 1, 4, 7]
        self.assertListEqual(shortest_path_to_each_node, expected)
 

if __name__ == '__main__':
    unittest.main()