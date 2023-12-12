from Inhertence_supper import Person


class Child(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def call_variables(self):
        print('Public : ', self.age1)
        print('Protected : ', self._age2)
        # print('Private : ',self.__age3)


child = Child("KK", 28, 'M')
child.call_variables()
print(child._age2)
