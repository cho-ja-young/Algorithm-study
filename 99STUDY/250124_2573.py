# 1월 24일 금요일 미션 : 백준 2573번

"""
<빙산>
- 문제
지구 온난화로 인하여 북극의 빙산이 녹고 있다. 빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자.
빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당되는 칸에는 0이 저장된다.
그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는
일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 따라서 그림 1의 빙산은 일년후에 그림 2와 같이 변형된다.

그림 3은 그림 1의 빙산이 2년 후에 변한 모습을 보여준다. 2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다.
따라서 그림 2의 빙산은 한 덩어리이지만, 그림 3의 빙산은 세 덩어리로 분리되어 있다.

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.


- 입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다.
N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다.
각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다.
배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.


- 출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().split()) for _ in range(n)]


# 인접 노드의 0 의 개수만큼 1년마다 줄어든다.

def bfs(x, y):
    q = deque([x, y])  # 큐 생성
    visited[x][y] = 1  # 방문 체크
    seaList = []  # 기존 노드에서 뺄 숫자 저장 리스트

    while q:
        x, y = q.popleft()
        sea = 0
        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:  # graph[nx][ny] 가 0인 경우
                    sea += 1  # 0인 인접 노드 개수 저장
                elif graph[nx][ny] and not visited[nx][ny]:  # 0이 아니고 방문한 적이 없는 경우
                    q.append((nx, ny))  # 방문 노드 큐에 추가
                    visited[nx][ny] = 1  # 방문 체크
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)  # 음수가 될 경우에 0 을 저장하도록

    return 1


ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))  # ice 에 빙산 위치 저장

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []  # ??
    group = 0  # 빙산 개수
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)  # bfs 실행
        if graph[i][j] == 0:  # bfs 실행 결과로 빙산 -> 바다 가 된 경우 체크한다.
            delList.append((i, j))  # delList 에 위치 추가
    if group > 1:  # 빙산 개수가 1이 넘으면 년 출력
        print(year)
        break  # 넘는 순간 추가 확인 불필요

    # 다 녹은 빙산은 전체 ice 에서 제거
    # 집합으로 설정해 바로 제거할 수 있도록 코드 작성
    # 위치 기준으로 저장되어 있기 때문에 다시 리스트화시키고 정렬
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

# 빙산이 다 녹을 때까지 분리되지 않은 경우
if group < 2:
    print(0)
