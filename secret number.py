import random
print(" Hello. What is  your name?")
name = input()

print('well, ' + name +', i am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print("take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("'Your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else:
        break
if guess == secretNumber:
    print('Good job,'+ name +' ! you guessed my number in '+ str(guessesTaken) + ' guess')  

else:
    print('Nope.The number I was thinking of was '+str(secretNumber))