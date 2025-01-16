# 1월 16일 목요일 미션 : 백준 2343번

"""
<기타 레슨>
첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다.
다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다.
각 강의의 길이는 10,000분을 넘지 않는다.

첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.
"""

import sys

n, m = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

result = 0
start = max(lectures)
end = sum(lectures)

while start <= end:
    mid = (start+end)//2
    total = 0
    count = 1
    for lecture in lectures:
        if total+lecture > mid:
            total = 0
            count += 1
        total += lecture

    if count <= m:
        result = mid
        end = mid-1
    else:
        start = mid+1

print(result)

