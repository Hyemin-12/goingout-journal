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
                global selected
                selected = roomList[i].get(roomNum)
                print(f"{k} : ", end="")
                for i in range(0, 3):
                    print(v[i], end=" ")
                print()

def findStudent(studentName):
    for i in range(0, 3):
        if(selected[i] == studentName):
            print(f"{selected[i]} 학생의 상태를 설정합니다.")
            break

while True:
    print("="*30)
    print("0. 종료")
    print("1. 기숙사생 명단 확인")
    print("2. 특정 기숙사생 상태 확인")
    print("="*30)
    select = int(input("할 일을 선택하세요 : "))
    print()

    if select == 0:
        print("프로그램을 종료합니다.")
        break
    elif select == 1:
        showList()
    elif select == 2:
        print()
        selectRoom = int(input("상태를 확인하려는 학생의 호실 번호를 입력하세요 : "))
        findRoom(selectRoom)
        selectStudent = input("상태를 확인하려는 학생의 이름을 입력해주세요 : ")

        while True:
            print()
            print(f"{selectStudent} 학생의 상태를 설정합니다.")
            print("-"*30)
            print("1. 잔류 / 외박 / 외출 상태 변경")
            print("2. 나가기")
            print("-"*30)
            select2 = int(input("할 일을 선택하세요 : "))
            print()

            if select2 == 1:
                print("상태 변경")
                break
            elif select2 == 2:
                print("나가기")
                break
            else:
                print("잘못된 메뉴입니다. 다시 입력해주세요.")
                continue

    else:
        print("없는 메뉴입니다. 다시 입력해주세요.")
        continue