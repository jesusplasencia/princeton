from typing import TypeVar, Generic;
from Node import Node;

T = TypeVar("T");

class Stack (Generic[T]):
    def __init__(self) -> None:
        """
        Initializes an empty stack.
        - `first`: Points to the top of the stack (None if the stack is empty).
        - `n`: Tracks the number of items in the stack.
        """
        self.first : Node[T] | None = None;
        self.n = 0;

    def push(self, item: T) -> None:
        """
        Pushes an item onto the stack.
        - If the stack is empty, creates a new top node.
        - If the stack is not empty, prepends the item to the top of the stack.

        Parameters:
            item (T): The item to add to the stack.
        """
        self.n += 1;
        if (self.first is None):
            self.first = Node(item, None);
        else:
            self.first = Node(item, self.first);

    def pop(self) -> T | None:
        """
        Removes and returns the item from the top of the stack.
        - Decreases the stack size by 1.
        - Returns None if the stack is empty.

        Returns:
            T | None: The item from the top of the stack, or None if the stack is empty.
        """
        if (self.n == 0): return None;
        if self.first is not None:
            tmp = self.first.item;
            self.first = self.first.next;
            self.n -= 1;
            return tmp;
        return None;

    def isEmpty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.n == 0;

    def size(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The size of the stack.
        """
        return self.n;


if __name__ == "__main__":
    stack = Stack();
    stack.push("to");
    stack.push("be");
    stack.push("or");
    stack.push("not");
    stack.push("to");
    stack.pop();
    stack.push("be");
    stack.pop();
    stack.pop();
    stack.push("that");
    stack.pop();
    stack.pop();
    stack.pop();
    stack.push("is");
    print(str(stack.first))