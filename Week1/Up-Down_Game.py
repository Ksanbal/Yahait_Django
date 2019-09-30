#1~100 사이 수의 Up-Down 게임을 실행하는 프로그램입니다.
#Write by KSanbal

import random #난수 산출을 위한 라이브러리 포함

def GameStart(): #게임을 실행하는 함수
    print(" Game Start!!")

    realanswer = random.randrange(1,101) #1~100의 난수 산출
    trycount = 1

    while True:
        print(" Guess what!!")
        tryanswer = int(input())

        if tryanswer > realanswer: #정답과 비교
            print(" Down!!\n")
            trycount += 1
        elif tryanswer < realanswer:
            print(" UP!!\n")
            trycount += 1
        else: #정답
            print(" That's Right!!\n",
            " You tried",trycount,"times")
            break

#메인 실행문 

print("Let's start UP-DOWN game with in 1~100\n",
    "Do you want to play? yes/no")
Iwant = input()

while(Iwant == 'yes'): 
    GameStart() #게임 실행 함수 호출
    print(" Do you want more? yes/no")
    Iwant = input()

print("Game Over")
