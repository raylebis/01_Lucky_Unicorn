import random

# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter either 'Yes' or 'No'")


def instructions():
    print("*** How to Play ***")
    print()
    print("The rules of the game goes here")
    print()
    return""


def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # If the amount is too low / too high to give
            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
played_before = yes_no("Have you played the "
                           "game before? ")
if played_before == "no":
    instructions()

print("program continues")

how_much = num_check("How much would you like to play with? ",0,10)
print("You have asked to play with ${}".format(how_much))

# set balance for testing purposes
balance = how_much

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

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

print()
print("Final balance", balance)