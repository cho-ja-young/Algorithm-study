# 2월 7일 금요일 문제 : 백준 15686번

"""
<치킨배달>
- 문제
크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다.
도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다.
r과 c는 1부터 시작한다.

치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며,
각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다.
오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

- 입력
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.


- 출력
첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

"""

import sys

sys.setrecursionlimit(10 ** 8)

N, M = map(int, input().split())  # N은 격자 사이즈, M은 치킨집 개수
graph = []
house = []
chicken = []

for col in range(N):
    graph.append(list(map(int, input().split())))
    for row in range(N):
        if graph[col][row] == 1:
            house.append((col, row))

        elif graph[col][row] == 2:
            chicken.append((col, row))

arr = []
real_check = int(1e9)


def back(num, cnt):
    global real_check
    if num > len(chicken):
        return

    if cnt == M:
        result_tot = 0
        for hx, hy in house:
            min_check = int(1e9)
            for idx in arr:
                cx, cy = chicken[idx]
                min_check = min(min_check, abs(hx - cx) + abs(hy - cy))

            result_tot += min_check

        real_check = min(result_tot, real_check)
        return

    arr.append(num)
    back(num + 1, cnt + 1)
    arr.pop()
    back(num + 1, cnt)
    return real_check


print(back(0, 0))