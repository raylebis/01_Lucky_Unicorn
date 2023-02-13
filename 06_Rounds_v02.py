import random
# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("press <Enter> to play...").lower()
while play_again == "":

    # increases the number of rounds being played
    rounds_played += 1

    # prints the round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5, the user gets a unicorn (adding $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        # if the random # is between 6 and 36, user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        # if the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

print()
print("Final balance", balance)