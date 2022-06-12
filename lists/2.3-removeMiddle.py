# remove an element from the middle of a singly linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        n = Node(value)

        if self.head:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n

    def search(self, value):
        p = self.head
        while p:
            if p.value == value:
                return p
            else:
                p = p.next

    def print(self):
        p = self.head
        while p:
            print(p.value, end='->')
            p = p.next


def solution(node):
    while node.next:
        p = node.next
        node.value = p.value

        if p.next:
            node = node.next
        else:
            node.next = None


linked_list = List()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(1)
linked_list.add(9)
linked_list.add(2)
linked_list.add(4)
linked_list.add(2)
linked_list.add(3)


solution(linked_list.search(4))
linked_list.print()
