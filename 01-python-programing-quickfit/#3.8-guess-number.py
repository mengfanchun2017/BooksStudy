# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
guessmin = 1
guessmax = 20
#怒目ber
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    guess = random.randint(guessmin, guessmax)
    print ('trying:', guess)
    if guess < secretNumber:
        print('Your guess is too low.')
        guessmin = guess + 1
    elif guess > secretNumber:
        print('Your guess is too high.')
        guessmax = guess - 1
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))