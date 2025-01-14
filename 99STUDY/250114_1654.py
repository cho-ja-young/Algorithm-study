# 1월 14일 월요일 미션 : 백준 1654번

"""
<랜선 자르기>
첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다.
그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 2(31승)-1보다 작거나 같은 자연수이다.

첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
"""

array = []
k, n = map(int, input().split())

for _ in range(k):
    array.append(int(input()))

# 시작점, 끝점
start = 1
end = max(array)

# 이진 탐색 수행
result = 0
while(start <= end):
    total = 0
    mid = (start + end)//2
    for i in array:
        total += (i//mid)
    # 덜 만들어진 경우
    if total < n:
        end = mid - 1
    # 같거나 더 만들어진 경우
    else:
        result = mid
        start = mid + 1

print(result)

'''
첫번째 코드

total = 0
array = []
k, n = map(int, input().split())

for _ in range(k):
    num = int(input())
    array.append(num)
    total += num

average = total//n

# 시작점, 끝점
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while(start <= end):
'''