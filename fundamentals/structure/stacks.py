from typing import TypeVar, Generic;
from node import Node;

T = TypeVar("T");

class Stack (Generic[T]):
    def __init__(self) -> None:
        self.first : Node[T] | None = None;
        self.n = 0;

    def push(self, item: T) -> None:
        self.n += 1;
        if (self.first is None):
            self.first = Node();
            self.first.item = item;
        else:
            self.first.insertAtBeginning(item);

    def pop(self) -> T | None:
        if (self.n == 0):
            return None;
        self.n -= 1;
        if self.first is not None:
            tmp = self.first.item;
            if self.first.next is None:
                self.first = None;
            else:
                self.first.removeFromBeginning()
            return tmp;
        return None;

    def isEmpty(self) -> bool:
        return self.n == 0;

    def size(self) -> int:
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
    print(repr(stack.first))