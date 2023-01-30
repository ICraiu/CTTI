#given two words w1 and w2 and a isSubstring function that checks if the first input is a substring of the second.
#determine if the second word is a rotation of the first by doing one call to isSubstring.


def isSubstring(w1: str, w2: str) -> bool:

    return w1.__contains__(w2)


assert isSubstring("abc", "bc")
assert isSubstring("abc", "a")
assert not isSubstring("abc", "ac") 


def solution(w1: str, w2: str) -> bool:
    if len(w1) != len(w2):
        return False
    length = len(w1)
    i = j = 0
    while j < length:
        if w1[i] == w2[j]:
            i+=1
        else:
            i = 0
        j+=1
    return isSubstring(w1, w2[0:length - i])


assert solution("watterbottle", "erbottlewatt")
assert not solution("wattetrbottle", "erbottlewattt")