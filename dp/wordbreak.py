"""
Problem - http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/
"""

vocab = set(["a", "i", "am", "ace", "mobile", "sam", "sung", "mobile","man","mango",
             "icecream","and","go","i","like","ice","cream"])

# this is the recursive version
def wordbreak(string):
    if not len(string):
        return True
    for i in range(1, len(string) + 1):
        if string[:i] in vocab and wordbreak(string[i:]):
            return True
    return False

# a DP based solution that uses a 1D array
# to cache intermediate solutions 
# Runs in O(N^2).
def wordbreakDP(string):
    if not len(string):
        return True
    cache = [False] * (len(string) + 1)
    cache[0] = True
    result = []
    for i in range(1, len(string) + 1):
        if not cache[i] and string[:i] in vocab:
            cache[i] = True
            result.append(string[:i])

        if cache[i]:
            for j in range(i+1, len(string) + 1):
                if not cache[j] and string[i:j] in vocab:
                    cache[j] = True
                    result.append(string[i:j])

                if j == len(string) and cache[j]:
                    return " ".join(result)
    return False

print wordbreak("ilikesamsung")
print wordbreakDP("ilikesamsung")
