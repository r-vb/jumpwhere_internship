# using hash tables best way 
def areanagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    freq1=freq2={}
    for char in s1:
        if char not in freq1:
            freq1[char]=1
        else:
            freq1[char]+=1
    for char in s2:
        if char not in freq2:
            freq2[char]=1
        else:
            freq2[char]+=1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


# using lexicographically sorting
def areanagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

# using collections.Counter
from collections import Counter
def areanagrams(s1,s2):
    return Counter(s1) == Counter(s2)
