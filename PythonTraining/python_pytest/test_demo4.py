import pytest


@pytest.mark.usefixtures("setup")
class TestPythonPytest:

    def test_case8(self):
        print("This is 3rd test function")

    def test_case9(self):
        print("This is 4th test function")

    def test_case10(self):
        print("This is 5th test function")


@pytest.mark.usefixtures("data")
class Test_data:
    def test_tc1(self, data):
        print(data)


@pytest.mark.usefixtures('name')
class Test_names:
    def test_tc2(self, name):
        print(name[0])



@pytest.mark.usefixtures('return_names')
class Test_NamesReturn:
    def test_tc3(self, return_names):
        print(return_names)