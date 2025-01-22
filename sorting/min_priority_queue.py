import heapq;

# Min-Priority Queue

# Operations
# INSERT (S, x)          -> insert element x into set S
# MINIMUM (S)            -> return minimum element from set S
# EXTRACT-MIN (S)        -> removes and returns of S with the minimum key
# DECREASE-KEY (S, x, k) -> decrease the value of the key of x by k

class MinPriorityQueue:
    def __init__(self):
        self.heap = [];

    def insert(self, x):
        """
        Insert an element x into the Min-Priority Queue.
        """
        heapq.heappush(self.heap, x);

    def minimum(self):
        """
        Return the maximum element from the Min-Priority Queue.
        """
        if not self.heap:
            raise IndexError("The priority queue is empty.");
        return self.heap[0];

    def extractMin(self):
        """
        Remove and return the element with the minimum key from the Min-Priority Queue.
        """
        if not self.heap:
            raise IndexError("The priority queue is empty.")
        return heapq.heappop(self.heap)

    def decreaseKey(self, i, k):
        """
        Decrement the value of the key at index i by k.
        """
        if i < 0 or i >= len(self.heap):
            raise IndexError("Index out of range.")

        if k > self.heap[i]:
            raise ValueError("New key is greater than current key.")

        self.heap[i] = k
        heapq.heapify(self.heap)  # Restore heap property

    def __str__(self):
        """
        Return a string representation of the heap structure as a min-heap.
        """
        return "MinPriorityQueue: [" + ", ".join(map(str, self.heap)) + "]"

if __name__ == "__main__":
    pq = MinPriorityQueue()

    # Insert elements
    pq.insert(10)
    pq.insert(20)
    pq.insert(15)
    print("Minimum:", pq.minimum())  # Output: 10

    # Print structure
    print(pq)  # Output: MinPriorityQueue: [10, 20, 15]

    # Extract min
    print("Extracted min:", pq.extractMin())  # Output: 10

    # Print structure after extraction
    print(pq)  # Output: MinPriorityQueue: [15, 20]

    # Decrease key
    pq.decreaseKey(1, 5)  # Decrease the second element to 5
    print("Minimum after decrease key:", pq.minimum())  # Output: 5
    print(pq)  # Output: MinPriorityQueue: [5, 15]