color = ["r", "g", "b"]
graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E","F"],
        "D": ["B", "C", "E"],
        "E": ["C", "D","F"],
        "F": ["C","E"]
}
assign ={
    "A": "",
    "B": "",
    "C": "",
    "D": "",
    "E": "",
    "F": ""
}
def safecheck(v,c):
  for i in graph[v]:
    if assign.get(i)==c:
      return False
  return True

def graphcolor(v):
    if assign[v] != "":
      return True
    for c in color:
      if safecheck(v,c) :
        assign[v]=c
        print(f"Assigning {c} to {v}")
        if all(graphcolor(neigh) for neigh in graph[v] if assign[neigh] == ""):
            return True
        print(f"Backtracking on {v}")
        assign[v] = ""
    return False
graphcolor(list(graph.keys())[4])

print(assign)
