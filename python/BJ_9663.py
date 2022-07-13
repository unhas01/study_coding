def dfs(depth):
    global count
    if depth == n:
        count += 1
        return
    
    for i in range(n):
        if visited[i] == 0: 
            graph[depth] = i
            t = True

            for j in range(depth):   
                if abs(graph[depth] - graph[j]) == abs(depth-j):
                    t=False
                    break
            if t:
                visited[i] = 1
                dfs(depth+1)
                visited[i] = 0            

n = int(input())

graph = [0] * n
visited = [0] * n
count = 0

dfs(0)
print(count)