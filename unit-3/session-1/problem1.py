def arrange_guest_arrival_order(arrival_pattern):
    ans = []
    stack = []

    for i in range(len(arrival_pattern) + 1):
        stack.append(str(i + 1))
        
        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                ans.append(stack.pop())
        
    return ''.join(ans)

print(arrange_guest_arrival_order("IIIDDIDDD"))  
print(arrange_guest_arrival_order("DDD"))


"""
I I I D I D D D
0 1 2 3 4 5 6 7

- cur = I, 1
- cur = I, 1 2
- cur = I, 1 2 3
q = [4]
- cur = D, 1 2 3 
- cur = I, 1 2 3 5 4 
q = [6]
- cur = D
q = [6, 7]
- cur = D
"""