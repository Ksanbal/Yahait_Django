#클래스로 작동하는 게산기 프로그램이고, 어떤 연산을 몇번 했는지 알 수 있습니다.
#Write by Ksanbal

import Calculator_mods as cm

Cal = cm.Cal()

while(True):
    print("\nEnter the expression!\n(Please enter space key between numbers and arithmetic ex) 10 + 3)\nIf you want to show Calculate times, Enter Show")
    exp = input().split(' ')

    if '+' in exp:
        Cal.sum(int(exp[0]), int(exp[2]))
    elif '-' in exp:
        Cal.sub(int(exp[0]), int(exp[2]))
    elif '*' in exp:
        Cal.mul(int(exp[0]), int(exp[2]))
    elif '/' in exp:
        Cal.div(int(exp[0]), int(exp[2]))
    elif 'Show' in exp:
        Cal.print_times()
    else:
        print("*Sorry! I can't understand your expression!!*")
    

    