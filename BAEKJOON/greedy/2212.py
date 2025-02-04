# 2월 4일 화요일 문제 : 백준 2212번

"""
<센서>
- 문제
집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다.
N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며, 집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다.

편의를 위해 고속도로는 평면상의 직선이라고 가정하고,각 센서의 좌표는 정수 하나로 표현된다.
각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 프로그램을 작성하시오.
단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.

- 입력
첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000), 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다.
셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다.
각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

- 출력
첫째 줄에 문제에서 설명한 최대 K개의 집중국의 수신 가능 영역의 길이의 합의 최솟값을 출력한다.
"""

import sys

n = int(sys.stdin.readline()) # 센서 수
k = int(sys.stdin.readline()) # 집중국 수
way = sorted(list(map(int, sys.stdin.readline().split())))
distance = []

if k >= n:
    print(0)
else:
    for i in range(n-1):
        d = way[i+1]-way[i]
        distance.append(d)
    result = sorted(distance, reverse=True)
    for _ in range(k-1):
        result.pop(0)
    print(sum(result))