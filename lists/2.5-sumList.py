# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
# Output: 2 -) 1 -) 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -) 1 -) 7) + (2 -) 9 -) 5) . Thatis,617 + 295 .
# Output: 9 -) 1 -) 2. That is, 912.


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
    n = node

    while n:
        temp = n.next
        n.next = prev
        prev = n
        n = temp
    return prev


def prt(n):
    while n:
        print(n.value, end='->')
        n = n.next


def solution1(l1, l2):
    result = List()
    remainder = 0

    while l1 or l2:
        lhs = 0
        rhs = 0
        if l1:
            lhs = l1.value
            l1 = l1.next
        else:
            lhs = 0
        if l2:
            rhs = l2.value
            l2 = l2.next
        else:
            rhs = 0

        digit = rhs+lhs+remainder
        if digit > 9:
            remainder = 1
            digit = digit % 10
        else:
            remainder = 0
        result.add(digit)

    if remainder > 0:
        result.add(remainder)

    return result


def solution2(l1, l2):
    l1 = reverse(l1)
    l2 = reverse(l2)
    return reverse(solution1(l1, l2).head)


l1 = List()
l1.add(1)
l1.add(3)
l1.add(5)

l2 = List()
l2.add(2)
l2.add(4)
l2.add(6)

prt(solution2(l1.head, l2.head))
