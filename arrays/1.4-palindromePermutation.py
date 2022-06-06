# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:Tact Coa
# Output:True (permutations: "taco cat". "atco cta". etc.)


def solution(input):
    input = input.lower()
    input = input.replace(" ", "")
    asList = list(input)
    _sort(asList, 0, len(input)-1)
    input = asList
    i = 0
    counter = 0
    m = False  # checks if there are multiple characters with odd count
    while i < len(input):
        counter = counter+1
        if i < len(input)-1 and input[i] != input[i+1]:
            if counter % 2 == 1:
                if m:
                    return False
                m = True
            counter = 0
        i = i+1
    if counter % 2 == 1:
        if m:
            return False
    return True


def _sort(input, l, r):
    if l < r:
        p = _pivot(input, l, r)
        _sort(input, l, p-1)
        _sort(input, p+1, r)


def _swap(a, i, j):
    aux = a[i]
    a[i] = a[j]
    a[j] = aux


def _pivot(a, l, r):
    i = l
    p = a[r]
    for j in range(l, r):
        if a[j] < p:
            _swap(a, i, j)
            i = i+1
    _swap(a, i, r)
    return i


assert solution("tact coa")
assert solution("ttact coA") == False
