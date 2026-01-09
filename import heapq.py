import heapq

maze = [
    [0,0,0,1,0,0],
    [1,1,0,1,0,1],
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,0,1,0],
    [1,1,0,0,0,0]
]

start, goal = (0,0), (5,3)
moves = [(1,0),(-1,0),(0,1),(0,-1)]
h = lambda a,b: abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(maze, s, g):
    pq, came, cost = [(0, s)], {}, {s: 0}
    while pq:
        _, cur = heapq.heappop(pq)
        if cur == g:
            break
        for dx, dy in moves:
            nxt = (cur[0] + dx, cur[1] + dy)
            if 0 <= nxt[0] < len(maze) and 0 <= nxt[1] < len(maze[0]) and maze[nxt[0]][nxt[1]] == 0:
                new = cost[cur] + 1
                if nxt not in cost or new < cost[nxt]:
                    cost[nxt] = new
                    heapq.heappush(pq, (new + h(nxt, g), nxt))
                    came[nxt] = cur

    path = [g]
    while path[-1] in came:
        path.append(came[path[-1]])
    return path[::-1]

print("Shortest path from start to goal is:", astar(maze, start, goal))
