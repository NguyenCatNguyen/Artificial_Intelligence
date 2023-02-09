## Problem Set 3

### Problem 3.1 [15 points] 
- Give a complete problem formulation for each of the following scenarios.  In each case, choose a formulation that is precise enough to be implemented.

a. Using only four colors, you have to color a plannar map in such a way that no two adjacent regions have the same color.
```
Problem formulation: Four Color Map Coloring
- States: 
    - Undirected graph G = (R, A)
        - R is the set of regions.
        - A is the assignment of colors to regions. 
    - Number of color k = 4
- Initial state: 
    - (R,A) where A is an empty assignments of colors to regions.
- Actions:
    - An action is defined as a color assignment to a region. 
    - The action is applied to the state (R,A) by updating the color assignment for a region
- Transition model:
    - The transition model takes the current state (R,A) and an action ( color assignment to a region) 
    as inputs and return a new state (R,A') where A' is the update color assignment to regions
- Goal states: Achive a state (R,A) where all regions have been assigned a color.
- Action cost: 
    - The cost of an action is 1, as each color assignment incurs a cost of 1.
    - The total cost is the number of actions taken to reach the goal state.
```

d. You have three jugs, measuring 12 gallons, 8 gallons, and 3 gallons, and a water faucet. you can fill the jugs up or empty them out from one to another or onto the ground. You need to measure out exactly one gallon
```
Problem formulation: Water Jug Problem
- States: 
    - Define the state as a tuple(J1,J2,J3), represent how 
    much water in each jugs.
- Initial state:
    - The initial state is (0,0,0), start at where all jugs are empty.
- Action:
    - Fill, Empty, and pouring water from one jugs to another. 
- Transition model:
    - Transition model take the current state and an action inputs then return a new state (J1', J2', J3') where
    J1', J2' and J3' represent the new volumes of water in each jug after the action is taken.
- Goal states: The goal is meet when exactly 1 gallon of water is measured in one of the jugs.
- Action cost:
    - The cost of an action is 1, as each color assignment incurs a cost of 1.
    - The total cost is the number of actions taken to reach the goal state.



```


### Problem 3.2[15 points] Search spaces, Do the following problem:
3.15 Consider a state space where the start state is number 1 and each state k has two successor: numbers 2k and 2k + 1.

a. Draw the portion of the state space for states 1 to 15.

[![state Space](stateSpace.png)](stateSpace.png)


b. Suppose the goal state is 11. List the order in which nodes will be visited for breadth-first search, depth-limited search with limit 3, and iterative deepening search.

```
- Breadth-first search:
    => 1 2 3 4 5 6 7 8 9 10 11
- Depth-limited search with limit 3:
    - Iterative limit 0:
        => 1
    - Iterative limit 1:
        => 1 2
    - Iterative limit 2: 
        => 1 2 4
    - Iterative limit 3: 
        => 1 2 4 8
```

c. How well would bidirectional search work on this problem? What is the branching factor in each direction of the bidirectional search?

d. Does the answer to (c) suffest a refomulation of the problem that would allow you to solve the problem of getting from state 1 to a given goal state with almost no search?

e. Call the action going from k to 2k Left, and the action going to 2k + 1 Right. Can you find an algorithm that outputs the solution to this problem without any search at all?


