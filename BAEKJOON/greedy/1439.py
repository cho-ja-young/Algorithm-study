# 뒤집기 (1439)

# 문제

'''
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 
뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

예를 들어 S=0001100 일 때,

1. 전체를 뒤집으면 1110011이 된다.
2. 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.

하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.
'''

# 입력
# 첫째 줄에 문자열 S가 주어진다. S의 길이는 100만보다 작다. 

# 출력
# 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력한다.

'''
'0' 을 기준으로 나눠서 나눠진 개수를 이용해보기

-> 연속된 문자를 묶어서 리스트에 추가 

'''

# 1번째 시도
# 11001100110011000001 예제에서 실패
'''
data = input().split('0')
print(data)

result1 = []
result2 = []

answer = ''

for i in data:
    if i == '':
        result1.append(i)
    else:
        result2.append(i)

if len(result1) >= len(result2):
    answer = len(result2)
else:
    answer = len(result1)

print(answer)
'''

# 2번째 시도
# 성공


s = input()
current_group = s[0] # 첫 번째 문자를 기준으로 초기 그룹 설정

result = []
count = 0

# 문자열을 순회하면서 연속된 문자를 그룹으로 묶음
for char in s[1:]:
    if char == current_group[-1]:  # 연속된 문자인 경우
        current_group += char
    else:  # 새로운 문자가 나온 경우
        result.append(current_group)
        current_group = char  # 새로운 그룹 시작
        count += 1

# 마지막 그룹을 결과 리스트에 추가
result.append(current_group)
count += 1

print(count//2)