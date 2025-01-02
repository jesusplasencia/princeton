from typing import TypeVar, Generic;

T = TypeVar("T");

# Page 177 - Algorithm Book

class Node(Generic[T]):
    def __init__(self):
        self.item : T | None = None;
        self.next : Node | None = None;

    def __str__(self):
        strTmp = "";
        while (self.next):
            strTmp += f"{self.item} -> ";
            self = self.next;
        return strTmp + str(self.item);

    def __repr__(self):
        if (not self.next): return f"Node ({self.item}, null)";
        val, self = self.item, self.next;
        return f"Node({val}, {self.__repr__()})";

    def insertAtBeginning(self, incoming: T) -> None:
        if (not self.item):
            self.item = incoming;
            return;
    
        temp = Node();
        temp.item = self.item;
        temp.next = self.next;

        self.item = incoming;
        self.next = temp;

    def removeFromBeginning(self) -> None:
        if (not self.item): return;
        if (not self.next):
            self.item = None;
            return None;
        else:
            self.item = self.next.item;
            self.next = self.next.next;

    def insertAtEnd(self, incoming: T) -> None:
        if (not self.item):
            self.item = incoming;
            return;
        current = self;
        while current.next:
            current = current.next;
        newNode = Node();
        newNode.item = incoming;
        current.next = newNode;

    def delete(self, k: int) -> None:
        if not self.item:
            return  # Empty list, nothing to delete

        if k == 1:
            # Special case: delete the first node
            if self.next:
                self.item = self.next.item
                self.next = self.next.next
            else:
                # If it's the only node, just clear its value
                self.item = None
            return

        current = self
        i = 1
        while current.next and i < k - 1:
            current = current.next
            i += 1

        # Check if `current.next` is valid before attempting to access `current.next.next`
        if current.next and current.next.next:
            current.next = current.next.next
        elif current.next:
            # If `current.next.next` is None, it means we're at the last node to be deleted
            current.next = None

    def find(self, key: T) -> bool:
        pass;
