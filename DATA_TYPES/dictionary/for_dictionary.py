players = {"Carlos": 10,
           "Javier": 12,
           "Marc": 16}

for player, number in players.items():
    print(player, ">>>", number)


# Returns the repetitions for each letter in form of a dictionary
letters = "asjkdbaskjhhfkjsah"
dic = {}

for i in letters:
    dic[i] = dic.get(i, 0)
    dic[i] += 1

print(dic)