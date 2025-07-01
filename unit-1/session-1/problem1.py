def linear_search(items, target):
    for i in range(len(items)):
        if (items[i] == target): 
            return i
    
    return -1


items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))