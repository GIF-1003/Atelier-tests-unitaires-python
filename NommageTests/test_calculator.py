import pytest
from NommageTests.calculator import Calculator

class TestCalculator:

    def setup(self):
        self.calculator = Calculator()

    def test_given_two_numbers_when_adding_then_sum_is_correct(self):
        # Given
        firstNumber = 5
        secondNumber = 10

        # When
        result = self.calculator.add(firstNumber, secondNumber)

        # Then
        assert result == 15

    def test_given_two_numbers_when_subtracting_then_difference_is_correct(self):
        # Given
        firstNumber = 10
        secondNumber = 5

        # When
        result = self.calculator.subtract(firstNumber, secondNumber)

        # Then
        assert result == 5

    def test_given_two_numbers_when_multiplying_then_product_is_correct(self):
        # Given
        firstFactor = 5
        secondFactor = 10

        # When
        result = self.calculator.multiply(firstFactor, secondFactor)

        # Then
        assert result == 50

    def test_given_two_numbers_when_dividing_then_quotient_is_correct(self):
        # Given
        dividend = 10
        divisor = 2

        # When
        result = self.calculator.divide(dividend, divisor)

        # Then
        assert result == 5

    def test_given_dividend_and_zero_divisor_when_dividing_then_exception_is_thrown(self):
        # Given
        dividend = 10
        divisor = 0

        # When + Then
        with pytest.raises(ValueError):
            self.calculator.divide(dividend, divisor)
