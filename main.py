import random
import time

n = int(input("Random number between 1 and:"));
number = random.randint(1, n);
guess = int(input("Enter a number between 1 and {}: " .format(n)));
guess_count = 0;
guess_limit = 5;
out_of_guesses = False;

while guess != number and not(out_of_guesses):
    if guess_count < guess_limit:
        if guess < number:
            print("Number is Higher");
            time.sleep(1);
            guess = int(input("Enter a number between 1 and {}:" .format(n)));
            guess_count += 1;

        if guess > number:
            print("Number is Lower");
            time.sleep(1);
            guess = int(input("Enter a number between 1 and {}:".format(n)));
            guess_count += 1;

    else:
        out_of_guesses = True;

if not(out_of_guesses):
    print("You win");
else:
    print("Out of guesses.The number was {}".format(number));
