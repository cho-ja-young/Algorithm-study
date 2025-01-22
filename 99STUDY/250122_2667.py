# 1월 22일 수요일 미션 : 백준 2667번

"""
<단지번호붙이기>
- 문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

- 입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.


- 출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""

n = int(input())
graph = [list(map(int, input())) for i in range(n)]
count = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global num
        num += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


num = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            count.append(num)
            result += 1
            num = 0

count.sort()
print(result)

for i in count:
    print(i)

'''
<1>
def dfs(v):
    for i in (x-1, x+1, y-1, y+1):
        if visited[i] 
            dfs(i)
'''
'''
<2>
def dfs():
    visited[x] == 1
    for i in (x-1, x+1):
        if 0 <= i <= 24 and graph[i][y] == 1:
            crr_x = i
            dfs()
        else:
            for j in (y - 1, y + 1):

                if graph[][]==1 and (visited[i]==0):
                    dfs(i)
'''
'''
<3>
n = int(input())
graph = [[input()] for i in range(n)]
count = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global num
        num += 1 # 여기는 글로벌 변수로 해준다. 그래야 참조가 가능
        graph[x][y] = 0 # 탐색을 한 것은 다시 0으로 바꿔준다.
        # 어떻게 하면 한줄로 x, y를 돌 수 있을까.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


num = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            count.append(num)
            result += 1
            num = 0

count.sort()
print(result)

for i in count:
    print(i)
'''