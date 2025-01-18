# 20250118 2110번

"""
<공유기 설치>
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
"""

import sys

n, c = map(int, sys.stdin.readline().split())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start+end)//2
    current = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] >= current+mid:
            count += 1
            current = array[i]
    if count >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)