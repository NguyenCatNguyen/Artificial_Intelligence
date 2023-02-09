# define the grid size and initialize the grid
N, M = 4,8
grid = [[0 for j in range(M)] for i in range(N)]

# initialize start and goal positions
start = (0,2)
goal = (0,6)

# mark the obstacles in the grid
for i, j in [(2,3), (2,4),(2,5),(2,6),(1,6),(0,6)]:
    grid[i][j] = 1

# define the movements in the grid
movements = [(0,1), (0,-1), (1,0), (-1,0)]

# initialize the queue for BFS
queue = [(start[0], start[1], 0)]

# initialize the visited set
visited = set()

# perform BFS
# define the grid size and initialize the grid
N, M = 4,8
grid = [[0 for j in range(M)] for i in range(N)]

# initialize start and goal positions
start = (0,2)
goal = (0,6)

# mark the obstacles in the grid
for i, j in [(2,3), (2,4),(2,5),(2,6),(1,6),(0,6)]:
    grid[i][j] = 1

# define the movements in the grid
movements = [(0,1), (0,-1), (1,0), (-1,0)]

# initialize the queue for BFS
queue = [(start[0], start[1], 0)]

# initialize the visited set
visited = set()

# perform BFS
while queue:
    x, y, cost = queue.pop(0)
    if (x, y) == goal:
        print(f"Found a path at {goal} with cost {cost}!")
        break
    if (x, y) in visited:
        continue
    visited.add((x, y))
    for dx, dy in movements:
        newx, newy = x + dx, y + dy
        if 0 <= newx < N and 0 <= newy < M and grid[newx][newy] == 0:
            queue.append((newx, newy, cost + 1))
