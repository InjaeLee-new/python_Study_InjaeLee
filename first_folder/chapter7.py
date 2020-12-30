# python에서는 for문을 한 가지 방식만 제공한다.
'''
for [변수] in [문자열, 리스트, 튜플]:
    [수행부분]

해당 구조를 갖는다.

주의할 점은 for문의 끝에는 꼭 세미콜론(:)을 붙여줘야하고,
수행 구문이라는 것을 들여쓰기를 통해 구분지어줘야한다.
'''
# 1. 반복 횟수만 지정
for i in range(4):

    print('Hello!')

# 2. 반복 횟수는 rightNum - LeftNum 이다.
for i in range(1, 4):

    print(f'{i}번 반복합니다.')

# 3-1 성환이형의 꿀팁 강의내용
# for 변수 in *args => 해당형태처럼 *을 붙이고 뒤에 값이 오면 *뒤에 값만큼 반복문이 수행된다.
# 1번의 range 함수 대용으로 더 짧게 코딩이 가능하다.
'''
args = 3
for i in *args
    print(f'{i}번반복') # 3번 반복된다.
이렇게 하지말고
'''

'''
def sum_alot(*args):

sum = 0

*for* i *in* args:

sum = sum + i

*return* sum

print(sum_alot(1, 2, 3, 4, 5, 6)) → 21

print(sum_alot(1, 2, 3, 4)) → 10

성환이형이 짜준 코드 이렇게 활용하자.
'''
# 3. java에서 사용하던 확장 for문처럼 배열의 length만큼 반복시키는 구조를 가질수도 있다.
arr = [1, 2 ,3 ,4, 5]

for i in arr:

    print(i)


# 4. 중첩 가능한 for문
'''
for [변수1] in [문자열1, 리스트1, 튜플1]:

    [수행부분]

    for [변수2] in [문자열2, 리스트2, 튜플3]:

        [수행부분]

항상 들여쓰기는 신경써줘야한다. 해당 모양으로 for문의 중첩 사용이 가능하다.
'''

# 5. break를 이용해서 for구문을 조건에따라 탈출 가능하다.

index = 0
arr = "abcdekjnndsk" 
for a in arr:
    if a == 'k':            
        break    # 'k'를 찾으면 for문 탈출
     
    index = index + 1

print(index)    # 'k'가 첫번째로 존재하는 위치 출력

'''
for [변수1] in [문자열1, 리스트1, 튜플1]: // 조건 반복식
    [수행부분1]
    
    특정조건:
    continue

    [수행부분2]
    [수행부분3]

이렇게 특정조건을 만족해서 continue로 들어가게 되면 수행부분2, 수행부분3을 거치지 않고 바로 for 문으로 올라가서
다음 문자열을 변수에 할당받아서 for 반복문을 수행하게 된다.
'''