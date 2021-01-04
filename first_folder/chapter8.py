'''
    python에서는 함수를 사용할때 def 키워드를 사용한다.
    아마 definition의 약자인 것으로 추정된다. 물론 그냥 기억하기 쉬우라고 내가 임의로 정해봤다!
'''

# 함수는 다음과 같이 3가지 상황으로 정리해볼 수 있다 !

# 1. 매개변수도 없고 반환값도 없는경우 !
'''
    def 함수명() :
        수행문장
'''
def func1():
    print('BlockDMask')
 
# 함수 호출
func1()
func1()
func1() # 함수의 호출은 일반 java와 같다 !

# 2. 매개변수만 있고 반환값은 없는경우 !
'''
    def 함수이름(매개변수1, 매개변수2, ... ):
        수행문장
'''
def func2(a, b):
    print(f'{a} 곱하기 {b} = {a * b}')
 
func2(1, 2)
func2(1, 3)
func2(2, 4)

# 3. 매개변수는 없고 반환값만 있는 경우 !
'''
    def 함수이름():
        수행문장
        return 반환값
'''
def func3():
    return "abcdefg"

a = func3()
print(a + "GG")

# 4. 매개변수와 반환값이 둘 다 있는경우 !
'''
    def 함수이름(매개변수1, 매개변수2 ...):
    수행문장
    return 반환값
'''

def func4(a, b):
    return a * b

c = func4(3, 9)
print(c)