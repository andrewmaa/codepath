def organize_pirate_crew(group_sizes):
    dic = {}
    for id, size in enumerate(group_sizes):
        if size not in dic:
            dic[size] = [id]
        else:
            dic[size].append(id)

    print(dic)
    ans = []
    for i in dic.items():
        size = i[0]
        lst = []
        for j in dic[size]:
            if len(lst) == size:
                ans.append(lst)
                lst = []
            lst.append(j)

        

    return ans

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 