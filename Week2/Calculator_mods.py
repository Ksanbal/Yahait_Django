#계산기 프로그램의 클래스를 가진 파일입니다.
#Write by Ksanbal

class Cal():
    _caltime = {'sum':0, 'sub':0, 'mul':0, 'div':0}

    def __init__(self):
        print("\nLet's start calculation!!")

    def sum(self, addend, augend):
        print(" SUM\n{0} + {1} = {2}".format(addend, augend, addend+augend))
        self._caltime['sum'] += 1

    def sub(self, addend, augend):
        print(" SUB\n{0} - {1} = {2}".format(addend, augend, addend-augend))
        self._caltime['sub'] += 1

    def mul(self, addend, augend):
        print(" MUL\n{0} * {1} = {2}".format(addend, augend, addend*augend))
        self._caltime['mul'] += 1

    def div(self, addend, augend):
        print(" DIV\n{0} / {1} = {2}".format(addend, augend, addend/augend))
        self._caltime['div'] += 1

    def print_times(self):
        print("\n==========================")
        print("You did {0} times of Calculation".format(sum(self._caltime.values())))
        print(" SUM : {0}".format(self._caltime['sum']))
        print(" SUB : {0}".format(self._caltime['sub']))
        print(" MUL : {0}".format(self._caltime['mul']))
        print(" DIV : {0}".format(self._caltime['div']))
        print("==========================")
