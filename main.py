import random, json
def represents_int(string):
    """Used to check if str can be turned into an int
    Args:
        string - String to test
    Returns:
        True - string represents an int
        False - string does not represent an int
    """
    try:
        int(string)
        return True
    except ValueError:
        return False
fortune_tellers = [[["Red","Yellow","Green","Blue"],{"1":"You will learn a lot today.","2":"Your shoes will make you happy today.","5":"You are very talented in many ways.","6":"It's better to be alone sometimes."},{"3":"A dream you have will come true.","4":"Now is the time to learn something new.","7":"The man on top of the mountain did not fall there.","8":"Sometimes you just need to lay on the floor."}],[["Red","Yellow","Green","Blue"],{"1":"If you're happy, you're successful.","2":"You will always be surrounded by true friends.","5":"Conquer your fears or they will conquer you.","6":"Rivers need springs."},{"3":"A lifetime of happiness is in store for you.","4":"Everything happens for a reason.","7":"The world may be your oyster, but that doesn't mean you'll get it's pearl.","8":"Do not fear what you don't know."}],[["Red","Yellow","Green","Blue"],{"1":"Beware of bears bearing hugs.","2":"You will fall victim to a freak accident that gets featured on local news.","5":"Your carefully laid plans will be thwarted by a collection of crime-fighting hamsters.","6":"Santa Claus knows what you did.  You're relegated to The Naughty List."},{"3":"Your next love interest has a hobby that you detest.  Good luck with that.","4":"Before congratulating yourself for jumping 'out of the pan,' you'll soon find yourself 'in the fire.'","7":"Yes, you will fall over in front of the person you have a massive crush on.","8":"There is a pox curse waiting for you in your future."}]]
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
    try:
        user_input = raw_input("Choose an option above, type exactly as shown: ")
    except NameError:
        user_input = input("Choose an option above, type exactly as shown: ")
if represents_int(user_input):
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
        try:
            user_input = raw_input("Choose an option above, type exactly as shown: ")
        except NameError:
            user_input = input("Choose an option above, type exactly as shown: ")
elif pos == 2:
    while user_input not in pos_2:
        try:
            user_input = raw_input("Choose an option above, type exactly as shown: ")
        except NameError:
            user_input = input("Choose an option above, type exactly as shown: ")
if represents_int(user_input):
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
        try:
            user_input = raw_input("Choose an option above, type exactly as shown: ")
        except NameError:
            user_input = input("Choose an option above, type exactly as shown: ")
    print("Your fortune is:")
    print(pos_1[user_input])
elif pos == 2:
    while user_input not in pos_2:
        try:
            user_input = raw_input("Choose an option above, type exactly as shown: ")
        except NameError:
            user_input = input("Choose an option above, type exactly as shown: ")
    print("Your fortune is:")
    print(pos_2[user_input])
