# 2월 18일 화요일 문제 : 백준 11053번

"""
<가장 긴 증가하는 부분 수열>
- 문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에
가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

- 입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

- 출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# i가 0일 때 증가하는 최대 부분 수열의 길이는 1이기 때문에, 테이블을 우선 전부 1로 초기화해줌
d = [1] * n

for i in range(1, n):  # 1부터 n - 1번 인덱스까지의 모든 i에 대하여
    for j in range(i):  # i보다 작은 j 각각에 대해
        if arr[j] < arr[i]:  # j의 원소가 i의 원소보다 작다면, 즉 부분적으로 증가한다면
            d[i] = max(d[i], d[j] + 1)  # i에서의 최적의 해를 갱신해준다.

print(max(d))  # 가장 긴 증가하는 부분 수열의 길이 출력