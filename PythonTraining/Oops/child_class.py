from base_class import Calculator


class CalculatorFunc(Calculator):
    child_class_num = 200

    def __init__(self):
        Calculator.__init__(self, 2, 2)

    def child_add_two_numbers(self):
        return self.firstNumber + self.secondNumber + self.child_class_num


if __name__ == "__main__":
    obj = CalculatorFunc()
    print(obj.child_class_num)
    print(obj.add_two_numbers())
    print(obj.child_add_two_numbers())
