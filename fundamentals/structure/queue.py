from typing import TypeVar, Generic;
from Node import Node;

T = TypeVar("T");

class Queue (Generic[T]):
    def __init__(self):
        self.first: Node | None = None;
        self.last : Node | None = None;
        self.n    : int         = 0;

    def isEmpty(self):
        """Returns True if the queue is empty."""
        return self.n == 0;

    def size(self):
        """Returns the number of items in the queue."""
        return self.n;

    def enqueue(self, item : T):
        """Adds an item to the end of the queue."""
        newNode = Node(item, None);
        
        if self.isEmpty():
            self.first = self.last = newNode;
        else:
            assert self.last is not None; # For type-checking assurance
            self.last.next = newNode;
            self.last = newNode;
        self.n += 1;

    def dequeue(self) -> T | None:
        """
        Removes and returns the item from the beginning of the queue.
        Raises an exception if the queue is empty.
        """
        if (self.isEmpty()): raise IndexError("Dequeue from an empty queue");

        assert self.first is not None  # For type-checking assurance
        item = self.first.item;
        self.first = self.first.next;

        if self.first is None:
            self.last = None;
        
        self.n -= 1;
        return item;

if __name__ == "__main__":
    # queue = Queue();
    # queue.enqueue("to");
    # queue.enqueue("be");
    # queue.enqueue("or");
    # queue.enqueue("not");
    # queue.enqueue("to");
    # queue.deque();
    # queue.enqueue("be");
    # queue.deque();
    # queue.deque();
    # queue.enqueue("that");
    # queue.deque();
    # queue.deque();
    # queue.deque();
    # queue.enqueue("is");

    # print(queue.first);
    # print(queue.last);
    queue = Queue[int]();
    queue.enqueue(10);
    queue.enqueue(20);
    print(queue.dequeue()); # 10 
    
    print('first:', queue.first);
    print('last :', queue.last);
    # print(queue.dequeue()); # 20
    print(queue.isEmpty());

    try:
        queue.dequeue();
    except IndexError as e:
        print(e);