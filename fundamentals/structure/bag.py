from typing import TypeVar, Generic;
from node import Node;

T = TypeVar("T");

class Bag(Generic[T]):
    def __init__(self):
        self.container : Node | None = None;
        self.n = 0;

    def add (self, item: T) -> None:
        if not self.container:
            new_node = Node();
            new_node.item = item;
            self.container = new_node;
            self.n = 1;
        else:
            self.n += 1;
            self.container.insertAtEnd(item);

    def isEmpty(self, ) -> bool:
        return self.n == 0;

    def size(self) -> int:
        return self.n;

    def __str__(self) -> str:
        return self.container.__str__();


if __name__ == "__main__":
    bag = Bag();
    bag.add("glasses");
    bag.add("pencil");
    bag.add("mouse");

    print(bag);
    print(bag.isEmpty());
    print(bag.size());