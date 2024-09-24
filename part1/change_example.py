'''
<문제> 거스름돈

당신은 음식점의 계산을 도와주는 점원입니다. 
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정합니다.
손님에게 거슬러 주어야 할 돈이 N원일 때, 거슬러 주어야 할 동전의 최소 개수를 구하세요.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.

- 문제 해결 아이디어 : 가장 큰 화폐 단위부터 돈을 거슬러 주면 된다.
- 정당성 분석 : 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문

(예) 만약에 800원을 거슬러 주어야 하는데 화폐 단위가 500, 400, 100 이라면?
500 + 100x3  보다  400x2   가 더 적은 동전으로 만들 수 있는 경우임 
-> 500이 400의 배수가 아니기 때문에 발생하는 일 


'''

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    count += n//coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)


'''
>> 시간복잡도 분석

화폐의 종류가 K 라고 할 때, 소스코드의 시간복잡도는 O(K)
-> 즉, 화폐의 종류만큼만 반복을 수행하면 답을 도출할 수 있다는 것

이 알고리즘의 시간복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받는다
'''