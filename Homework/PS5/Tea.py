# Python conversion
# MS Branicky, 2020-02-11

from random import random # random() generates a uniform random number in [0.0, 1.0]
from math import ceil

EVALS = 0

"""
// Use: Metropolis Algorithm for Maximization
//
// Source: Based on the code and explanation
// of a routine for minimization found in
// Press et al., _Numerical_Recipes_in_C_,
// Cambridge Univ. Press, 1988.  Page 351.
//
// Returns a boolean value on whether or not to
// accept a reconfiguration which leads to a 
// change dE in the objective function E.
// If dE>0, returns 1 (TRUE); if dE<=0, returns
// 1 with probablity exp(dE/T), where T is a
// temperature determined by the annealing schedule.
//
"""
def metrop(dE, T):
  r=random()
  return (dE>0) or (r<exp(dE/T))

# returns 1 if queens q1 and q2 are attacking each other, 0 o.w.
def attacking(q1col, q1row, q2col, q2row):
  if q1col==q2col:
    return 1  # same column
  if q1row==q2row:
    return 1  # same row
  coldiff=q1col-q2col
  rowdiff=q1row-q2row
  if abs(coldiff)==abs(rowdiff):
    return 1  # same diagonal
  return 0 

# evaluates the fitness of an encoding, defined as the number of
# non-attacking pairs of queens (28 - number of attacking pairs)
#
# the global variable EVALS keeps track of the number of times called
def fitness(encoding):
  global EVALS
  EVALS += 1
  E = 28
  for i in range(1,8):
    for j in range(i+1,9):
      E -= attacking(i, encoding[i-1], j, encoding[j-1])
  return E

# the following is useful in a variety of algorithms
# returns the nth successor of an encoding
def getsuccessor(init, n, succ):
  n -= 1
  quotient, remainder = divmod(n,7) 
  newrow=init[quotient]+remainder+1
  if newrow>8:
    newrow -= 8
  for j in range(8):
    if j==quotient:
      succ[j]=newrow
    else:
      succ[j]=init[j]

# copy each digit of an encoding with a prob. of error p (in place)
def mutate(enc, p):
  for i in range(1,9):
    r = random()
    if r<p:
      enc[i-1] = int(ceil(random()*8))

# copy each digit of an encoding with a prob. of error p
def mutate2(src, dest, p):
  for i in range(1,9):
    r = random();
    if (r<p):
      dest[i-1] = int(ceil(random()*8))
    else:
      dest[i-1] = src[i-1]

# produces TWO offspring via crossover at a random location on two encodings (in place)
def xover(e1, e2):
  # choose a random integer c between 1 and 7, inclusive
  c = int(ceil(random()*7));
  for i in range(c+1,9):
    e1[i-1], e2[i-1] = e2[i-1], e1[i-1]

def printenc(s, encoding):
  s = str(encoding)

# test the routines
def test():
  """
  for (double T=10000000.; T>0.000001; T/=10.) {
    int i=metrop(-1.,T);
    // int j=metrop(1.,T);
    // cout << i << ", " << j << endl;
    cout << i << endl;
  }
  """
    
  # configs from R&N, p 123, 4th ed
  enc1 = [5, 6, 7, 4, 5, 6, 7, 6]
  enc2 = [8, 3, 7, 4, 2, 5, 1, 6]

  # configs from R&N, p 127, 4th ed
  enc3 = [2, 4, 7, 4, 8, 5, 5, 2]
  enc4 = [3, 2, 7, 5, 2, 4, 1, 1]
  enc5 = [2, 4, 4, 1, 5, 1, 2, 4]
  enc6 = [3, 2, 5, 4, 3, 2, 1, 3]

  # test fitness
  for enc in [enc1, enc2, enc3, enc4, enc5, enc6]:
    print("Fitness (", str(enc), ") = ", fitness(enc))
  print()

  # test mutate
  mutate2(enc1,enc2,1.0)
  print("Random Encoding: ", str(enc2))
  mutate2(enc1,enc2,0.5)
  print("Random Encoding: ", str(enc2))
  mutate2(enc1,enc2,0.0)
  print("Random Encoding: ", str(enc2))
  mutate(enc1,1.0)
  print("Random Encoding: ", str(enc1))
  mutate(enc1,0.5)
  print("Random Encoding: ", str(enc1))
  mutate(enc1,0.0)
  print("Random Encoding: ", str(enc1))
  print()

  # test xover
  print("  Parents:", str(enc3), str(enc4))
  xover(enc3,enc4)
  print("Offspring:", str(enc3), str(enc4))
  print("  Parents:", str(enc5), str(enc6))
  xover(enc5,enc6)
  print("Offspring:", str(enc5), str(enc6))
  print()

  # test successor function
  enc7 = [1, 2, 3, 4, 5, 6, 7, 8]
  enc8 = enc7[:]
  bestE = 0
  bestSuccIndex = 0
  for i in range(1,57):
    getsuccessor(enc7, i, enc8)
    f = fitness(enc8)
    # accept better always, bu accept one that is not better with some small probability
    if f>bestE or (f==bestE and random()<0.001):  
      bestE = f
      bestSuccIndex = i
    print("Successor ( ", i, " ) = ", str(enc8), ", fitness =", fitness(enc8));
  
  getsuccessor(enc7, bestSuccIndex, enc8)
  print("  Best Successor with index ", bestSuccIndex, "=", str(enc8), "has E =", bestE)

  # generate a random successor
  RandomSuccIndex = int(ceil(random()*56)) # random int in {1, 2, ..., 56}
  getsuccessor(enc7, RandomSuccIndex, enc8)
  print("Random Successor with index ", RandomSuccIndex, "=", str(enc8), "has E =", fitness(enc8))  

"""
- Min-conflicts, choosing the variable (column) to minimize over at random
- Min-conflicts, choosing the variable to minimize in cyclic order: 1, 2, ..., 8, 1, 2, ..., 8, ..
- Implement one program encompassing both algorithms above (the difference between
them is very slight; use a #define, global variable, command-line option, or user input to
switch between them).  In each case, the algorithm should exit as soon as a solution is
found, print the solution (as a string of digits like those depicted in Figure 4.6 of R&N),
and print the total number of fitness evaluations required from the start of the
algorithm.
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

# test the minconflicts routine
def test2():
    # initialize the encoding
    encoding = [0, 0, 0, 0, 0, 0, 0, 0]
    
    # run the algorithm
    numEvals = minconflicts(encoding, 1000000)
    print("Encoding: ", str(encoding))
    print("Fitness: ", fitness(encoding))
    print("Number of fitness evaluations: ", numEvals)

test2()
