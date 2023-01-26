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
#Function to flip the coin
def coin():
    x = 32
    while x != 0:
        flip = random.randint(0,1)
        if flip == 0:
            print("Heads")
        else:
            print("Tail")
        x -= 1

"""
1.6 Markov chain problem
- Compute the Markov chain transition probabilities over the first 21 tosses of a coin.
- Then use it to predict the next 10 tosses.
"""
def Markov_chain(data):
    # The probability of HH, HT, TH, TT
    HH = 0
    HT = 0
    TH = 0
    TT = 0
    # Count the number of HH, HT, TH, TT
    i = 1
    while i != 21:
        if data[i] == "H" and data[i + 1] == "H":
            HH += 1
        elif data[i] == "H" and data[i + 1] == "T":
            HT += 1
        elif data[i] == "T" and data[i + 1] == "H":
            TH += 1
        elif data[i] == "T" and data[i + 1] == "T":
            TT += 1
        i += 1
    # Calculate the probability of HH, HT, TH, TT
    HH_prob = HH / (HH + HT)
    HT_prob = HT / (HH + HT)
    TH_prob = TH / (TH + TT)
    TT_prob = TT / (TH + TT)
    # Predict the next 10 flips based on the probability of the first 21 flips
    print("The next 10 flips are: ")
    i = 1
    while i != 11:
        

    

data = ["T T T T H H H T T H T H T H T T T T H H H T H H H T H T H T H H"]
set = data[0].split()
Markov_chain(set)

