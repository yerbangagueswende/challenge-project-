class Calculator(): 
    def __init__(self):
        self.result = 0
        self.num1 = 0
        self.num2 = 0
        self.operator = ''
        self.operators = ['+', '-', '*', '/']

    def set_num1(self, num1: int):
        self.num1 = num1

    def set_num2(self, num2: int):
        self.num2 = num2

    def set_operator(self, operator: str):
        self.operator = operator

    def get_result(self):
        return self.result
    