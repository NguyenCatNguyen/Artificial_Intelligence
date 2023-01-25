# Problem Set 1

## Problem 1.1 Can you think of new objections arising from developments since he wrote the paper?
- Since the public of Computing Machinery and Intelligence there have been many new objections arising about 
Artificial Intelligence. One of the biggest concerns is that will one days AI would take over human jobs? 
The answer might be yes since AI technology is development more advance as time goes by. As for right now, there are many evident that AI is taking over human jobs. For example, self-driving cars, self-checkout machines, and many more.

## Problem 1.2 Are reflexes intelligent?
 - No, since reflex is a behavior that is developed as time goes by. It is a behavior that is not learned but is developed by experience. So reflex is not intelligent.

 ## Problem 1.3 "Surely computers cannot be intelligent-they can do only what their programmers tell them." Is the latter statement true, and does it imply former?
 - This statement would  be true during the time of this paper being written. But nowaday, AI is more advance and can learn  from experience to perform better. So if we consider the statement in the present time it would be false.

 ## Problem 1.4 State of the Art in AI
h. Writing an intentinally funny story.
    - Yes, there are AIs that can write funny story.
    - Example: AI Dungeon
j. Translating spoken English into spoken Swedish in real time.
    - Yes, there are AIs that can translate spoken English into spoken Swedish in real time.
    - Example: Google Translate

 ## Problem 1.5
 ```python
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
        k = random.choice(range(z+1, z+3))
        print(f"The sum of the two numbers is: {x}+{y}= {k}")

def main():
    while True:
        Add()
        print("Do you want to add another two numbers? (y/n)")
        answer = input()
        if answer == "n":
            break
main()
```
### Output
```
Enter a number: 5
Enter a number: 3
The sum of the two numbers is: 5+3= 8
Do you want to add another two numbers? (y/n)
y
Enter a number: 1
Enter a number: 2
The sum of the two numbers is: 1+2= 3
Do you want to add another two numbers? (y/n)
y
Enter a number: 4
Enter a number: 3
The sum of the two numbers is: 4+3= 8
Do you want to add another two numbers? (y/n)
n
```

## Problem 1.6
```
a. Toss a coin 32 times and record the outcome.
b. Compute the experimentally observed probability of heads over tosses 2 throught 21, inclusive (20 outcomes).
c. Compute the Markov chain transition probabilities over the first 21 tosses (viz., the first 20 transitions).
d. Repeat (a)-(c) above with a sequence verbally derived from a friend not in the class who does not know the 
underlying model you are trying to construct.
e. Using any language you wish, implement a computer program that uses the Markov chain model to predict the final ten 
transitions of each data set (throws 23-32 given the values of throws 22-31, respectively). That is, given the previous state 
(throw i), compute the next state (throw i+1) using the model, compare with the actual data, 
and tally the error function (# of wrong guesses).
```


- Tosses outcome:
```
T T T T H H H T T H T H T H T T T T H H H T H  |  H H T H T H T H H
```
