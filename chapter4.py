"""
    Python에서 MySQL Database를 사용하기 위해 Python DB API 표준을 따르는 MySQL DB모듈을 다운받아야한다.
    MySQL DB를 지원하는 모듈은 여러가지는 있는데 이중 cx_Oracle이라는 모듈을 예제로 사용한다.
    하지만 표준을 따르는 모듈이기 때문에 어떤 모듈을 사용하더라도 동일한 API를 사용한다.
"""

# 1. $ python -m pip install cx_Oracle -- upgrade
# 2. 일반 oracle 사용법처럼 CRUD 방식을 이용한다.

import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
connection = cx_Oracle.connect('javaexam','m1234','192.168.0.6:1521:xe')

cursor = connection.cursor()


cursor.execute("""
   select user_name
   from mymemoryMember
   where user_name = :texting""",
   texting = "이인제"
)



for name in cursor:
   print("테스트 이름 리스트 : ", name)