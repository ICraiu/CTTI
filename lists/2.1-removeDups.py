# Remove Dups: Write code to remove duplicates from an unsorted li nked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def print(self):
        n = self.head
        while n is not None:
            print(str(n.value)+" -> ")
            n = n.next

def solution(list:Node):
    n = list
    while n is not None:
        p = n
        while p is not None:
            if p.next and p.next.value == n.value:
                p.next = p.next.next
            else:
                p = p.next
        n = n.next

linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(1)
linked_list.add(2)
linked_list.add(2)
linked_list.add(2)
linked_list.add(2)
linked_list.add(3)

solution(linked_list.head)

linked_list.print()