import copy #deepcopy를 위한 라이브러리
import numpy as np

#============================================
#클래스들
#각 상영관의 상속을 위한 상영관 클래스 
class Screen: 
    # seat 번호를 초기화하는 메소드
    def _MakeSeat(seatsize):
        seat = [] #초기화 될 2차원배열 선언
        ascii_A = 65 #아스키코드 A
        ascii_1 = 49 #아스키코드 1
        
        for _ in range(seatsize):
            listt = []
            for _ in range(seatsize):
                listt.append(chr(ascii_A)+chr(ascii_1))
                ascii_1 += 1     
            ascii_A += 1 #A~E까지 증가
            ascii_1 -= seatsize #5까지 올라간 아스키값을 다시 1로 바꿈
            
            seat.append(listt)
            
        return seat
    
    # seat의 예매 여부를 가지는 Bool List
    _seat_ticket = [[False for _ in range(5)] for _ in range(5)]
    seatsize = 5
    
    
    movie_name = "The secreat life of walter Mitty" #영화명
    time_n_seat = [         #[0]:날짜, [1]:좌석번호, [2]:좌석예매여부
        ['12:00', _MakeSeat(seatsize), np.full((seatsize,seatsize),True)],
        ['13:00', _MakeSeat(seatsize), np.full((seatsize,seatsize),True)],
        ['14:00', _MakeSeat(seatsize), np.full((seatsize,seatsize),True)],
        ['15:00', _MakeSeat(seatsize), np.full((seatsize,seatsize),True)]
        ]

#============================================
#함수들
#관리자용 함수
#상영관의 영화와 시간표를 변경해주는 함수

def moviesetup(Screen, screensize):
    print('\nWhich screen will you change?')
    for _ in range(len(Screen)):
        print(" {0}관 - {1}".format(_, Screen[_].movie_name))
    selectscreen = int(input()) #상영관 선택

    #영화변경 또는 시간 변경 기능 선택
    selectfunc = int(input("\nWhat will you change? Movie:1 / Time:2\n"))

    if selectfunc == 1: #영화명 변경을 선택한 경우
        setup_movie(Screen[selectscreen]) #선택된 상영관의 영화명을 변경 함수 호출
        if 1 == int(input("\nDo you want to chage time? Yes:1 / No:2 \n")): #상영시간 변경여부 묻기
            setup_time(Screen[selectscreen], selectscreen)

    elif selectfunc == 2: #시간 변경을 선택한 경우
        setup_time(Screen[selectscreen], selectscreen) #선택된 상영관의 상영시간을 변경하는 함수 호출
        if 1 == int(input("\nDo you want to chage movie name? Yes:1 / No:2 \n")): #영화 변경여부 묻기
            setup_movie(Screen[selectscreen])
    else:
        print("\nSelect only in 1 to 2")


#영화명을 변경하는 함수
def setup_movie(Screen):
    print("\nNow movie name is '{0}'".format(Screen.movie_name))
    Screen.movie_name = input("Enter new name of movie\n") #입력받은 영화명을 상영관의 이름으로 변경


#상영관 시간을 수정하는 함수
def setup_time(Screen, selectscreen):
    #현재 상영관의 시간표 출력
    print("\nNow {0} screen time is on ".format(selectscreen))
    for _ in range(len(Screen.time_n_seat)):
        print(Screen.time_n_seat[_][0], end=" ")

    #변경될 상영관의 시간표 입력
    print("\n\nEnter new screen time ")
    for _ in range(len(Screen.time_n_seat)):
        Screen.time_n_seat[_][0] = input(" {0} : ".format(_)) #새로운 시간을 입력
    print("Sucess to change times")
    

#영화관 총 수입을 출력하는 함수
def check_income(income):
    print("\nBoss, today's income is {0} won".format(income))

#=====================
#관객용 함수
def ticketing(Screen, price): #티켓팅을 해주는 함수

    #현재 있는 상영관 출력
    print("\nWhat movie would you like to see?")
    for _ in range(len(Screen)): 
        print(" {0}관 - {1}".format(_, Screen[_].movie_name))
    selectscreen = int(input())

    #상영관의 시간표 출력
    print("\nWhat time do you want to see?")
    for _ in range(len(Screen[selectscreen].time_n_seat)): #선택한 상영관의 시간표 출력
        print(" {0}. {1}, Available seat = {2}" #선택한 관의 상영시간 및 예매가능 자리수
            .format(_, Screen[selectscreen].time_n_seat[_][0], np.sum(Screen[selectscreen].time_n_seat[_][2])))
    selecttime = int(input())
        
    #인원을 입력
    num_person = int(input("\nHow many ticket do you want?\n")) #총 인원수 입력
    num_teen = int(input("\nHow many tennager?\n")) #청소년수 입력
    num_child = int(input("\nHow many child?\n"))#아이수 입력

    #어른의 수 체크
    if (num_person - num_child -num_teen) >= 0 :
        num_adult = num_person - num_child -num_teen
    else:
        num_adult = 0
    
    #좌석 출력
    print()
    for i in range(len(Screen[selectscreen].time_n_seat[selecttime][1])):
        for j in range(len(Screen[selectscreen].time_n_seat[selecttime][1][i])):
            print(Screen[selectscreen].time_n_seat[selecttime][1][i][j], end=" ")
        print()

    #좌석 선택
    print("\nSelect seat what you want")
    successticket = 0
    successseat = []
    while(successticket < num_person):
        selectseat = input("{0} : ".format(successticket))
        index_i, index_j = searchindex(Screen, selectscreen, selecttime, selectseat)
        if Screen[selectscreen].time_n_seat[selecttime][2][index_i][index_j] == False: #이미 예매가 된 자리인 경우
            print("It's unavailable seat. Please select other seat")
            continue #다시 선택하세요
        else:
            Screen[selectscreen].time_n_seat[selecttime][2][index_i][index_j] = False
            successseat.append(selectseat)
            successticket += 1
    
    #금액 계산
    income = num_adult * price['adult']
    income += num_teen * price['teen']
    income += num_child * price['child']

    #최종 예매결과 출력
    print("\n=============================")
    print("Success to ticketing movie!")
    print(" Screen : {0}관".format(selectscreen)) #상영관
    print(" Movie  : {0}".format(Screen[selectscreen].movie_name)) #영화이름
    print(" Time   : {0}".format(Screen[selectscreen].time_n_seat[selecttime][0])) #상영시간
    print(" Adult  : {0}".format(num_adult)) #어른의 티켓 수
    print(" Teen   : {0}".format(num_teen)) #청소년의 티켓 수
    print(" Child  : {0}".format(num_child)) #어린이의 티켓 수
    print(" Price  : {0} won".format(income))
    print(" Seat   : ", end='')
    for _ in successseat: print(_, end=" ")

    #총 수입 반환
    return income 
    


#선택한 자리의 인덱스를 알려주는 함수
def searchindex(Screen, selectscreen, selecttime, selectseat):
    for i in range(len(Screen[selectscreen].time_n_seat[selecttime][1])):
        for j in range(len(Screen[selectscreen].time_n_seat[selecttime][1][i])):
            if selectseat == Screen[selectscreen].time_n_seat[selecttime][1][i][j]: #선택한 자리의 인덱스를 찾는 중
                return i, j


def show_timetable(Screen): #상영중인 영화와 시간표 출력을 해주는 함수
    while(True):
        print("\nWhat timeline of Screen do you want to see?")
        for _ in range(len(Screen)): #현재 있는 상영관 출력
            print(" {0}관 - {1}".format(_, Screen[_].movie_name))
        selectscreen = int(input())

        print("\n{0}관".format(selectscreen)) #선택한 관
        print(Screen[selectscreen].movie_name) #선택한 관의 영화명
        for _ in range(len(Screen[selectscreen].time_n_seat)): #선택한 상영관의 시간표 출력
            print(" {0}, Available seat = {1}" #선택한 관의 상영시간 및 예매가능 자리수
                .format(Screen[selectscreen].time_n_seat[_][0], np.sum(Screen[selectscreen].time_n_seat[_][2])))
        
        #고객 페이지로 돌아갈지 아니면 다른 상영관의 시간표를 볼지 입력
        selecttodo = int(input('\nDo you want to go first page or to see other timeline?\n 1. Go to first page\n 2. See other timeline\n'))
        if selecttodo == 1: #첫 고객 페이지를 선택한 경우
            break
        elif selecttodo == 2: #다른 상영관 시간표를 선택한 경우
            continue
        else:
            print('Enter only in 1 to 2')
            continue
    