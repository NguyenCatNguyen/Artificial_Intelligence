# Problem Set 5
---
#### Reading: R&N 5.1-7

## Problem 1: Describe all the elements of solving a game
```
Describe the state description move generators, terminal tests, utility
functions, and evaluation functions for only one of the following
stochastic games: Monopoly, Scrabble, bridge play with a given contract,
OR Texas hold'em poker.
```

- Game: Monopoly

- State description: the state of the game is the board, the players, and the money of each player.
    - The location of properties and the location of the players on the board.
    - The money and properties that each player has.
    - The player who is rolling the dice.
- Move generators:
    - Player throws a dice, and moves the number of squares that the dice shows.
    - Players then can buy properties, pay rent, and mortgage properties.
    - Draw a card from the community chest or chance, then do the action that the card says.

- Terminal tests:
    - The game ends when a player has bankrupted all the other players or when a player become a solo 
    owner of all the properties.


- Utility functions:
    - Hold posible outcomes of the game.
    - Assign a value to each outcome.
    - Winner is the player with the most value.

- Evaluation functions:
    - The evaluation function is use to evaluate the current state of the game.
    - It will consider the position of the AI player with respect to the other players.
    - Based on the calculation of the evaluation function, the AI player will decide which move to make.


## Problem 2: Minimax vs Alpha-Beta
``` 
a. Fill in the minimax values on one copy. Beneath the tree, note what
move Player 1 should make at Node A and the minimum payoff the player is
assured if they make that move.

b. Perform alpha-beta search on the second copy. Then, below the tree,
list the nodes that would not have been expanded if alpha-beta pruning
had been used (assuming nodes are expanded in LEFT-TO-RIGHT order).
``` 
![(a)[HW2.png]](HW2.png)
## Problem 3: Basic concepts of game playing 
```
a. Approximately how many possible games of tic-tac-toe are there?
b. Show the whole game tree starting from an empty board down to depth 2, taking symmetry into account.
c. Mark on your tree the evaluations of all the positions at depth 2.
d. Using the minimax algorithm, mark on your tree the backed-up values for the positions at depth 1
and 0, and use those values to choose the best starting move. 
e. Circle the nodes at depth 2 that would not be evaluated if alpha-beta pruning were applied, assuming
the nodes are generated in the optimal order for alpha-beta pruning.
```

- a. $9! = 362880$

- b. Tic-tac-toe game tree

![(b)[Partb.png]](Partb.png)

c. Evaluation of the positions at depth 2:

    - A = 1
    - B = 0
    - C = 1
    - D = -1
    - E = 0
    - F = 2
    - G = 1
    - H = -1
    - I = 0
    - J = -2
    - K = -1
    - L = 0
d.The best starting move is: in the middle of the board. The minimum payoff the player is assured if they make that move is 0.

e. The nodes that would not be evaluated if alpha-beta pruning were applied are: A, B, C, D, E, H, I, J, K, L.

## Problem 4: Min-conflicts aka 8-queen Revisited
a.
```python
"""
- Implement the min-conflicts algorithm for the 8-queens problem.
- Min-conflicts choosing the variable (column) to minimize over randomly.
"""
def minconflicts(encoding, maxEvals):
    # initialize the encoding
    for i in range(8):
        encoding[i] = int(ceil(random()*8))
    
    # initialize the number of fitness evaluations
    numEvals = 0
    
    # loop until a solution is found or the maximum number of evaluations is reached
    while numEvals<maxEvals:
        # compute the fitness of the current encoding
        E = fitness(encoding)
        numEvals += 1
    
        # if the fitness is 0, we have found a solution
        if E==0:
            return numEvals
    
        # choose a random column to minimize over
        col = int(ceil(random()*8))
    
        # find the row with the minimum number of conflicts
        minrow = 1
        minconflicts = 28
        for row in range(1,9):
            encoding[col-1] = row
        if fitness(encoding)<minconflicts:
            minconflicts = fitness(encoding)
            minrow = row
    
        # update the encoding
        encoding[col-1] = minrow
    
    # if we get here, we have not found a solution
    return -1
```

