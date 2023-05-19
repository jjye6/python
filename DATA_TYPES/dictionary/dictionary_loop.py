# .items() converts players dictionary into a list
players = {"Carlos": 10,
           "Javier": 12,
           "Marc": 16}

for player, number in players.items():
    print(player, ">>>", number) # Carlos >>> 10\Javier >>> 12\nMarc >>> 16

# Returns the repetitions for each letter in form of a dictionary
letters = "asjkdbaskjhhfkjsah"
dic = {}

for i in letters:
    dic[i] = dic.get(i, 0)
    dic[i] += 1

print(dic) # {'a': 3, 's': 3, 'j': 3, 'k': 3, 'd': 1, 'b': 1, 'h': 3, 'f': 1}