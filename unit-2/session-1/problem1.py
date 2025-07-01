def total_treasure(treasure_map):
    res = treasure_map.values()
    return sum(res)
    

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasure(treasure_map1)) 
print(total_treasure(treasure_map2)) 

