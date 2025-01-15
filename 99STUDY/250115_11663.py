# 1월 15일 수요일 미션 : 백준 11663번

"""
<선분 위의 점>
첫째 줄에 점의 개수 N과 선분의 개수 M이 주어진다. (1 ≤ N, M ≤ 100,000) 둘째 줄에는 점의 좌표가 주어진다.
두 점이 같은 좌표를 가지는 경우는 없다. 셋째 줄부터 M개의 줄에는 선분의 시작점과 끝점이 주어진다.
입력으로 주어지는 모든 좌표는 1,000,000,000보다 작거나 같은 자연수이다.

입력으로 주어진 각각의 선분 마다, 선분 위에 입력으로 주어진 점이 몇 개 있는지 출력한다.
"""
import sys

n, m = map(int, sys.stdin.readline().split())
points = list(map(int, sys.stdin.readline().split()))
points.sort()  # 크기순 정렬


def binary_search_start(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if points[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def binary_search_end(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if target < points[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


for _ in range(m):
    s_n, e_n = map(int, sys.stdin.readline().split())
    result_s = binary_search_start(s_n)
    result_e = binary_search_end(e_n)
    print(result_e - result_s + 1)

'''
세번째 코드 
n, m = map(int, input().split())
points = list(map(int, input().split()))
points.sort()  # 크기순 정렬


def binary_search_start(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def binary_search_end(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


for _ in range(m):
    s_n, e_n = map(int, input().split())
    result_s = binary_search_start(points, s_n, 0, n - 1)
    result_e = binary_search_end(points, e_n, 0, n - 1)
    print(result_e - result_s + 1)
'''
'''
두번째 코드 
def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == target:
            return mid
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, m = map(int, input().split())
points = list(map(int, input().split()))

for _ in range(m):
    cnt = 0
    s_n, e_n = map(int, input().split())
    for i in points:
        result = binary_search(i, s_n, e_n)
        if result is not None:
            cnt += 1
    print(cnt)
'''
'''
첫번째 코드 
n, m = map(int, input().split())
points = list(map(int, input().split()))

for _ in range(m):
    cnt = 0
    s_n, e_n = map(int, input().split())
    for point in points:
        if s_n >= point:
            s_index = points.index(point)
    for point in sorted(points, reverse=True):
        if e_n >= point:
            e_index = points.index(point)
    cnt = e_index - s_index + 1
    print("s_index : ", s_index)
    print("e_index : ", e_index)
    print(cnt)

'''
