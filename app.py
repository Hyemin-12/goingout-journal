from datetime import datetime
import sqlite3

# 전역 변수 선언
db, cur = None, None # 연결자, 커서를 저장하는 변수 초기화
room, name, state, date = "","","",""

# 테이블 삭제
# db.execute("DROP TABLE studentTable")

# 메인 코드 부분
# def manageStudent():

# 기숙사생 추가
def addStudent(addRoom, addName, state = "잔류중"):
    db = sqlite3.connect(".\dormDB")
    cur = db.cursor()

    # 테이블 유무 확인
    cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE name = 'studentTable'")
    tableCheck = cur.fetchone()
    if tableCheck[0] == 0:
        # 테이블 추가
        cur.execute("CREATE TABLE studentTable (room int, name char(15), state char(15), date char(15))")

    date = datetime.now().date()

    cur.execute("INSERT INTO studentTable (room, name, state, date) VALUES(?, ?, ?, ?)",[addRoom, addName, state, date])

    db.commit()
    db.close()

# 기숙사생 삭제
def deleteStudent(delRoom, delName):
    db = sqlite3.connect(".\dormDB")
    cur = db.cursor()

    # 데이터 삭제
    cur.execute("DELETE FROM studentTable WHERE room=? AND name=?", [delRoom, delName])
    cur.fetchall()

    db.commit()
    db.close()

# 기숙사생 확인
def checkStudent():
    db = sqlite3.connect(".\dormDB")
    cur = db.cursor()

    # 데이터 조회
    cur.execute("SELECT * FROM studentTable ORDER BY room, name")
    
    res = []

    while True:
        row = cur.fetchone()
        if row == None:
            break
        room = row[0]
        name = row[1]
        state = row[2]
        date = row[3]

        text = f"{room}\t{name}\t\t{state}\t\t{date}"
        res.append(text)

    return res

    db.close()

# 특정 호실 기숙사생 이름 가져오기
def getParticularStudents(checkRoom):
    db = sqlite3.connect(".\dormDB")
    cur = db.cursor()

    cur.execute("SELECT * FROM studentTable WHERE room=? ORDER BY name", [checkRoom])

    res = []

    while True:
        row = cur.fetchone()
        if row == None:
            break
        name = row[1]
        res.append(name)

    return res

    db.close()

# 특정 기숙사생 확인
def checkParticularStudent(checkName):
    db = sqlite3.connect(".\dormDB")
    cur = db.cursor()

    # 데이터 조회
    cur.execute("SELECT * FROM studentTable WHERE name=?", [checkName])

    res = []

    row = cur.fetchone()
    name = row[1]
    state = row[2]

    res.append(name)
    res.append(state)

    return res

    db.close()

# 특정 기숙사생 상태 변경
def changeParticularStudent(name, status):
    db = sqlite3.connect(".\dormDB")
    cur = db.cursor()

    date = datetime.now().date()
    
    # 데이터 업데이트 / 조회
    cur.execute("UPDATE studentTable SET state=?, date=? WHERE name=?", [status, date, name])
    db.commit()
    cur.execute("SELECT * FROM studentTable WHERE name=?", [name])

    row = cur.fetchone()
    state = row[2]

    return state

    db.close()

# 참고 사이트
# 테이블 유무 확인 https://eggwhite0.tistory.com/138
# 데이터 조회 https://velog.io/@raed123456/23장.-간단한-데이터베이스#파이썬에서-데이터를-조회하는-코딩--순서
# 데이터 삭제 https://seong6496.tistory.com/171