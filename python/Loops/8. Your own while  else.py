from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left>0:
    guess = randint(1, 10)
    if guess==random_number:
        print 'You win!'
        break
    guesses_left-=1
else:
    print "You lose."
        
    
    