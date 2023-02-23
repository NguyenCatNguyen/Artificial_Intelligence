import random
import copy
def min_conflicts(n, iter_max):
    queens = [random.randint(0, n-1) for i in range(n)]
    for i in range(iter_max):
        conflicts = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and queens[i] == queens[j]:
                    conflicts[i] += 1
                if i != j and abs(queens[i] - queens[j]) == abs(i - j):
                    conflicts[i] += 1
        if sum(conflicts) == 0:
            return queens
        else:
            min_conflicts = min(conflicts)
            min_conflicts_index = [i for i in range(n) if conflicts[i] == min_conflicts]
            random_index = random.choice(min_conflicts_index)
            queens[random_index] = random.randint(0, n-1)
    return queens

def min_conflicts_cyclic(n, iter_max):
    queens = [random.randint(0, n-1) for i in range(n)]
    for i in range(iter_max):
        conflicts = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and queens[i] == queens[j]:
                    conflicts[i] += 1
                if i != j and abs(queens[i] - queens[j]) == abs(i - j):
                    conflicts[i] += 1
        if sum(conflicts) == 0:
            return queens
        else:
            min_conflicts = min(conflicts)
            min_conflicts_index = [i for i in range(n) if conflicts[i] == min_conflicts]
            random_index = min_conflicts_index[0]
            queens[random_index] = random.randint(0, n-1)
    return queens

# Test min_conflicts_cyclic
def test_min_conflicts_cyclic():
    n = 8
    iter_max = 100
    queens = min_conflicts_cyclic(n, iter_max)
    print(queens)
    print("Conflicts: ", end = "")
    print(sum([0 if i != j and queens[i] != queens[j] and abs(queens[i] - queens[j]) != abs(i - j) else 1 for i in range(n) for j in range(n)]))
    print("Iterations: ", end = "")
    print(iter_max)

# Test min_conflicts
def test_min_conflicts():
    n = 8
    iter_max = 100
    queens = min_conflicts(n, iter_max)
    print(queens)
    print("Conflicts: ", end = "")
    print(sum([0 if i != j and queens[i] != queens[j] and abs(queens[i] - queens[j]) != abs(i - j) else 1 for i in range(n) for j in range(n)]))
    print("Iterations: ", end = "")
    print(iter_max)

test_min_conflicts_cyclic()
test_min_conflicts()
