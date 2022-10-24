import app

# 메인 메뉴
while True:
    print("="*30)
    print("0. 종료")
    print("1. 기숙사생 명단 확인")
    print("2. 특정 기숙사생 상태 확인")
    print("3. 기숙사생 추가 / 삭제")
    print("4. 날짜 별 기숙사생 상태 확인")
    print("="*30)
    select = int(input("할 일을 선택하세요 : "))
    print()

    if select == 0: # 프로그램 종료
        print("프로그램을 종료합니다.")
        break
    elif select == 1: # 기숙사생 명단 확인
        app.checkStudent()
    elif select == 2: # 특정 기숙사생 상태 확인
        checkRoom = int(input("상태를 확인할 기숙사생의 호실 번호를 입력하세요 : "))
        checkName = input("상태를 확인할 기숙사생의 이름을 입력하세요 : ")
        print()
        
        app.checkParticularStudent(checkRoom, checkName)
        
        while True:
            print("-"*30)
            print("1. 잔류 / 외박 / 외출 상태 변경")
            print("2. 나가기")
            print("-"*30)
            select2 = int(input("할 일을 선택하세요 : "))
            print()
            if select2 == 1: # 잔류 / 외박 / 외출 상태 변경
                print("상태 변경")
                break
            elif select2 == 2: # 메뉴 나가기
                print("나가기")
                break
            else:
                print("존재하지 않는 메뉴입니다. 다시 입력해주세요.")
                continue
    elif select == 3:
        while True:
            print("-"*30)
            print("1. 기숙사생 추가")
            print("2. 기숙사생 삭제")
            print("3. 나가기")
            print("-"*30)
            select3 = int(input("할 일을 선택하세요 : "))
            print()
            if select3 == 1: # 기숙사생 추가
                addRoom = int(input("추가할 기숙사생의 호실 번호를 입력하세요 : "))
                addName = input("추가할 기숙사생의 이름을 입력하세요 : ")

                app.addStudent(addRoom, addName)
                break
            elif select3 == 2:
                delRoom = int(input("삭제할 기숙사생의 호실 번호를 입력하세요 : "))
                delName = input("삭제할 기숙사생의 이름을 입력하세요 : ")

                app.deleteStudent(delRoom, delName)
                break
            elif select3 == 3: # 메뉴 나가기
                print("나가기")
                break
            else:
                print("존재하지 않는 메뉴입니다. 다시 입력해주세요.")
                continue
    elif select == 4:
        print("날짜 별 기숙사생 상태 확인")
    else:
        print("존재하지 않는 메뉴입니다. 다시 입력해주세요.")
        continue