# Returns the value of a key only if it exists otherwise none or a message

players = {"Carlos": 10,
           "Javier": 12,
           "Marc": 16}

print(players.get("Carlos")) # 10
print(players.get("Matias")) # none
print(players.get("Matias", "Hello")) # Hello