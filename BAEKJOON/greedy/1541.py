# 잃어버린 괄호

# 문제

'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''

# 입력
# 첫째 줄에 식이 주어진다. 
# 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
# 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

'''
'-' 를 기준으로 나눠서 계산을 하고 마지막에 '-' 실행

'''

# 1번째 시도
# 00009-00009 예제에서 실패
'''
data = list(map(str, input().split('-')))

# 각 요소를 계산하기 위해 리스트를 순회하며 eval()을 사용
result = [eval(item) for item in data]
start = result[0]

for i in result[1:]:
    start -= i

print(start)

-> str 로 만들면 안 될 것 같음
'''



data = input().split('-')

result = []

for i in data:
    sum = 0
    data2 = i.split('+')
    for j in data2:
        sum += int(j) # 00009 같은 예제를 통과할 수 있도록 
    result.append(sum)

start = result[0]

for i in result[1:]:
    start -= i
print(start)