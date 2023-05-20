# Shows keys and values separately

players = {"Carlos": 10,
           "Javier": 12,
           "Marc": 16}

print(players.items()) # dict_items([('Carlos', 10), ('Javier', 12), ('Marc', 16)])
print(list(players.items())) # [('Carlos', 10), ('Javier', 12), ('Marc', 16)]