# check if a string has all unique characters
# what if you cannot use an additional data structure?


# uses O(n) time and O(n) space
def solution_with_ds(input):
    map = {}
    for i in input:
        if map.get(i):
            return False
        else:
            map[i] = True
    return True

assert solution_with_ds("abcda") == False
assert solution_with_ds("abcdefg")


# uses O(n log n) time and O(1) space
def solution_no_ds(input):
    sort(input, 0, len(input)-1)

    for i in range(0, len(input)-1):
        if input[i] == input[i+1]:
            return False

    return True


def sort(input, l, r):
    if l < r:
        m = (l+r)//2
        sort(input, l, m)
        sort(input, m+1, r)
        merge(input, l, m, r)


def merge(input, l, m, r):
    i = j = 0
    k = l
    L = input[l: m+1]
    R = input[m+1: r]

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            input[k] = L[i]
            i += 1
        else:
            input[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        input[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        input[k] = R[j]
        j += 1
        k+=1


assert solution_no_ds(list("abcdefg"))
assert solution_no_ds(list("abcdefag")) == False
assert solution_no_ds(list("abcdefbg")) == False
assert solution_no_ds(list("abcdefcg")) == False