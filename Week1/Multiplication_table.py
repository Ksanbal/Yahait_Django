#짝수 또는 홀수의 구구단을 출력해주는 프로그램입니다.
#구구단 함수 2개를 얘기하셨지만, 1개로 실행이 가능해서 1개로 작성했습니다.
#Write by KSanbal

def gugudan(dan): #구구단을 계산해 출력하는 함수
    while dan < 10: 
        print(dan, "단\n")

        for i in range(1,10):
            print(" {0} * {1} = {2}\n".format(dan, i, dan*i))

        dan += 2

while True:
    print(" Enter the Multiplication table what you want")
    print(" 1 : Odd dan, 2 : Even dan, 3 : Stop, other : Retry")

    daninput = int(input())

    if daninput == 1:
        gugudan(daninput + 2) #홀수 구구단 호출
        break
    elif daninput == 2:
        gugudan(daninput) #짝수 구구단 호출
        break
    elif daninput == 3:
        break
    else:
        print(" Retry")
        continue
    

