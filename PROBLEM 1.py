class Calc:
    def cal(self, a, b, var):
        if var == 'add':
            return a + b
        if var == 'sub':
            return a - b
        if var == 'mul':
            return a * b
        if var == 'div':
            if b == 0:
                return 'Zero Div Error'
            return a / b
        return 'Invalid'

calculate = Calc()
print(calculate.cal(10, 5, 'add'))
print(calculate.cal(10, 5, 'sub'))
print(calculate.cal(10, 5, 'mul'))
print(calculate.cal(10, 5, 'div'))
