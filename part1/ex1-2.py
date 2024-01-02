'''
* 큰 수의 법칙

- N개의 수가 있다.

- 주어진 수를 M번 더하여 가장 큰 수를 만든다.

- 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

* 입력 조건

- 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000) 의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.

- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.

- 입력으로 주어지는 K는 항상 M보다 작거나 같다.

* 출력 조건

- 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다. 

'''

n, m ,k = map(int, input.split())

data = list(map(int, input.split()))

data.sort()

first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)