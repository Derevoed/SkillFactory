import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 0) == 0

    def test_division(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_adding_success(self):
        assert self.calc.adding(self, 9, 1) == 10

    def teardown(self):
        print('Выполнение метода Teardown')