from collections import deque
def blueprint_approval(blueprints):
    sorted_blueprints = sorted(blueprints)
    queue = deque(blueprints)
    res = []

    i = 0

    while queue:
        if queue[0] == sorted_blueprints[i]:
            res.append(queue.popleft())
            i += 1
        else:
            queue.append(queue.popleft())

    return res


print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 