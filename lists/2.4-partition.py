# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below) . The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None


    def add(self, value):
        n = Node(value)
        if self.head:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n

    def print(self):
        n = self.head
        while n:
            print(n.value, end='->')
            n = n.next


def solution(node, part):
    while node:
        if node.value >= part:
            p = node
            while p and p.value >= part:
                p = p.next
                if p:
                    aux = node.value
                    node.value = p.value
                    p.value = aux
                else:
                    return
        node = node.next

linked_list = List()
linked_list.add(3)
linked_list.add(5)
linked_list.add(8)
linked_list.add(5)
linked_list.add(10)
linked_list.add(2)
linked_list.add(1)

solution(linked_list.head, 5)

linked_list.print()