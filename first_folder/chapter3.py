"""
    Python에서 난수를 사용하기 위해서는 기본적으로 제공되는 random 모듈을 사용한다. random 모듈에서 자주 사용되는 함수는
    다음과 같다.
"""
# random 모듈을 임포트 시켜준다.
from random import *

# 1. randint(최솟값, 최댓값) : 입력 파라미터인 최소부터 최대까지 'int' 값을 리턴한다.
i = randint(1, 100) 
print(i) # result =  33

# 2. random() : 0부터 1 사이의 임의의 'float' 값을 리턴한다.
f = random()
print(f) # result =  0.2383488901480747

# 3. uniform(최솟값, 최댓값) : 입력 파라미터 사이에 임의의 'float' 값을 리턴한다.
f = uniform(1.0, 36.5)
print(f) # result =  11.340798931121133

#  randrange(최솟값 , 최댓값 + 1 , 간격) : 1번파라미터와 (2번파라미터-1) 사이에 지정된 간격으로 나열된 숫자중
#                                         임의의 정수를 리턴한다.
i = randrange(1, 101, 2)
print(i) # result =  73
 
# randrange(n) : 0부터 n 사이의 임의의 'int' 값을 리턴한다.
i = randrange(10)  
print(i) # result =  3