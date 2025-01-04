from typing import Optional, TypeVar, Generic;

T = TypeVar("T");

class DoubleNode(Generic[T]):
        """
        Each node contains:
        - `item`: The data stored in the node.
        - `prev`: Reference to the previous node (None if it's the first node).
        - `next`: Reference to the next node (None if it's the last node).
        """
        def __init__(self, item: T, prev: Optional["DoubleNode"] = None, next: Optional["DoubleNode"] = None):
            self.item = item
            self.prev = prev
            self.next = next