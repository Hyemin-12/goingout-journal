# 사용자로부터 데이터를 입력받아서 DB에 저장하는 실습
import sqlite3

# 전역 변수 선언
db, cur = None, None # 연결자, 커서를 저장하는 변수 초기화
room, studentId, name, state = "","","",""

# 메인 코드 부분
if __name__ == '__main__':
    db = sqlite3.connect("E:\python\프로젝트\dormDB")
    cur = db.cursor()
    
    # 테이블 삭제
    # db.execute("DROP TABLE studentTable")

    # 테이블 추가
    cur.execute("CREATE TABLE studentTable (room int, studentId int, name char(15), state char(15))")

    # 무한 루프를 돌면서 사용자로부터 데이터를 입력받는 코드
    while True:
        room = input("호실 입력: ")
        if room == "": # 엔터 치면 종료
            break
        studentId = input("학번 입력: ")
        name = input("기숙사생 이름 입력: ")
        state = (input("상태 입력(잔류중 / 외박중 / 외출중): "))

        cur.execute("INSERT INTO studentTable (room, studentId, name, state) values(?, ?, ?, ?)",(room , studentId, name, state))
    db.commit()

    # 데이터 조회
    cur.execute("SELECT * FROM studentTable ORDER BY room")

    print("호실 번호\t학번\t학생 이름\t상태")
    print('------------------------------------------------')

    while True:
        row = cur.fetchone()
        if row == None:
            break
        room = row[0]
        studentId = row[1]
        name = row[2]
        state = row[3]
        print(f"{room}\t\t{studentId}\t\t{name}\t\t{state}")

    db.close()


# 참고 사이트
# https://velog.io/@raed123456/23장.-간단한-데이터베이스#파이썬에서-데이터를-조회하는-코딩--순서