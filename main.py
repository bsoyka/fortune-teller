import random, json, fortune_helper
with open("data.json") as file:
    fortune_tellers = json.load(file)
fortune_teller_number = random.choice(range(len(fortune_tellers)))
print("Fortune Teller #{}".format(fortune_teller_number + 1))
fortune_teller = fortune_tellers[fortune_teller_number]
pos_0 = fortune_teller[0]
pos_1 = fortune_teller[1]
pos_2 = fortune_teller[2]
pos = 0
print("")
for color in pos_0:
    print(color)
print("")
user_input = None
while user_input not in pos_0:
    user_input = raw_input("Choose an option above, type exactly as shown: ")
if fortune_helper.represents_int(user_input):
    amount_to_move = int(user_input)
else:
    amount_to_move = len(user_input)
for _ in range(amount_to_move):
    pos += 1
    if pos == 3:
        pos = 1
print("")
if pos == 1:
    for number in pos_1:
        print(number)
elif pos == 2:
    for number in pos_2:
        print(number)
print("")
user_input = None
if pos == 1:
    while user_input not in pos_1:
        user_input = raw_input("Choose an option above, type exactly as shown: ")
elif pos == 2:
    while user_input not in pos_2:
        user_input = raw_input("Choose an option above, type exactly as shown: ")
if fortune_helper.represents_int(user_input):
    amount_to_move = int(user_input)
else:
    amount_to_move = len(user_input)
for _ in range(amount_to_move):
    pos += 1
    if pos == 3:
        pos = 1
print("")
if pos == 1:
    for number in pos_1:
        print(number)
elif pos == 2:
    for number in pos_2:
        print(number)
print("")
user_input = None
if pos == 1:
    while user_input not in pos_1:
        user_input = raw_input("Choose an option above, type exactly as shown: ")
    print("Your fortune is:")
    print(pos_1[user_input])
elif pos == 2:
    while user_input not in pos_2:
        user_input = raw_input("Choose an option above, type exactly as shown: ")
    print("Your fortune is:")
    print(pos_2[user_input])
