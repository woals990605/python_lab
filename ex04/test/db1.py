# python -m pip install pymysql 마리아 db 사용을 위한 라이브러리 설치(빌드까지 된다)
from db import connect as db

insert_sql = "INSERT INTO my_member(username, password) VALUES(%s, %s)"
db.cursor.execute(insert_sql, ["love", "1234"])
db.conn.commit()
# conn.rollback() 트랜잭션 단위에 하나의 카운팅 변수를 만들어 카운트가 0이면 commit 그렇지 않으면 rollback 해준다.
