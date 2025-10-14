from collections import deque
C, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]
visited = [[False] * R for _ in range(C)]
DIR = [(0,1), (1,0), (0,-1), (-1,0)]

max_area = 0
cnt = 0 
area = 0 

q = deque()
for i in range(C):
    for j in range(R):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            q.append((i, j))
            cnt += 1
            area = 1

        while q:
            x,y = q.popleft()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < C and 0 <= ny < R and arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx, ny))
                    area += 1
        
        if area > max_area:
            max_area = area

print(cnt)
print(max_area)
