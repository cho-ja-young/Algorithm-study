# 행복 유치원 (13164)

# 문제

'''
행복 유치원 원장인 태양이는 어느 날 N명의 원생들을 키 순서대로 일렬로 줄 세우고, 총 K개의 조로 나누려고 한다. 
각 조에는 원생이 적어도 한 명 있어야 하며, 같은 조에 속한 원생들은 서로 인접해 있어야 한다. 조별로 인원수가 같을 필요는 없다.

이렇게 나뉘어진 조들은 각자 단체 티셔츠를 맞추려고 한다. 
조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다. 
최대한 비용을 아끼고 싶어 하는 태양이는 K개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어한다. 

태양이를 도와 최소의 비용을 구하자.
'''

# 입력
# 입력의 첫 줄에는 유치원에 있는 원생의 수를 나타내는 자연수 N(1 ≤ N ≤ 300,000)과 
# 나누려고 하는 조의 개수를 나타내는 자연수 K(1 ≤ K ≤ N)가 공백으로 구분되어 주어진다. 
# 다음 줄에는 원생들의 키를 나타내는 N개의 자연수가 공백으로 구분되어 줄 서 있는 순서대로 주어진다. 
# 태양이는 원생들을 키 순서대로 줄 세웠으므로, 왼쪽에 있는 원생이 오른쪽에 있는 원생보다 크지 않다. 
# 원생의 키는 109를 넘지 않는 자연수이다.

# 출력
# 티셔츠 만드는 비용이 최소가 되도록 K개의 조로 나누었을 때, 티셔츠 만드는 비용을 출력한다.

'''
티셔츠 만드는 비용이 최소가 된다는 것은, 키 차이가 얼마 나지 않도록 만든다는 것.
조를 묶는 두명의 유치원생을 고르는 것이 그리디 알고리즘이 사용되는 곳.

'''

# 1번째 시도
# 풀이 보고 해결, 그래도 이해가 필요함

n,k = map(int,input().split())

data = list(map(int,input().split()))

# 원생들의 키 차이를 나타내는 배열
array = []
for i in range(1, n):
    array.append(data[i] - data[i-1])

# 한 조를 줄일 때 마다 가장 최소 비용을 더해주면 됨. 즉 n - k만큼 더하면 k조가 되는 최소 비용
array.sort(reverse=True)
print(sum(array[k-1:]))

'''
array.sort()
ans = 0
for i in range(n - k):
    c = array[i]
    ans += c
print(ans)
'''