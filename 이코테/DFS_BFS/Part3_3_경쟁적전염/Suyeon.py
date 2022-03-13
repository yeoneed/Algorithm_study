from collections import deque

n,k = map(int, input().split()) #수 입력 

graph = [] 
graph_num = []

for i in range(n):
    graph.append(list(map(int, input().split()))) #그래프 입력 받기
    for j in range(n):
        if graph[i][j]!=0:
            graph_num.append(graph[i][j],0, i, j)

#정렬 이후에 큐로 옮기기(낮은 번호의 바이러스 먼저 증식)
graph_num.sort()
q= deque(graph_num)

target_s,target_x,target_y = map(int, input().split()) #s초, (x,y)에 존재하는 수 찾기

#상하좌우 형태 입력받기 위해
dx = [-1,1, 0,0]
dy = [0,0,-1,1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])