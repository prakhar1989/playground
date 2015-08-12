def naivesearch(string, patt):
    count = []
    for i in range(len(string)):
        for j in range(len(patt)):
            if string[i + j] != patt[j]:
                break
            elif j == len(patt) - 1:
                count.append(i)
    return count if count else -1


print naivesearch("hello world", "orl")
print naivesearch("ABCDASDGACABCD", "ABCD")
print naivesearch("adad", "agad")
