# 1월 23일 목요일 미션 : 백준 1707번

"""
<이분 그래프>
- 문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

- 입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.


- 출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

"""

import sys
sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline())


def dfs(start, group):
    visited[start] = group # 현재 노드가 어느 그룹에 속하는지 저장
    # 인접 노드를 탐색한다.
    for node in graph[start]:
        # 만약 인접 노드가 방문하지 않은 곳이라면 dfs 실행, 그룹 반대값으로 지정
        # 만약 인접 노드가 방문한 곳이라면 그 값이 현재 노드의 그룹과 같은지 다른지 확인
        # 같으면 FALSE 리턴, 다르면 pass
        if visited[node] == 0:
            result = dfs(node, -group)
            if not result:
                return False
        else:
            if visited[node] == visited[start]:
                return False
    return True


for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 노드 순서대로 확인
    for i in range(1, v + 1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    if result:
        print("YES")
    else:
        print("NO")



'''
<1>
import sys

k = int(sys.stdin.readline())

def is_bipartite(g):
    # 간선의 중심을 어떻게 찾지?고 시작 노드를 어떻게 찾지? 
    # bfs 로 개수 세었을때, 가장 많은 간선을 가지
    for i in g
    if ggg:
        return 'YES'
    else:
        return 'NO'


for _ in range(k):
    graph = []
    v, e = map(int, sys.stdin.readline().split())
    for _ in range(e):
        graph.append(list(map(int, sys.stdin.readline())))
    print(is_bipartite(graph))
'''