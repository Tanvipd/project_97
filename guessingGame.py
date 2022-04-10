import random
import math

lower = int(input("Enter the minimum value:- "))
upper = int(input("Enter the maximum value:- "))

x = random.randint(lower,upper)

print("\n\t you've only got",
round(math.log(upper - lower + 1, 2)),
"chances to guess the number! \n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")