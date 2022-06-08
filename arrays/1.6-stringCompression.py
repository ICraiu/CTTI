# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

#cannot append string with int so ints have to be cast to string

def solution(a):
    result = ""
    prev = a[0]
    counter = 1
    for i in range(1, len(a)):
        if a[i] == prev:
            counter +=1
        else:
            result += prev+str(counter)
            counter = 1
            prev = a[i]

    result += prev+str(counter)
    if len(result) > len(a):
        return a
    return result


assert solution("aaabbbdddeeedd") == "a3b3d3e3d2"
assert solution("abcdef") == "abcdef"
