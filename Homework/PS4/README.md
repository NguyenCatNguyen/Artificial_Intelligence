# Problem Set 4
## Problem 4.1 [10 points]
Specify fitness functions for use in evolving agents that

a. control an elevator.
- The calculate of a fitness function is depend on the specific objectives of the elevator control 
system. There are many criteria that need to be consider. The following formular is a simple example 
of a fitness function that consider 3 criteria:
    - average wait time
    - total ennergy used
    - total number of stops

```
    F = w1*(1/average wait time) + w2*(1/total ennergy used) + w3*(1/total number of stops)

    -  w1 is the weight of average wait time
    -  w2 is the weight of total ennergy used
    -  w3 is the weight of total number of stops
    -  w1 + w2 + w3 = 1

```

b. control stop lights on a city main street.
- The following formular is consider the following variables:
    - average wait time
    - time used to pass the intersection
    - numbers of vehicles that pass the intersection.
```
F = 1/((1/x)*Sum(yi))

    - x is number of vehicles that pass the intersection
    - yi is the time used to pass the intersection of each vehicle
```

## Problem 4.2 [10 points]
Give a precise formulation for the following as a constraint satisfaction problem (CSP):
    Class scheduling: There is a fixed number of professors and classrooms, a list of classes 
    to be offered, and a list of possible time slots for classes. Each professor has a set of 
    classes that he or she can teach.

- The following is a CSP formulation for the problem:
    - Variables: 
        - `classrooms`:
            - List of classes in each classroom
        - `professors`:
            - List of classes for each professor
        - `classes`: 
            - List of time slots for each class
    - Domains:
        - `classrooms`: have a list of possible time slots
        - `professors`: have a list of possible classes that he or she can teach
        - `classes`: have a list of possible time slots that can be scheduled
    - Constraints:
        - Each class must be scheduled in a room that is available at that time.
        - Each class must be scheduled with a professor that is available at that time and 
        can teach that class.
        - Each class must be scheduled at a time that is available for that class.
        - The timeslot of each professor must be the same as the timeslot of the class that 
        the professor is teaching.

## Problem 4.3 [20 points] 
- Solve the cryptarithmetic problem in Figure 6.2 of R&N by hand
- Used:
    - strategy of backtracking with forward checking
    - the MRV and least-constraining-value heuristics
- Record the steps and the reasoning/method behind them.
- Answer the following questions:
    - Does min-conflicts make sense for this type of problem?


## Problem 4.4 [30 points]
- Repeat the one-dimensional optimization experiment from the eHandout of Local Search lecture.
(See the bottom page 2 of the Local Search Handout for that day.) Specifically, maximize
    - F(x) = 4 + 2x  + 2 sin(20x) - 4 x^2
    - on the interval [0, 1] using fitness-proportional selection (aka roulette selection) of 
    individuals (points of the form 0.01*k, k= 0, ..., 100) and simple mutation (x-epsilon, with 
    probability 0.3; copy with probability 0.4; x + epsilon, with probability 0.3).  You may use 
    epsilon=0.01.
    - Use at least N=10 individuals in your population.  Report N and comment on your experiments
    and results.  Turn in documented code.


## Problem 4.5 [30 points]
- Consider the 8-queens Problem, solve it by using:
    - Random-restart hill-climbing 
- Should:
    - minimizing "fitness" def as the number of non-attacking pairs of queens

a. Implement the RRHC above.  Write your algorithm so that it exits as soon as a solution
is found, prints the solution (as a string of digits like those depicted in Figure 4.7 of
R&N), and prints the total number of fitness evaluations required from the start of the
algorithm.

```python
import random


# Generates a random state to test the hill climbing algorithm
def random_state():
    return [random.randint(0, 7) for i in range(8)]

# Calculates the number of attacking pairs of queens in a state
def attacking_pairs(state):
    # attack is the number of attacking pairs of queens in a state
    attack = sum([state.count(state[i])-1 for i in range(8)])
    # Check is the number of queens that share a diagonal, then add to attack 
    for i in range(8):
        for j in range(i+1, 8):
            if abs(state[i]-state[j]) == abs(i-j):
                attack += 1
    return attack


def hill_climb(max_evaluations):
    evaluations = 0
    current = random_state()
    current_fitness = 28 - attacking_pairs(current)
    while evaluations < max_evaluations and current_fitness > 0:
        neighbor_states = []
        for i in range(8):
            for j in range(8):
                if current[i] != j:
                    neighbor = list(current)
                    neighbor[i] = j
                    neighbor_fitness = 28 - attacking_pairs(neighbor)
                    if neighbor_fitness == current_fitness:
                        neighbor_states.append(neighbor)
                    elif neighbor_fitness < current_fitness:
                        current = neighbor
                        current_fitness = neighbor_fitness
                        neighbor_states = []
                        break
        evaluations += len(neighbor_states)
        # If there are no neighbor states with a lower fitness, terminate
        if neighbor_states: 
            current = random.choice(neighbor_states)
            current_fitness = 28 - attacking_pairs(current)
    return (current_fitness == 0, current, evaluations)

def RRHC(num_restarts, max_evaluations):
    evaluation = 0
    for i in range(num_restarts):
        found, solution, evals = hill_climb(max_evaluations - evaluation)
        evaluation += evals
        if found:
            print(f"State: {solution}, Number of Solutions: {i} ")    
            return
    print("No solution found")

```

Output:
```
Test with 10 restarts and 100 evaluations per restart:
No solution found

Test with 100 restarts and 1000 evaluations per restart:
State: [2, 4, 4, 4, 2, 4, 2, 4], Number of Solutions: 81  

Test with 100 restarts and 10000 evaluations per restart:
State: [0, 1, 2, 3, 4, 5, 6, 7], Number of Solutions: 11  



Test with 10 restarts and 100 evaluations per restart:
No solution found

Test with 100 restarts and 1000 evaluations per restart:
State: [0, 1, 2, 3, 4, 5, 6, 7], Number of Solutions: 17  

Test with 100 restarts and 10000 evaluations per restart:
State: [3, 3, 3, 3, 0, 3, 0, 0], Number of Solutions: 13  


Test with 10 restarts and 100 evaluations per restart:
No solution found
Test with 100 restarts and 1000 evaluations per restart:
State: [3, 3, 0, 3, 0, 3, 3, 0], Number of Solutions: 4  

Test with 100 restarts and 10000 evaluations per restart:
State: [1, 2, 1, 0, 1, 1, 1, 0], Number of Solutions: 27  

```
- The output show that the algorithm is able to find a solution in a reasonable amount of time. But it is not guaranteed to find a solution. The number of restarts and the number of evaluations per restart are important parameters to consider when using this algorithm.













