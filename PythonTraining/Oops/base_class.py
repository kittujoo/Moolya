class Calculator:
    base_class_num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("__init__")

    def get_data(self):
        print("Get_data")

    def add_two_numbers(self):
        return self.firstNumber + self.secondNumber + self.base_class_num


if __name__ == "__main__":
    obj = Calculator(2, 3)
    print(obj.base_class_num)
    print(obj.get_data())
    print(obj.add_two_numbers())
