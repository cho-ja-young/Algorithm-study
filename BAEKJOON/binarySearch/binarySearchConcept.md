# 이코테 파이썬 기본
### 복잡도(Complexity)
#### 복잡도는 알고리즘의 성능을 나타내는 척도
* 시간 복잡도 : 특정한 크기의 입력에 대해 알고리즘의 수행 시간을 분석
* 공간 복잡도 : 특정한 크기의 입력에 대해 알고리즘의 메모리 사용량 분석
> 동일한 기능을 수행하는 알고리즘이 있다면, 일반적으로 복잡도가 낮을수록 좋은 알고리즘

<br>

### 빅오 표기법(Big-O Notation)
#### 가장 빠르게 증가하는 항만을 고려하는 표기법
* 함수의 상한만을 나타내게 된다.
* EX : 연산 횟수가 3N(3승) + 5N(2승) + 1,000,000 인 알고리즘 -> O(N(3승))
* 계수는 무시

> O(1) : 상수 시간 (Constant time) <br>
> O(logN) : 로그 시간 (Log time) <br>
> O(N) : 선형 시간 <br>
> O(NlogN) : 로그 선형 시간 <br>
> O(N의 2승) : 이차 시간 <br>
> O(N의 3승) : 삼차 시간 <br>
> O(2의 N승) : 지수 시간

<br>

### 요구사항에 따라 적절한 알고리즘 설계
#### 시간제한 (수행시간 요구사항) 가장 먼저 확인
* 시간제한이 1초인 경우의 일반적인 기준
> N의 범위가 500 : 시간 복잡도가 O(N의3승) 인 알고리즘을 설계 <br>
> N의 범위가 2,000 : 시간 복잡도가 O(N의2승) 인 알고리즘을 설계 <br>
> N의 범위가 100,000 : 시간 복잡도가 O(NlogN) 인 알고리즘을 설계 <br>
> N의 범위가 10,000,000 : 시간 복잡도가 O(N) 인 알고리즘을 설계

<br>

### 수행 시간 측정 소스코드 예제
* 일반적인 알고리즘 문제 해결 과정
```python
import time

start_time = time.time() # 측장 시작

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time: ", end_time - start_time) # 수행 시간 출력
```

---

## 파이썬 기본 문법 : 자료형
### 1. 정수형 (Integer) : 정수를 다루는 자료형
* 양의 정수, 0, 음의 정수
* 코딩테스트에서 주로 사용

<br>

### 2. 실수형 (real number) : 소수점 아래의 데이터를 포함하는 수 자료형 
* 파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리된다.
* 소수부가 0이거나 정수부가 0인 소수는 0을 생략하고 작성할 수 있다.
> EX1 : a = 5.  ->  print(a)  -> 5.0 <br>
> EX2 : a = -.7  ->  print(a)  -> -0.7 <br>
* 지수 표현 방식 :  유효숫자 e(지수 승) = 유효숫자 X 10(지수 승)
> EX3 : 1e9  ->  10의 9제곱 (1,000,000,000)
* <b>round()</b> : 반올림 함수 -> 실수 값을 제대로 비교하기 위한 방법 
> EX4 : round(123.456, 2)  ->  123.46

<br>

### 수 자료형 연산
- 나누기(/) : 나눠진 결과를 실수형으로 반환
- 나머지(%) : 
- 몫(//) : 
- 거듭제곱(**) : 
- 제곱근(**0.5) : 

<br>

### 3. 리스트 자료형 
#### 여러개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
* 인덱스는 0부터 시작
* list() or [] : 비어있는 리스트 선언 
```python
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 5
a = [0] * n
print(a)

# -> [0,0,0,0,0]
```
* <b>인덱싱(indexing)</b> : 인덱스 값을 입력하여 리스트의 특정한 원소에 접근하는 것
* 음의 정수를 넣으면 원소를 거꾸로 탐색
```python
a = [1,2,3,4,5,6,7,8,9]

# 뒤에서 첫 번째 원소 출력 
print(a[-1])

# -> 9
```
* <b>슬라이싱(slicing)</b> : 연속적인 위치를 갖는 원소들을 가져오는 방법
* 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정 
```python
a = [1,2,3,4,5,6,7,8,9]

# 두 번째 원소부터 네 번째 원소까지 
print(a[1:4])

# -> [2,3,4] 
``` 
* <b>리스트 컴프리헨션</b> : 리스트를 초기화하는 방법 중 하나 
* 대괄호 안에 반복문을 사용 
```python
# 0부터 9까지의 수를 포함하는 리스트 
array = [i for i in range(10)] 

print(array)

# -> [0,1,2,3,4,5,6,7,8,9] 

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트 
array = [i for i in range(20) if i % 2 == 1] 

print(array)

# -> [1,3,5,7,9,11,13,15,17,19] 

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트 
array = [i*i for i in range(1, 10)] 

print(array)

# -> [1,4,9,16,25,36,49,64,81] 
```
* <b>2차원 리스트를 초기화할 때, 효과적으로 사용 가능</b>
* 특히 N X M 크기의 2차원 리스트를 한 번에 초기화 해야 할 때 매우 유용
> EX : array = [[0] * m for _ in range(n)] <br>
> -> N번 반복을 할 때마다, 길이가 M인 리스트를 새롭게 초기화하는 방식으로 리스트를 구성 
> 
> 그냥 [[0] * m] * n 이런 식으로 리스트 초기화를 해버리면, [[0] * m] 이라는 내부적인 리스트가 모두 같은 객체로써 인식될 수 있다. 

<br>

### 리스트 관련 기타 메서드
#### append()
- 리스트에 원소를 하나 삽입할 때 사용
- 변수명.append()
- 시간 복잡도 : O(1)

#### sort()
- 기본 정렬 기능 : 오름차순
- 변수명.sort(reverse = True) : 내림차순 
- 시간 복잡도 : 0(NlogN)

#### reverse()
- 리스트의 원소 순서 뒤집기
- 변수명.reverse()
- 시간 복잡도 : O(N)

#### insert()
- 특정한 인덱스 위치에 원소를 삽입
- insert(삽입할 위치 인덱스, 삽입할 값)
- 시간 복잡도 : O(N)

#### count()
- 리스트에서 특정한 값을 가지는 데이터의 개수 세기
- 변수명.count(특정한 값)
- 시간 복잡도 : O(N)

#### remove()
- 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러개면 하나만 제거
- 변수명.remove(특정값)
- 시간 복잡도 : O(N)

```python
# 리스트에서 특정 값을 가지는 원소를 모두 제거하려면?

a = [1,2,3,4,5,5,5]
remove_set = {3, 5} # 집합 자료형

# remove_set 에 포함되지 않은 값만을 저장
result = [i for i in a if not in remove_set]
print(result)

# -> [1,2,4]
```

<br>

### 4. 문자열 자료형 
#### 문자열 변수를 초기화할 때, 큰따옴표(")나 작은 따옴표(')를 이용 
* 백슬래시 사용시, 원하는 만큼 포함 가능
```python
data = "Don't you know \"Python\"?"
print(data)

# -> Don't you know "Python"?
```

#### 문자열 연산
* 문자열 변수가 덧셈(+) 이용시, 문자열이 더해져 연결(concatenate)된다.
* 특정한 양의 정수와 곱하는 경우, 그 값만큼 문자열이 여러 번 더해진다.
* 인덱싱과 슬라이싱 사용 가능
* 단, 특정 인덱스 값 변경은 불가능 (immutable)

```python
# 덧셈 이용 
a = "Hello"
b = "World"
print(a + " " + b)

# -> Hello World

# 곱셈 이용 
a = "String"
print(a * 3)

# -> StringStringString

# 슬라이싱 
a = "ABCDEF"
print(a[2:4])

# -> CD
```

<br>

### 5. 튜플 자료형 
* 한 번 선언된 값은 변경이 불가능
* 리스트 -> 대괄호 []
* 튜플 -> 소괄호 ()
* 튜플은 리스트에 비해 상대적으로 공간 효율적

```python
a = (1,2,3,4,5,6,7,8,9)

# 네 번째 원소만 출력
print(a[3])

# -> 4

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# -> (2,3,4)
```

#### 튜플을 사용하면 좋은 경우
* 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
> 최단 경로 알고리즘에서는 (비용, 노드 번호) 형태로 튜플 자료형 자주 사용
* 데이터의 나열을 해싱(Hashing)의 키값으로 사용해야 할 때
> 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사요오딜 수 있다.
* 리스트보다 메모리를 효율적으로 사용해야 할 때

<br>

### 6. 사전 자료형 
#### 키(key)와 값(value) 쌍을 데이터로 가지는 자료형
* 순차적 저장(리스트, 튜플) 과는 대비되는 특징
* '변경 불가능한(immutable) 자료형'을 키로 사용할 수 있다.
* 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 <b>데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리</b> 할 수 있다.

#### 키와 값을 별도로 뽑아내기 위한 메서드를 지원
* keys() : 키 데이터만 뽑아서 리스트로 이용
* values() : 값 데이터만 뽑아서 리스트로 이용 
```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
print(key_list)

# -> dict_keys(['사과', '바나나', '코코넛'])

# 값 데이터만 담은 리스트
value_list = data.values()

# -> dict_values(['Apple', 'Banana', 'Coconut'])

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
    
'''
-> Apple
   Banana
   Coconut
'''
```

<br>

### 7. 집합 자료형 
* 중복 허용 X, 순서 X -> 데이터 존재 유무에 많이 활용하는 이유
* 집합은 리스트 혹은 문자열 이용해 초기화 가능 : set([]) 사용
* 중괄호 {} 안의 각 원소를 콤마(,)를 기준으로 구분해 삽입 -> 초기화 가능
* 데이터의 조회 및 수정에 있어서 O(1) 시간에 처리가 가능

#### 집합 자료형 연산
* 합집합 : A or B
* 교집합 : A and B
* 차집합 : A - B
```python
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

# 합집합
print(a|b)

# -> {1,2,3,4,5,6,7}

# 교집합
print(a&b)

# -> {3,4,5}

# 차집합
print(a-b)

# -> {1,2}
```

#### 집합 자료형 관련 함수 
* add : 원소 하나 추가 
* update : 원소 여러 개 추가 
* remove : 삭제 
```python
data = set([1,2,3])
print(data)

# -> {1,2,3}

# 새로운 원소 추가
data.add(4)
print(data)

# -> {1,2,3,4}

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# -> {1,2,3,4,5,6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# -> {1,2,4,5,6}
```

<br>

### 사전 자료형과 집합 자료형의 특징
* 리스트, 튜플 : 순서 O -> 인덱싱을 통해 자료형의 값 얻음
* 사전, 집합 : 순서 X -> 인덱싱으로 값 얻기 불가능
> 사전의 키(key) 혹은 집합의 원소(element) 이용해 0(1)의 시간복잡도로 조회.
> 
> 키나 원소의 값으로는 변경불가능한 문자열이나 튜플 같은 객체가 사용되어야 한다. 

---

## 파이썬 기본 문법 : 기본 입출력 
### 자주 사용되는 표준 입력 방법
* input() : 한 줄의 문자열을 입력 받는 함수
* map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용하는 함수
> 공백을 기준으로 구분된 데이터를 입력 받을 때
> 
> -> list(map(int, input().split()))
> 
> 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 아래처럼 사용
> 
> -> a, b, c = map(int, input().split())

#### 사용자로부터 빠르게 입력받아야 할 때
* sys.stdin.readline() 메서드
* 입력 후 엔터(enter)가 줄바꿈 기호로 인식되므로 rstrip() 메서드를 함께 사용 
* 이진탐색, 정렬, 그래프 관련 문제에서 자주 사용

```python
import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)
```
<br>

### 자주 사용되는 표준 출력 방법
#### print()
* 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분해 출력
* 기본적으로 출력 이후에 줄 비꿈을 수행
* 줄바꿈 원치 않는 경우에 'end' 속성 이용

#### f-string
```python
answer = 7
print(f"정답은 {answer}입니다.")

# -> 정답은 7입니다.
```

---

## 파이썬 기본 문법 : 조건문 과 반복문  
### 조건문 
* 프로그램의 흐름을 제어하는 문법 
* 조건문 이용해 프로그램 로직을 설정 
* 기본 형태 : if ~ elif ~ else

#### 파이썬에서는 코드의 블록(block)을 들여쓰기(indent)로 지정
* 4개의 공백 문자 사용이 표준 

#### 비교 연산자
* 특정한 두 값을 비교하는데 사용
> X == Y : X와 Y가 같을 때 참(True)
> 
> X != Y : X와 Y가 다를 때 참 
> 
> X > Y : X가 Y보다 클 때 
> 
> X < Y : X가 Y보다 작을 때 
> 
> X >= Y : X가 Y보다 크거나 같을 때 
> 
> X <= Y : X가 Y보다 작거나 같을 때

#### 논리 연산자
* 논리값 (True / False) 사이의 연산을 수행할 때 사용
> X and Y : X와 Y가 모두 참일 때 참(True)
> 
> X or Y : X와 Y때 중 하나만 참이어도 참 
> 
> not X : X가 거짓(False)일 때 참 

#### 기타 연산자
* 다수의 데이터를 담는 자료형을 위해 제공
* 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능 
> x in 리스트 : 리스트 안에 x가 들어있을 때 참(True)
> 
> x not in 문자열 : 문자열 안에 x가 들어있지 않을 때 참

#### pass 키워드
* 아무것도 처리하고 싶지 않을 때 사용 
* 디버깅 과정 (프로그램 동작 과정 확인) 경우에 사용 

### 조건문의 간소화
* 조건문에서 실핼될 소스코드가 한 줄인 경우
```python
score = 85

if score >= 80: result = "Success"
else: result = "Fail"

# -> Success
```
* 조건부 표현식(Conditional Expression)
* if ~ else 문을 한줄에 작성
```python
score = 85

result = "Success" if score >= 80 else "Fail"
print(result)

# -> Success
```

<br>

### 반복문 
* 특정한 소스코드를 반복적으로 실행하고자 할 때 사용 
* while문, for문 (더 간결한 경우 많음)

> while 반복문 안에서의 무한루프 항상 주의

#### continue
* 반복문에서 남은 코드 실행을 건너뒤고, 다음 반복을 진행
```python
result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue # 아래 내용 실행 X
    result += i

print(result)

# -> 25
```

#### break
* 반복문에서 즉시 탈출하고자 할 때 
```python
i = 1

while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1

'''
-> 현재 i의 값: 1
   현재 i의 값: 2
   현재 i의 값: 3
   현재 i의 값: 4
   현재 i의 값: 5
'''
```

---

## 파이썬 기본 문법 : 함수   
### 함수(function)
* 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미 
* 불필요한 소스코드 반복을 줄일 수 있음
    - 매개변수 : 함수 내부에서 사용할 변수
    - 반환 값 : 함수에서 처리된 결과를 반환 
```python
def 함수명(매개변수):
    실행할 소스코드
    
    return 반환 값 
```

* 내장 함수 : 파이썬이 기본적으로 제공하는 함수
* 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수 
    - 파라미터 변수 직접 지정 가능
    - 매개변수 순서가 달라도 상관 X

    
* 여러개의 반환 값울 가질 수 있음

<br>

### global 키워드
* global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고 바로 참조
```python
a = 0

def func():
    global a
    a += 1
    
for i in range(10):
    func()
    
print(a)
```

<br>

### 람다 표현식
* 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다
* 특정 기능 수행 함수를 한 줄에 작성이 가능
```python
def add(a, b):
    return a + b
    
# 일반적인 add() 메서드 사용
print(add(3, 7))

# -> 10

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

# -> 10
```

<활용>
1) 어떤 함수 자체를 입력으로 받는 또 다른 함수가 존재할 때, 유용하게 사용이 가능
2) 한번 사용하고 말 경우에도 사용 

#### 내장 함수에서 잘 사용되는 람다 함수 
```python
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# 함수 정의 
def my_key(x):
    return x[1]
    
print(sorted(array, key=my_key))

# -> key=my_key : 정렬 기준
# -> x[1] : ('홍길동', 50) 에서 두번째 원소를 기준으로 정렬하겠다. 

# 람다 함수 사용 
print(sorted(array, key=lambda x: x[1]))

# -> [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
```
#### 여러개의 리스트에 적용
```python
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))

# -> [7,9,11,13,15]
```

---

## 파이썬 기본 문법 : 실전에서 유용한 표준 라이브러리  
### 내장 함수
* 기본 입출력 함수 ~ 정렬 함수 같은 기본적인 함수를 제공 
    - 필수 기능을 포함 
    - import 없이 사용 
```python
# sum() : 합 반환 
result = sum([1,2,3,4,5])
print(result)

# -> 15

# min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result)

# -> 2 7

# eval() : 수식 있을 때, 계산 겨로가 수로 반환 
result = eval("(3+5)*7")
print(result)

# -> 56

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result)
print(reverse_result)

# -> [1,4,5,8,9]
# -> [9,8,5,4,1]

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# -> [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
```

### itertools
* 파이썬에서 반복되는 형태의 데이터 처리에 유용한 기능들 제공
    - 순열과 조합 라이브러리 많이 사용
    - 모든 경우의 수 
* 순열 : 서로 다른 n 개에서 서로 다른 r 개를 선택하여 일렬로 나열 
```python
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# -> [('A', 'B', 'C'), ... ('C', 'B', 'A')]
```
* 중복 순열
```python
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용) 
print(result)

# -> 
```  
* 조합 : 서로 다른 n 개에서 순서에 상관 없이 서로 다른 r 개를 선택
```python
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기 
print(result)

# -> [('A', 'B'), ('A', 'C'), ('B', 'C')]
```
* 중복 조합 
```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용) 
print(result)

# -> 
``` 

### heapq
* 힙(Heap) 자료구조를 제공 
    - 일반적으로 우선순위 큐 기능 구현을 위해 사용됨
    - 최단경로 알고리즘 : 다익스트라 
    
### bisect
* 이진 탐색(Binary Search) 기능을 제공 
    
### collections
* 덱(deque), 카운터(counter) 등의 유용한 자료구조 포함
    - 카운터(counter) : 등장 횟수를 세는 기능
    > 리스트와 같은 반복 가능한 객체가 주어졌을 때, 내부에 원소가 몇 번식 등장했는지 알려준다.
```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환 

'''
-> 3
   1
   {'red': 2, 'blue': 3, 'green': 1}
'''
```  

### math
* 필수적인 수학 기능 제공
    - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수
    - 파이(pi) 와 같은 상를 포함
* 최대공약수를 구할 때 : gcd() 함수
```python
import math

# 최소공배수(LCM) 를 구하는 함수
def lcm(a,b):
    return a * b // math.gcd(a,b)
    
a = 21
b = 14

print(math.gcd(21, 14)) # 최대공약수(GCD) 계산
print(lcm(21, 14)) # 최소공배수(LCM) 계산

'''
-> 7
   42
'''
```  

---

* 출처

Link : [(이코테 2021 강의 몰아보기) 1. 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기](https://www.youtube.com/watch?v=m-9pAwq1o3w&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=1&pp=iAQB, "by 동빈나")