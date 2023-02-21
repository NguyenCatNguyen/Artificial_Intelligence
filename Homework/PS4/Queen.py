import random


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
            print(f"State: {solution}, Number of Solutions: {i}  \n")    
            return
    print("No solution found\n")


if __name__ == "__main__":
    print("")
    print("Test with 10 restarts and 100 evaluations per restart:")
    RRHC(10, 100)
    print("Test with 100 restarts and 1000 evaluations per restart:")
    RRHC(100, 1000)
    print("Test with 100 restarts and 10000 evaluations per restart:")
    RRHC(100, 1000)








"""
The random_state() function generates a random state (i.e., a list of 8 integers between 0 and 7).

The attacking_pairs() function returns the number of attacking pairs of queens in a state. It first 
counts the number of queens that share a row or column with at least one other queen (by counting the 
number of times each column appears in the state minus 1). It then checks for diagonal attacks by comparing 
the absolute difference in row and column between all pairs of queens. The sum of these counts is the total 
number of attacking pairs.

The hill_climb() function implements the hill-climbing algorithm. It starts with a random state and repeatedly
 generates all possible neighbor states (by changing the position of one queen), evaluates their fitness using
  the attacking_pairs() function, and selects the neighbor with the lowest fitness as the new current state. 
  If the fitness of the new current state is lower than the fitness of the previous current state, the 
  function resets the list of neighbor states and starts over with the new current state. If the list of 
  neighbor states is empty, the function terminates. The function returns a tuple of three values: a boolean 
  indicating whether a solution was found (i.e., whether the fitness of the current state is 0), the best 
  state found, and the number of evaluations performed.

The rrhc() function implements the random-restart hill-climbing algorithm. It performs num_restarts random 
restarts of the hill-climbing algorithm, each with a maximum of max_evaluations evaluations. If a solution is
 found, it prints the solution (as a string of digits representing the columns of the queens) and the total
  number of evaluations performed. If no solution is found after all restarts, it prints a message indicating
   that no
"""


