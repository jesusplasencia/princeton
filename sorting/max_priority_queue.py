import heapq;

# Max-Priority Queue

# Operations
# INSERT (S, x)          -> insert element x into set S
# MAXIMUM (S)            -> return maximum element from set S
# EXTRACT-MAX (S)        -> removes and returns of S with the largest key
# INCREASE-KEY (S, x, k) -> increment the value of the key of x by k

class MaxPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        """
        Insert an element x into the Max-Priority Queue.
        """
        heapq.heappush(self.heap, -x)  # Use negative values to simulate a max-heap
    
    def maximum(self):
        """
        Return the maximum element from the Max-Priority Queue.
        """
        if not self.heap:
            raise IndexError("The priority queue is empty.");
        return -self.heap[0];

    def extractMax(self):
        """
        Remove and return the element with the largest key from the Max-Priority Queue.
        """
        if not self.heap:
            raise IndexError("The priority queue is empty.")
        return -heapq.heappop(self.heap)

    def increaseKey(self, i, k):
        """
        Increment the value of the key at index i by k.
        """
        if i < 0 or i >= len(self.heap):
            raise IndexError("Index out of range.")

        # Remove the element, increment it, and reinsert it
        self.heap[i] -= k  # Decrease because we're storing negative values
        heapq.heapify(self.heap)  # Restore heap property

    def __str__(self):
        """
        Return a string representation of the heap structure as a max-heap.
        """
        return "MaxPriorityQueue: [" + ", ".join(map(lambda x: str(-x), self.heap)) + "]"

if __name__ == "__main__":
    pq = MaxPriorityQueue();

    # Insert elements
    pq.insert(100);
    pq.insert(950);
    pq.insert(1);

    # Print structure
    print(pq);

    # Extract max
    print("Extracted max:", pq.extractMax())  # Output: 20

    # Print structure
    print(pq);

    # Increase key
    pq.increaseKey(0, 10)  # Increase the first element by 10
    print("Maximum after increase key:", pq.maximum())  # Output: 25
    print(pq)  # Output: MaxPriorityQueue: [25, 10]
