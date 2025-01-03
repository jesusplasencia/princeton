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

    def insertAtBeginning(self, incoming: T) -> None:
        if (not self.item):
            self.item = incoming;
            return;
    
        temp = Node();
        temp.item = self.item;
        temp.next = self.next;

        self.item = incoming;
        self.next = temp;

    def removeBeginning(self) -> None:
        if (not self.item): return None;
        if self.next is None:
            self.item = None;
            return
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

    def find(self, key: T = None) -> bool:
        if not key: return False;
        if not self.item: return False;

        if (self.item == key): return True;

        while self.next:
            self = self.next;
            if (self.item == key): return True;
        return False;

    def removeAfter(self, key : T = None) -> None:
        if not key: return False;
        if not self.item: return None;
        
        if (self.item == key):
            self.next = None;
            return None;
        
        while self.next:
            self = self.next;
            if self.item == key:
                self.next = None;
                break;
        return None;

    def insertAfter(self, val : T = None, key : T = None,) -> None:
        if not key or not self.item: return None;

        current = self;
        while current:
            if current.item == key:
                newNode = Node();
                newNode.item = val;
                newNode.next = current.next;
                current.next = newNode;
                return None;
            current = current.next;
        return None;
        
    def remove(self, key: T = None) -> None:
        if key is None or self.item is None: return None;
        
        dummy = Node();
        dummy.item = 0;
        dummy.next = self;

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

    def max(self) -> int:
        max = 0;
        dummy = Node();
        dummy.item = 0;
        dummy.next = self;
        while dummy.next:
            if (dummy.next.item > max):
                max = dummy.next.item;
            dummy = dummy.next;
        return max;

    def reverse(self):
        reversed = None;
        while self:
            tmp = self.next;
            newHead = Node(self.item, reversed);
            reversed = newHead;
            self = tmp;
        return reversed;


if __name__ == "__main__":
    node = Node();
    node.insertAtEnd(3);
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