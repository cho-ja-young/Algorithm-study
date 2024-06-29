'''
스파와 르탄이는 영어 공부를 하고 있습니다. 

1부터 10까지의 숫자를 영어로 익히는 것이 쉽지 않은지 르탄이가 스파에게 게임을 제안합니다. 바로 영어와 숫자를 섞은 문자를 모두 숫자로 바꿔내는 것이죠!

영어와 숫자가 무작위로 조합된 문자열 s를 매개변수로 주어지고, 이 s가 원래 의미하는 숫자로만 return 하도록 solution 함수를 완성해주세요

아래의 영단어 표와 예시를 참조해주세요
'''

# ""8zerothree2"" → 8032
# ""seven73nine"" → 7739
# ""two53eightfour"" → 25384

s1 = "8zerothree2"
s2 = "seven73nine"
s3 = "two53eightfour"

def solution(s):
    num_dict = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }

    for str in num_dict:
        s = s.replace(str, num_dict[str])
    answer = int(s)
    return answer

print(solution(s1))
print(solution(s2))
print(solution(s3))