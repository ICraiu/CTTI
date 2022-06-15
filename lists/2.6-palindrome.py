# Palindrome: Implement a function to check if a linked list is a palindrome.

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


def reverse(node):
    prev = None
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    return prev


def size(node):
    count = 0
    while node:
        count += 1
        node = node.next

    return count


def findMiddle(node):
    l = size(node)
    for i in range(0, int(l/2)):
        node = node.next
    if l % 2 == 0:
        return node
    else:
        return node.next


def solution(node):
    m = findMiddle(node)
    m = reverse(m)

    while m:
        if node.value != m.value:
            return False
        else:
            node = node.next
            m = m.next
    return True


def print(node):
    result = ""
    while node:
        result += node.value
        node = node.next
    return result


l1 = List()

l1.add("a")
l1.add("b")
l1.add("b")
l1.add("a")

l2 = List()

l2.add("a")
l2.add("b")
l2.add("c")
l2.add("b")
l2.add("a")

l3 = List()

l3.add("a")
l3.add("a")
l3.add("b")
l3.add("a")

assert solution(l1.head) == True
assert solution(l2.head) == True
assert solution(l3.head) == False
