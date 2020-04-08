from collections import deque

''' Depth First Search (DFS) '''
def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for y in adj[x]:
        if not(visited[y]):
            dfs(y)

''' Breadth First Search (BFS) '''
def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if not(visited[x]):
            visited[x] = True
            print(x, end=' ')
            for y in adj[x]:
                if not visited[y]:
                    q.append(y)

n, m, start = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(start)
print()
visited = [False] * (n + 1)
bfs(start)

''' [Input Example 1]
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
