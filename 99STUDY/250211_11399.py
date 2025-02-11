# 2월 11일 화요일 문제 : 백준 11399번

"""
<ATM>
- 문제
인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다.
사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.

줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

- 입력
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

- 출력
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

"""

import sys

n = int(sys.stdin.readline())
p1 = map(int, sys.stdin.readline().split())
p2 = sorted(p1)
total = 0
result = 0

for i in range(0, len(p2)):
    total += p2[i]
    result += total

print(result)