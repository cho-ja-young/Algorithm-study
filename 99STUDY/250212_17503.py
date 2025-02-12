# 2월 12일 수요일 문제 : 백준 17503번

"""
<맥주 축제>
- 문제


- 입력
첫 번째 줄에 축제가 열리는 기간 N (1 ≤ N ≤ 200,000) 과, 채워야 하는 선호도의 합 M (1 ≤ M < 231) 과, 마실 수 있는 맥주 종류의 수 K (N ≤ K ≤ 200,000) 가 주어집니다.
다음 K개의 줄에는 1번부터 K번 맥주의 선호도 vi (0 ≤ vi ≤ 10,000) 와 도수 레벨 ci (1 ≤ ci < 231) (vi, ci는 정수) 이 공백을 사이에 두고 주어집니다.
1번부터 K번 맥주의 종류는 모두 다릅니다.

- 출력
첫 번째 줄에 주어진 선호도의 합 M을 채우면서 N개의 맥주를 모두 마실 수 있는 간 레벨의 최솟값을 출력합니다.
만약 아무리 레벨을 올려도 조건을 만족시킬 수 없으면 첫 번째 줄에 "-1" 하나만 출력하고 더 이상 아무것도 출력하지 않아야 합니다.
"""

import sys
import heapq

input = sys.stdin.readline

n,m,k = map(int,input().split())

beers = [list(map(int, input().split())) for _ in range(k)]
beers = sorted(beers, key=lambda x: (x[1],x[0]))

preference = 0
pq = []

# 낮은 도수부터 먹어보면서 N을 만족하는지 확인
# 만족하지 않으면 -1 출력하고 종료
for i in beers:
    preference += i[0]
    heapq.heappush(pq, i[0])

    if len(pq) == n:
        if preference >= m:
            answer = i[1]
            break
        else:
            preference -= heapq.heappop(pq)
else:
    print(-1)
    exit()

print(answer)