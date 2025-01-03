from typing import TypeVar, Generic;
from node import Node;

T = TypeVar("T");

class Steque (Generic[T]):
    def __init__(self):
        self.first : Node[T] | None = None;
        self.n = 0;

    def __str__(self):
        return str(self.first);

    def push(self, item: T):
        self.n = self.n + 1;
        if (self.first is None):
            self.first = Node(item);
        else:
            self.first.insertAtBeginning(item);

    def pop(self):
        if (self.n == 0): return None;
        self.n = self.n - 1;
        if self.first is not None:
            tmp = self.first.item;
            if self.first.next is None:
                self.first = None;
            else:
                self.first.removeBeginning();
            return tmp;
        return None;

    def enqueue(self, item : T):
        """
        Add item to the end of the list
        """
        if (self.n == 0):
            self.n = 1;
            self.first = Node(item);
        else:
            self.n = self.n + 1;
            self.first.insertAtEnd(item);
        return None;

if __name__ == "__main__":
    steque = Steque();
    steque.push(10);
    steque.push(8);
    steque.pop();
    steque.enqueue(12);
    print(str(steque));