import pymysql;  # pymysql 모듈 import

# 전역변수 선언부
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row=None

# 메인 코드
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    assword='1234',
    db='sqlDB',
    charset='utf8'
) # 접속포인트

cur = conn.cursor()  # cur에 conn 값을 입력함.

cur.execute("SELECT * FROM userTbl")  #execute = 실행 명령어

print("사용자ID     사용자이름      출생연도        주소")
print("--------------------------------------------------------")


                                    # fetchone 1개 fetchall 전부
while (True) :
    row = cur.fetchone() # row에 cur fetch (인출) 
    if row== None :
        break
    data1 = row[0] # userID
    data2 = row[1] # name
    data3 = row[2] # birthYear
    data4 = row[3] # addr
    print("%5s  %10s    %10d    %10s" % (data1,data2,data3,data4))
         # 문자  문자    숫자     문자
conn.close()


