# This min heap implementation only works for the edge from /Dijkstra-Lazy/edge.py
# Maybe I'll do a generic one later, but this will do for now
# Based on my Java min heap implementation found here: https://github.com/mfrandev/Java-Data-Structures/blob/main/src/Heap/MinHeap.java

# Min heap class that orders edges by their cost
class min_heap:
    
    # Initialize the heap with a dummy pair at index 0 and length as 0
    def __init__(self):
        self.length = 0
        self.data = [(-1, -1)]


    # Add an item to the priority queue and maintain the heap property
    def offer(self, item):

        # Increase the item counter by 1
        self.length = self.length + 1

        # Add the item to the list
        self.data.append(item)

        # Maintain the heap property
        self.propagate_up()

    # Return the element at the top of the heap, i.e., the minimum element
    def peek(self):
        if self.length == 0: return None
        return self.data[1]

    # Remove the smallest element from the heap
    def poll(self):
        
        # Save the min element
        min_element = self.peek()

        # Swap the minimum element with the last in the heap
        self.swap(1, self.length)

        # Remove the minimum element
        self.data.pop()

        # Decrement the length of the list
        self.length = self.length - 1

        # Maintain the min heap property
        self.propagate_down()

        # Return the minimum element from the heap at the time the function was invoked
        return min_element

    # Return the number of elements in the heap
    def size(self):
        return self.length

    # Return a truth value of whether the heap is empty or not
    def is_empty(self):
        return self.size() == 0

    # Remove all elements from the heap (same as __init__)
    def clear(self):
        self.data = [(-1, -1)]
        self.length = 0

    # =============== Helper Functions ===============

    # Preserve the heap element by moving a small element at the bottom of the heap to its proper position
    # Called when adding an element to the heap
    def propagate_up(self):

        # Index of the value to move
        index = self.length

        # While the value being moved is not the root and its parent is larger than itself...
        while self.has_parent(index) and (self.data[self.parent_index(index)][1] - self.data[index][1]) > 0:

            # Swap the value with its parent
            self.swap(index, self.parent_index(index))

            # The value is now at the position its parent previously was
            index = self.parent_index(index)

    # Preserve the min heap element by moving a large element at the root of the heap to its proper position
    # Called when removing an element from the heap 
    def propagate_down(self):

        # Index of out of place item
        index = 1

        # Since terminal nodes are added left-to-right,
        # a node may only have a left child, but will never have only a right child
        while self.has_left_child(index):

            # Save whichever child is smaller of the left and right
            smallest = self.left_child_index(index)
            if self.has_right_child(index):

                # Ternary statement judging two nodes based on edge cost
                smallest = self.right_child_index(index) if (self.data[smallest][1] - self.data[self.right_child_index(index)][1]) > 0 else smallest

            # If the smallest child is smaller than the item to propagate down, swap them
            if self.data[index][1] - self.data[smallest][1] > 0:
                self.swap(index, smallest)

            # Otherwise min heap property is restored
            else:
                break

            # Index should move to the value of the item it was just swapped with
            index = smallest


    # Swap two elements in an array
    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp

    # The index for any node's parent in the heap
    def parent_index(self, i):
        return round(i / 2)
    
    # The index for any node's left child in the heap
    def left_child_index(self, i):
        return 2 * i
    
    # The index for any node's right child in the heap
    def right_child_index(self, i):
        return (2 * i) + 1

    # Returns boolean value if the specified node has an index
    def has_parent(self, i):
        return i > 1
    
    # Returns a boolean value if the specified node has a left child
    def has_left_child(self, i):
        return self.left_child_index(i) <= self.length

    # Returns a boolean value if the specified node has a right child
    def has_right_child(self, i):
        return self.right_child_index(i) <= self.length