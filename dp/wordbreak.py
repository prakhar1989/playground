vocab = set(["a", "i", "am", "ace", "mobile", "sam", "sung", "mobile","man","mango",
             "icecream","and","go","i","like","ice","cream"])

def wordbreak(string):
    if not len(string):
        return True
    for i in range(1, len(string) + 1):
        if string[:i] in vocab and wordbreak(string[i:]):
            return True
    return False

print wordbreak("ilikesamsung")
