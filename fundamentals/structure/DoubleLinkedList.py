from typing import Optional, TypeVar, Generic;
from DoubleNode import DoubleNode;

T = TypeVar("T")

class DoublyLinkedList(Generic[T]):
    def __init__(self):
        """
        Initializes an empty doubly-linked list.
        - `head`: The first node in the list.
        - `tail`: The last node in the list.
        """
        self.head: Optional[DoubleNode] = None
        self.tail: Optional[DoubleNode] = None

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.item))
            current = current.next
        return " -> ".join(result)

    def is_empty(self) -> bool:
        """Checks if the list is empty."""
        return self.head is None

    def insert_at_beginning(self: "DoublyLinkedList", item: T) -> None:
        """Inserts an item at the beginning of the list."""
        new_node = DoubleNode(item, None, self.head);
        if self.head is None:
            self.head = self.tail = new_node;
        else:
            new_node.next = self.head;
            self.head.prev = new_node;
            self.head = new_node;

    def insert_at_end(self: "DoublyLinkedList", item: T) -> None:
        """Inserts an item at the end of the list."""
        new_node = DoubleNode(item, self.tail, None)
        if self.tail is None:
            self.head = self.tail = new_node;
            self.tail.next = new_node
        else:
            self.tail.next = new_node;
            self.tail = new_node;

    def remove_from_beginning(self: "DoublyLinkedList") -> Optional[T]:
        """Removes and returns the item from the beginning of the list."""
        if self.head is None: return None
        item = self.head.item;
        self.head = self.head.next;
        if self.head is None:
            self.tail = None;
        else:
            self.head.prev = None;
        return item

    def remove_from_end(self: "DoublyLinkedList") -> Optional[T]:
        """Removes and returns the item from the end of the list."""
        if self.tail is None: return None
        item = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None;
        return item

    def insert_before(self : "DoublyLinkedList", node: "DoubleNode", item: T) -> None:
        """Inserts an item before the given node."""
        if node is None: return None;
        new_node = DoubleNode(item, node.prev, node);
        if node.prev is not None: node.prev.next = new_node
        node.prev = new_node;
        if node == self.head: self.head = new_node;

    def insert_after(self: "DoublyLinkedList", node: "DoubleNode", item: T) -> None:
        """Inserts an item after the given node."""
        if node is None: return None;
        new_node = DoubleNode(item, node, node.next);
        if node.next: node.next.prev = new_node;
        node.next = new_node;
        if node == self.tail: self.tail = new_node;

    def remove_node(self: "DoublyLinkedList", node: "DoubleNode") -> None:
        """Removes the given node from the list."""
        if node is None: return None;
        if node == self.head: self.head = node.next;
        if node == self.tail: self.tail = node.prev;
        if node.prev is not None: node.prev.next = node.next
        if node.next is not None: node.next.prev = node.prev

if __name__ == "__main__":
    dll = DoublyLinkedList[int]()

    # Insert at the beginning
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(5)

    # Insert at the end
    dll.insert_at_end(15)

    # Remove from beginning
    dll.remove_from_beginning()  # Output: 5

    # Remove from end
    dll.remove_from_end()  # Output: 15

    # Insert before and after
    node = dll.head  # Assuming head is valid
    dll.insert_after(node, 20)
    dll.insert_before(node, 2)

    # Remove a node
    dll.remove_node(node)
    print(str(dll))  # Output: 2 -> 20;