# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string

from re import A


def solution(a, n):
    p = len(a)-1
    for i in range(n-1, -1, -1):
        if a[i] == " ":
            a[p] = "0"
            a[p-1] = "2"
            a[p-2] = "%"
            p = p-3
        else:
            a[p] = a[i]
            p = p-1

    return a


assert solution(list("Mr John Smith    "), 13) == list("Mr%20John%20Smith")