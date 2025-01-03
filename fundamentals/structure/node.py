from typing import TypeVar, Generic;

T = TypeVar("T");

# Page 177 - Algorithm Book

class Node(Generic[T]):

    def __init__(self):
        self.item : T | None = None;
        self.next : Node | None = None;
    
    def __init__(self, item : T = None, next = None):
        self.item = item;
        self.next = next;
    
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

    def prepend(self, incoming: T) -> None:
        """ Add an element to the beginning of the list """
        if (not self.item):
            self.item = incoming;
            return;
    
        temp = Node();
        temp.item = self.item;
        temp.next = self.next;

        self.item = incoming;
        self.next = temp;

    def removeFirst(self) -> None:
        """ Remove the first Node in the list """
        if (not self.item): return None;
        if self.next is None:
            self.item = None;
            return
        self.item = self.next.item;
        self.next = self.next.next;

    def append(self, incoming: T) -> None:
        """ Add an element to the end of the Node """
        if (not self.item):
            self.item = incoming;
            return;
        current = self;
        while current.next:
            current = current.next;
        newNode = Node();
        newNode.item = incoming;
        current.next = newNode;

    def deleteAt (self, k: int) -> None:
        """ Delete the k-th node in the list """
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
        for _ in range (k - 2):
            # Out of Bounds
            if not current.next:
                return; 
            current = current.next;
        
        if current.next:
            current.next = current.next.next;

    def contains (self, key: T = None) -> bool:
        """ Check if the List contains a Node with the given key """
        if key is None or self.item is None: return False;

        current = self;
        while current:
            if (current.item == key): return True;
            current = current.next;
        return False;

    def removeAfter(self, key : T = None) -> None:
        """ Remove all nodes after the node with the given key """
        if key is None or self.item is None: return None;
        
        current = self;
        while current:
            if current.item == key:
                current.next = None;
                break;
            current = current.next;
        return None;

    def insertAfter(self, key : T = None, value : T = None) -> None:
        """ Insert a new node with `value` after the node with `key`. """
        if key is None or self.item is None or value is None: return None;

        current = self;
        while current:
            if current.item == key:
                newNode = Node(value, current.next);
                current.next = newNode;
                break;
            current = current.next;
        return None;
        
    def removeAll(self, key: T = None) -> None:
        """ Remove all nodes with the given key """
        if key is None or self.item is None: return None;
        
        dummy = Node(0, self);
        current = dummy;

        while current.next:
            if (current.next.item == key):
                # Remove the node by skipping it
                current.next = current.next.next;
            else:
                # Move to the next node
                current = current.next;

        # Return the new head of the list (in case the head was removed)
        return dummy.next;

    def findMax(self) -> int:
        """ Find the maxmimum value in the list """
        if self.item is None:
            return float('-inf');
    
        current = self;
        maxValue = current.item;
        while current:
            if (current.item > maxValue):
                maxValue = current.item;
            current = current.next;
        return maxValue;

    def reverse(self):
        """ Reverse the Linked List """
        reversed = None;
        current = self;

        while current:
            newHead = Node(current.item, reversed);
            reversed = newHead;
            current = current.next;
        return reversed;


if __name__ == "__main__":
    node = Node();
    node.insertAtBeginning(3);
    # node.insertAtEnd(4);
    node.removeBeginning();
    print(str(node));
    # node.insertAtEnd(8);
    # node.insertAtEnd(10);

    # print(str(node));
    # node.insertAfter(9, 8);
    # node.insertAfter(9, 9);
    # print(str(node));
    # print(node.remove(9));
    # node.insertAtEnd(20);
    # print(str(node));
    # print(node.max());
    # print(node.reverse());