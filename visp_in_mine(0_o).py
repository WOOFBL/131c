from collections import  deque
graph = {
    1:[3,5],
    2:[6,7],
    3:[8],
    4:[],
    5:[8],
    6:[]
}
start = 1
queue = deque([start])
visited = []
while queue:
    vertex = queue.popleft()
    if vertex not in visited:
        visited.append(vertex)
        queue.extend(graph[vertex])
print(visited)
