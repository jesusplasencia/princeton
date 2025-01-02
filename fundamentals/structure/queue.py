from typing import TypeVar, Generic;
from node import Node;

T = TypeVar("T");

class Queue (Generic[T]):
    def __init__(self):
        self.first: Node | None = None;
        self.last : Node | None = None;
        self.n    : int         = 0;

    def isEmpty(self):
        return self.n == 0;

    def size(self):
        return self.n;

    def enqueue(self, item : T):
        """
        Add item to the end of the list
        """
        newNode = Node();
        newNode.item = item;
        newNode.next = None;
        
        if (self.isEmpty()):
            self.first = self.last = newNode;
        else:
            self.last.next = newNode;
            self.last = newNode;
        self.n += 1;

    def deque(self) -> T | None:
        """
        Remove item from the beginning of the list
        """
        if (self.isEmpty()):
            return None;

        item = self.first.item;
        self.first = self.first.next;

        if self.first is None:
            self.last = None;
        
        self.n -= 1;
        return item;

if __name__ == "__main__":
    queue = Queue();
    queue.enqueue("to");
    queue.enqueue("be");
    queue.enqueue("or");
    queue.enqueue("not");
    queue.enqueue("to");
    queue.deque();
    queue.enqueue("be");
    queue.deque();
    queue.deque();
    queue.enqueue("that");
    queue.deque();
    queue.deque();
    queue.deque();
    queue.enqueue("is");

    print(queue.first);
    print(queue.last);