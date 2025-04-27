def h(CS, GS):
    count = 0
    for i in range(3):
        for j in range(3):
            if CS[i][j] != 0 and CS[i][j] != GS[i][j]:
                count += 1
    return count


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    blank_i, blank_j = find_blank(state)

    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = blank_i + i, blank_j + j
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            neighbors.append(new_state)
    return neighbors

visited=[]
def a_star(initial_state, goal_state,visited,g_x):
  visited.append(initial_state)
  neighbors=get_neighbors(initial_state)
  for n in neighbors:
    if n in visited:
      neighbors.pop(neighbors.index(n))

  for n in neighbors:
    if n==goal_state:
      print("Solution found:")
      print(n)
      return
    min=[[[0,0,0],[0,0,0],[0,0,0]],100]
    h_x=h(n,goal_state)

    f_x=g_x+h_x
    if f_x<min[1]:
      min=[n,f_x]
    print("Neighbor selected:")
    for row in n:
      print(row)
    print(f"g(x) = {g_x}, h(x) = {h_x}, f(x) = {f_x}\n")

  print("Minimum Neighbor selected:")
  for row in min[0]:
    print(row)
  print("f(x) =",f_x)

  a_star(min[0],goal_state,visited,g_x+1)

# Example
initial_state = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
# goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

a_star(initial_state, goal_state,visited,1)
