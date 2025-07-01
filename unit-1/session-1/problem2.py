def final_value_after_operations(operations):
    value = 1
    for i in operations:
        if (i == 'bouncy') or (i== 'flouncy'):
            value += 1
        elif (i == 'trouncy') or (i== 'pouncy'):
            value -= 1
    
    return value
