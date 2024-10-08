'''
<문제> 1이 될 때까지

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택해 수행하려고 한다.
단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

    1) N에서 1을 뺀다
    2) N을 K로 나눈다

예를 들어 N이 17, K가 4라고 가정하자. 이때 1번의 과정을 한 번 수행하면 N은 16이 된다.
이후에 2번의 과정을 두 번 수행하면 N은 1이 된다. 

결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다.
이는 N을 1로 만드는 최소 횟수이다.

N과 K가 주어질 때, N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는
최소 횟수를 구하는 프로그램을 작성해라.
'''

# 아래의 방법을 사용하면, 반복문이 실행될 때 n 이 기하급수적으로 줄어들기 때문에
# 로그시간복잡도가 나올 수 있다.
# 빨리 실행되는 방식의 코드

# N, K 를 공백을 기준으로 구분해 입력받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)