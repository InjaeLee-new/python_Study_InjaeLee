"""
    기본적인 if-else 조건문 사용법을 익힌다.
"""
a = 10
b = 20
c = 20 + 3 * 3
d = 30.0000002

if a > b:
    print(a)
else:
    print(b)

# 현재 문자열과 숫자의 혼합을 사용했는데, 다음과 같은 에러를 갖는다.
# TypeError: can only concatenate str (not "int") to str
"""

if c > d :
    print("c는 " + c + "값을 가지며 30보다 큽니다.")
else:
    print("c는 " + c + "값을 가지며 30보다 작습니다.")

"""
# str(숫자) 를 사용하면 숫자를 문자열로 바꿀 수 있다.
if c > d :
    print("c는 " + str(c) + "값을 가지며 " + str(d) + "보다 큽니다.")
else:
    print("c는 " + str(c) + "값을 가지며 " + str(d) + "보다 작습니다.")

# 하지만 str()함수는 소수점 자리를 다 무시하는 변환 방법이다.
# 이를 대체할 함수로 repr()함수를 사용할 수 있다.
if c > d :
    print("c는 " + repr(c) + "값을 가지며 " + repr(d) + "보다 큽니다.")
else:
    print("c는 " + repr(c) + "값을 가지며 " + repr(d) + "보다 작습니다.")

# 근데 설명은 다른데,, 결과는 똑같았다고한다 쥬륵..