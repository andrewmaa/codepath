from collections import Counter
def find_duplicate_chests(chests):
    freq = Counter(chests)

    res = []

    for i in freq:
        if freq[i] > 1:
            res.append(i)
    
    return res
    

def find_duplicate_chests2(chests):
    freq = {}
    ans = []

    for num in chests:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num, count in freq.items():
        if count == 2:
            ans.append(num)

    return ans

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

print(find_duplicate_chests2(chests1))
print(find_duplicate_chests2(chests2))
print(find_duplicate_chests2(chests3))