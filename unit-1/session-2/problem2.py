def reverse_list(lst):
    p1 = 0
    p2 = len(lst)-1
    while (p2 > p1):
        temp = lst[p1]
        lst[p1] = lst[p2]
        lst[p2] = temp
        p1 += 1
        p2 -= 1
    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))