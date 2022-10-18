global selected

roomList = [
    {101 : ["미림1", "미림2", "미림3"]},
    {102 : ["미림4", "미림5", "미림6"]},
    {103 : ["미림7", "미림8", "미림9"]},
    {104 : ["미림10", "미림11", "미림12"]}
]

def showList():
    for i in range(0, 4):
        for k, v in roomList[i].items():
            print(f"{k} : ", end="")
            for i in range(0, 3):
                print(v[i], end=" ")
            print()

def findRoom(roomNum):
    for i in range(0, 4):
        for k, v in roomList[i].items():
            if(k == roomNum):
                selected = roomList[i].get(roomNum)
                print(f"{k} : ", end="")
                for i in range(0, 3):
                    print(v[i], end=" ")
                print()

def findStudent(studentName):
    for i in range(0, 3):
        if(selected[i] == studentName):
            print(f"{selected[i]} 학생의 상태를 설정합니다.")

            print("="*30)
            print("1. 잔류")
            print("2. 외출")
            print("3. 외박")
            print("="*30)
            selectState = int(input("상태를 지정해주세요 : "))

            return selectState

            break

while True:
    print("="*30)
    print("0. 종료")
    print("1. 기숙사생 명단 확인")
    print("2. 잔류 / 외박 / 외출 상태 설정")
    print("3. 잔류 / 외박 / 외출 상태 업데이트")
    print("="*30)
    select = input("할 일을 선택하세요 : ")

    if select == "0":
        print("프로그램을 종료합니다.")
        break
    elif select == "1":
        print("명단")
        showList()
        break
    elif select == "2":
        print("설정")
        selectRoom = int(input("상태를 설정하려는 학생의 호실 번호를 입력하세요 : "))
        findRoom(selectRoom)
        selectStudent = input("상태를 설정하려는 학생의 이름을 입력해주세요 : ")
        state = findStudent(selectStudent)
        break
    elif select == "3":
        print("업데이트")
    else:
        print("잘못된 번호를 입력하셨습니다.")
        continue