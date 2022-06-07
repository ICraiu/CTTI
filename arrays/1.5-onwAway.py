# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.


def solution(a, b):
    diff_size = abs(len(a)-len(b))
    if diff_size > 1:
        return False

    i = j = changes = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            changes += 1
            if a[i] == b[j+1] and j < len(b):
                j += 1
            if a[i+1] == b[j]:
                i += 1
            if i < len(a)-1 and j < len(b)-1 and a[i+1] == b[j+1]:
                i += 1
                j += 1
    changes += abs(i-len(a))+abs(j-len(b))

    if changes > 1:
        return False
    return True


assert solution("pale", "bale")
assert solution("pale", "bake") == False
assert solution("pale", "ple")
assert solution("pale", "padl") == False
