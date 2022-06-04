# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Solution: simply sort both strings and compare them char by char. If they are permutations of each other they will be identical when sorted.


def quicksort(a, l, r):
    if l < r:
        p = pivot(a, l, r)  # element at position p is sorted
        quicksort(a, l, p-1)
        quicksort(a, p+1, r)

def sort(a):
    quicksort(a,0,len(a)-1)
    return a


def pivot(a, l, r):
    p = a[r] #choose the pivot to be the last element of the array
    i = l
    for j in range(l,r):
        if a[j] <= p:
            aux = a[i]
            a[i] = a[j]
            a[j] = aux
            i+=1
    
    aux = a[i]
    a[i] = a[r]
    a[r] = aux
    return i


assert sort([9,1,8,2,7,3,6,4,6,5]) ==[1, 2, 3, 4, 5, 6, 6, 7, 8, 9]


# has complexity O(n log n) because of the sorting
def solution(a,b):
    sort(a)
    sort(b)
    if len(a) != len(b):
        return False
    else:
        for i in range(0,len(a)):
            if a[i] != b[i]:
                return False
    return True

assert solution([9,1,8,2,7,3,6,4,6,5], [1, 2, 3, 4, 5, 6, 6, 7, 8, 9])