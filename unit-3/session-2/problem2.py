def build_skyscrapers(floors):
    res = 0
    stack = []

    for floor in floors:
        if not stack or floor >= stack[-1]:
            stack.append(floor)
        else:
            res += 1
            stack = [floor]

    if stack:
        res += 1  

    return res

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 
