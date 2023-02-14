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
            print()



def num_check(question, low, high):

    valid = False
    while not valid:
        error = "Please enter a whole number between 1 and 10"
        print()

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

def instructions():

    statement_generator("How to Play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10")
    print()
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn")
    print()
    print("It costs $1 per round. Depending your prize you might win some of the money back. Heres the payouts amounts...")
    print("Unicorn: $5.00 (balance increases by $4")
    print("Horse: -$0.50 (balance decreases by $0.50")
    print("Zebra: -$0.50 (balance decreases by $0.50")
    print("Donkey: $1.00 (balance decreases by $1.00 ")
    print()
    print("Do you think you have what it takes to win this game? and take advantage?")
    print()

    return ""



def statement_generator(outcome, prize_decoration):

    sides = prize_decoration * 3

    outcome = "{} {} {}".format(sides, outcome, sides)

    top_bottom = prize_decoration * len(outcome)

    print(top_bottom)
    print(outcome)
    print(top_bottom)

    return ""



# Main routine


statement_generator("Welcome to the Lucky Unicorn Game", "*")


played_before = yes_no("Have you played the game before? ")
print()

if played_before == "no":
    instructions()

if played_before == "yes":
    statement_generator("Lets get started...", "-")

how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You have asked to play with ${}".format(how_much))

# set balance for testing purposes
balance = how_much

rounds_played = 0
print()
play_again = input("press <Enter> to play...").lower()
while play_again == "":

    # increases the number of rounds being played
    rounds_played += 1

    # prints the round number
    print()
    statement_generator("Round #{}".format(rounds_played), ".")
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5, the user gets a unicorn (adding $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4
        # if the random # is between 6 and 36, user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    else:
        # if the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    print()
    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print()
        statement_generator("Sorry you have run out of money", "#")
    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

print()
statement_generator("Results", "=")
print()
print("Final balance", "${}".format(balance))
print("Thank you for playing!")

