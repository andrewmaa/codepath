def remove_dupes(items):
    p1 = 0
    p2 = 1

    while (p2 < len(items)):
        if items[p2] != items[p1]:
            p1 += 1
            items[p1] = items[p2]
        p2 += 1

    return (p1 + 1)

items = ["extract of malt", "honey", "haycorns", "extract of malt", "honey", "thistle", "thistle"]
print(remove_dupes(items))
items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))