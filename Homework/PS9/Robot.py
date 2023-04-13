# a function to generate the above automatically from a given grid
#    3  5  8  11
#    2     7  10
#    1  4  6   9

grid = [
    [3, 5, 8, 11],
    [2, 'X', 7, 10],
    [1, 4, 6, 9],
]
sinks = [10,11]

def sideways(delr, delc):
  return [(-delc, -delr), (delc, delr)]

def generateT(grid, sinks):
  Up, Left, Right, Down = 1, 2, 3, 4
  A = [Up, Left, Down, Right]
  Amoves = [(Up, -1, 0), (Left, 0,-1), (Down, 1, 0), (Right, 0, 1)]
  for a, delr, delc in Amoves:
    print(a, delr, delc, sideways(delr,delc))
  Tdict = dict()
  for s in sinks:
    for a in A:
      Tdict[s,a,s] = 1
  grid_rows = len(grid)
  grid_cols = len(grid[0])
  top_bot_border = ['X']*(grid_cols+2)
  expanded_grid = []
  expanded_grid.append(top_bot_border)
  for row in grid:
    expanded_grid.append(['X'] + row + ['X'])
  expanded_grid.append(top_bot_border)
  print(expanded_grid)
  for r in range(grid_rows):
    for c in range(grid_cols):
      s = expanded_grid[r+1][c+1]
      if s not in sinks:
        for a, delr, delc in Amoves:
          self_prob = 0
          rnew, cnew = r+1+delr, c+1+delc
          snew = expanded_grid[rnew][cnew]
          if snew == 'X':
            self_prob += 0.8
          else:
            Tdict[s,a,snew] = 0.8
          for perpr, perpc in sideways(delr, delc):
            rnew, cnew = r+1+perpr, c+1+perpc
            snew = expanded_grid[rnew][cnew]
            if snew == 'X':
              self_prob += 0.1
            else:
              Tdict[s,a,snew] = 0.1
          Tdict[s,a,s] = self_prob
  return Tdict
          
Tdict = generateT(grid, sinks)

def T(s,a,snext):
  if (s,a,snext) in Tdict:
        return Tdict[s,a,snext]
  return 0

for s in range(1,12):
  for a in range(1,5):
    cumulative = 0
    cumulative2 = 0
    for nexts in range(1,12):
      tmp=T(s,a,nexts)
      cumulative += tmp
      if tmp>0:
        print("T ( %2d, %2d, %2d ) = %.1f" % (s,a,nexts,T(s,a,nexts)))
    assert cumulative==1, (s, a, nexts, cumulative)

# Value Iteration Algorithm
def value_iteration(T, R, gamma, epsilon):
    # initialize V(s) arbitrarily
    V = dict()
    for s in range(1,12):
        V[s] = 0
    while True:
        delta = 0
        for s in range(1,12):
            v = V[s]
        V[s] = max([sum([T(s,a,snext)*(R(s,a,snext)+gamma*V[snext]) for snext in range(1,12)]) for a in range(1,5)])
        delta = max(delta, abs(v-V[s]))
        if delta < epsilon:
            break
    return V

K = value_iteration(T, lambda s,a,snext: 0, 0.9, 0.0001)
print(K)
