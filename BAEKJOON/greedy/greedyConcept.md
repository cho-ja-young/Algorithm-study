# CHAPTER 03 그리디 
### 현재 상황에서 지금 당장 좋은 것만 고르는 방법 
#### 코딩테스트에서 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 한다.

* 예1 : 거스름돈 문제
  > 가장 큰 단위로 나누고 그 다음 작은 단위로 나누기
  > 
> 화폐의 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K) <br>
> -> 화폐 종류만큼 반복하기 때문이다.
* 예2 : 1이 될때까지
  > 가능한 최대한 많이 나누기
* 예3 : 곱하기 혹은 더하기 
  > 연산을 해야하는 두 수 중에 어느 하나라도 0이나 1이면 무조건 더하기 <br>
  > 두 수 모두 2 이상이면 곱하기 

<br>