# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self) -> None:
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


def solution(node: Node, k):
    p = node
    q = p
    while k > 0 and q.next:
        q = q.next
        k -= 1
    if k>0 :
        raise Exception("k is too large")
    while q.next:
        p = p.next
        q = q.next
    return p.value


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


assert solution(linked_list.head, 2) == 4
assert solution(linked_list.head, 4) == 9

