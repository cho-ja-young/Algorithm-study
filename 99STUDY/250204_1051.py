# 2월 4일 화요일 문제 : 백준 1051번

"""
<숫자 정사각형>
- 문제
N×M 크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
이때, 정사각형은 행 또는 열에 평행해야 한다.

- 입력
첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

- 출력
첫째 줄에 정답 정사각형의 크기를 출력한다.
"""

import sys

n, m = map(int, sys.stdin.readline().split())
rectangle = []
sizes = []
side = m if n >= m else n

for _ in range(n):
    rectangle.append(sys.stdin.readline().strip())

# 정사각형의 왼쪽 위 꼭짓점 좌표 설정
for s in range(side):
    for i in range(n-s):
        for j in range(m-s):
            r1 = rectangle[i][j] # 왼위
            r2 = rectangle[i][j+s] # 오위
            r3 = rectangle[i+s][j] # 왼아래
            r4 = rectangle[i+s][j+s] # 오아래
            # 만약 r1, r2, r3, r4 의 값이 다 같다면 size = s의 제곱
            if r1 == r2 == r3 == r4:
                sizes.append((s + 1) ** 2)  # 정사각형 넓이 추가

print(max(sizes))