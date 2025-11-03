import json

data = """
{
  "n": 6,
  "m": 5,
  "edges": [
    [1, 2],
    [2, 5],
    [5, 1],
    [3, 4],
    [4, 6]
  ]
}
"""

# JSON 문자열을 Python 객체로 변환
graph_data = json.loads(data)
n = graph_data["n"]
m = graph_data["m"]
edges = graph_data["edges"]

# DFS 코드
def dfs(v):
    visited[v] = True
    print('graph : ', graph)

    for nxt in graph[v]:
        print('nxt : ', nxt)

        visited_nxt = visited[nxt]
        print('visited_nxt : ', visited_nxt)

        if not visited_nxt:
            dfs(nxt)

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
