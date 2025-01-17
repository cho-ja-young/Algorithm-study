# 1월 17일 금요일 미션 : 백준 2470번

"""
<두 용액>
첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하이다.
둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다.
이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다.
N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다.
출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다.
특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.
"""

import sys

n = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

start = 0
end = n-1
compare = int(2e9)

while start < end:
    add_num = liquid[start] + liquid[end]
    if abs(add_num) < compare:
        result1 = liquid[start]
        result2 = liquid[end]
        compare = abs(add_num)

    if add_num < 0:
        start += 1
    elif add_num > 0:
        end -= 1
    else:
        break

print(result1, result2)

"""
# 두번째

import sys

n = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

start = 0
end = n-1
compare = 2000000000

while start <= end:
    add_num = liquid[start] + liquid[end]
    if abs(add_num) < compare:
        result1 = liquid[start]
        result2 = liquid[end]
        compare = abs(add_num)

    if add_num < 0:
        start += 1
    elif add_num > 0:
        end -= 1
    else:
        break

print(result1, result2)

"""
"""
# 첫번째 

import sys

n = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

start = 0
end = n-1
compare = 2000000000

while start <= end:
    add_num = liquid[start] + liquid[end]
    if abs(add_num) < compare:
        result1 = liquid[start]
        result2 = liquid[n - 1]
        compare = abs(add_num)

    if add_num < 0:
        start += 1
    elif add_num == 0:
        result1 = liquid[start]
        result2 = liquid[n-1]
        break
    else:
        end -= 1

print(result1, result2)
"""