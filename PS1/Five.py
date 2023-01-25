#write a program that add two number together but some time make a mistake
#and give the wrong answer ra
import random
#Create Add fuction
def Add():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    z = x + y
    #Create a random value that pick the correct answer or the wrong answer
    ra = random.randint(0,1)
    if ra == 0:
        print(f"The sum of the two numbers is: {x}+{y}= {z}")
    else:
        k = random.choice(range(z+1, z+5))
        print(f"The sum of the two numbers is: {x}+{y}= {k}")

def main():
    while True:
        Add()
        print("Do you want to add another two numbers? (y/n)")
        answer = input()
        if answer == "n":
            break

#Part 1.6 Markov chain

def coin():
    x = 32
    while x != 0:
        flip = random.randint(0,1)
        if flip == 0:
            print("Heads")
        else:
            print("Tail")
        x -= 1

#function to calculate the future probability of heads or tails
def future():
    # Previous data set
    data = ["T T T T H H H T T H T H T H T T T T H H H T H"]
    data = data[0].split()
    # Predict the next 10 flips
    for i in range(10):
        

future()
