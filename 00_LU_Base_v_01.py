
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