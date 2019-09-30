import Cinema_mods as cm #클래스와 함수가 포함된 파일 import

#영화관의 상영관을 담을 리스트 생성
Megabox = []
screensize = 3 #상영관 개수 지정
#상영관 객체 생성
for _ in range(screensize):
    Megabox.append(cm.Screen())

allincome = 0 #총 수입 선언
ticket_price = {'adult':8000, 'teen':6000, 'child':4000}


while(True):
    print("\n===============================")
    print("Welcome to Megabox!!\nWhat will you do?")
    selectmode = int(input(" 1. Admin page\n 2. User page\n 3. Exit Program\n"))

    if selectmode == 1: #관리자 메뉴
        while(True):
            print("\n===============================")
            print("Hello Boss.\nWhat will you do?")
            selectadmin = int(input(" 1. Setup Movie and Timeline\n 2. Check all income\n 3. Back to Main page\n 4. Exit Program\n"))

            if selectadmin == 1: #시간표 설정
                cm.moviesetup(Megabox, 3) #영화관의 상영관 리스트와 상영관 개수로 함수호출
            elif selectadmin == 2: #총수입 확인
                cm.check_income(allincome)
            elif selectadmin == 3: #메인화면
                break
            elif selectadmin == 4: #프로그램 종료
                print("Exit Program")
                exit()
            else:
                print("*Enter only in 1 to 4*")
                continue

    
    elif selectmode == 2: #고객 메뉴
        while(True):
            print("\n===============================")
            print("Hello sir.\nWhat do you want?")
            selectuser = int(input(" 1. Ticketing\n 2. Show movie timetable\n 3. Back to Main page\n 4. Exit Program\n"))

            if selectuser == 1: #영화예매
                allincome += cm.ticketing(Megabox, ticket_price)
            elif selectuser == 2: #영화시간표 보기
                cm.show_timetable(Megabox)
            elif selectuser == 3: #메인화면
                break
            elif selectuser == 4: #프로그램 종료
                print("Exit Program")
                exit()
            else:
                print("*Enter only in 1 to 4*")
                continue
    elif selectmode == 3:
        print("Exit Program")
        exit()

    else:
        print("*Enter only in 1 to 4*")
        continue            