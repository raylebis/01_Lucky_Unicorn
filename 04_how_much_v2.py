# Functions go here

# Main routine goes here
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

# Main routine goes here
how_much = num_check("How much would you like to play with? ",0,10)
print("You have asked to play with ${}".format(how_much))