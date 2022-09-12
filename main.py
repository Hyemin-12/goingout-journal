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
        print("'명단")
        break
    elif select == "2":
        print("설정")
        break
    elif select == "3":
        print("업데이트")
    else:
        print("잘못된 번호를 입력하셨습니다.")
        continue