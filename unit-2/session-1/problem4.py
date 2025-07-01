from collections import Counter
def is_balanced(code):

    freq = Counter(code)

    for char in freq:
        rem = code.replace(char, "", 1) # removes the character from the string
        remfreq = Counter(rem) 
        print(rem)
        print(set(remfreq.values()))
        if len(set(remfreq.values())) == 1:
            return True
    return False
        


# def is_balanced2(code):

#     freq = {}
#     for char in freq:
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
        
#     for char in freq:
#         tempFreq = freq.copy()
#         tempFreq[char] -= 1
        
#         if tempFreq[char] == 0:
#             del tempFreq[char]

#         values = list(temp)
        
    



code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 