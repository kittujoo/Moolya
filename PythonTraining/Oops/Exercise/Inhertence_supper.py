class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.age1 = age
        self._age2 = age
        self.__age3 = age


    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def display_info1(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Call the __init__ method of the parent class using super()
        super().__init__(name, age)
        self.employee_id = employee_id

    # Override the display_info method
    def display_info(self):
        # Call the overridden method from the parent class using super()
        # super().display_info()
        print(f"Employee ID: {self.employee_id}")

    def simple(self):
        super().display_info()
        print('Public : ', self.age1)
        print('Protected : ', self._age2)
        # print('Private : ',self.__age3)


if __name__ == "__main__":

    # Create an instance of the Employee class
    employee = Employee("John Doe", 30, "E12345")

    # Call the overridden method in the Employee class
    employee.display_info()
    employee.simple()
