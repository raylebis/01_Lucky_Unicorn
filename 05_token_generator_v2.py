import random

#main routine goes here

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

# Testing loop to generate 20 tokens
for item in range(0, 20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.50

# output
print("Token: {} , Balance: ${}".format(chosen, balance))