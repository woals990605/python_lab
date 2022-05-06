from pymysql import connect, cursors  # 접속과 읽는 위치를 위한 connect,cursors가 필요

conn = connect(
    host="localhost",
    user="green",
    passwd="green1234",
    db="greendb",
    charset="utf8"  # utf-8인것도 있고 utf8인 것도 있기 때문에 안되는경우 확인
)

cursor = conn.cursor(cursors.DictCursor)  # 기본이 tuple
