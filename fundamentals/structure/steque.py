from typing import TypeVar, Generic;
from Node import Node;

T = TypeVar("T");

class Steque (Generic[T]):
    def __init__(self):
        self.first : Node[T] | None = None;
        self.n = 0;

    def __str__(self):
        return str(self.first);

    def push(self, item: T):
        """
        Pushes an item onto the steque.
        - If the steque is empty, creates a new top node.
        - If the steqie is not empty, prepends the item to the top of the steque.

        Parameters:
            item (T): The item to add to the stack.
        """
        self.n = self.n + 1;
        if (self.first is None):
            self.first = Node(item);
        else:
            self.first = Node(item, self.first);

    def pop(self):
        """
        Removes and returns the item from the top of the steque.
        - Decreases the steque size by 1.
        - Returns None if the stack is empty.

        Returns:
            T | None: The item from the top of the steque, or None if the stack is empty.
        """
        if self.n == 0: return None;
        if self.first is not None:
            tmp = self.first.item;
            self.first = self.first.next;
            self.n -= 1;
            return tmp;
        return None;

    def enqueue(self, item : T):
        """
        Add item to the end of the steque
        """
        if self.n == 0:
            self.n = 1;
            self.first = Node(item);
        else:
            self.n = self.n + 1;
            self.first.append(item);
        return None;

if __name__ == "__main__":
    steque = Steque();
    steque.push(10);
    steque.push(8);
    popped = steque.pop();
    print('Popped: ', popped);
    steque.enqueue(12);
    print(str(steque));