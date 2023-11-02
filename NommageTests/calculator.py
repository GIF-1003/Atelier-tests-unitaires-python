class Calculator:
    @staticmethod
    def add(firstNumber, secondNumber):
        return firstNumber + secondNumber

    @staticmethod
    def subtract(firstNumber, secondNumber):
        return firstNumber - secondNumber

    @staticmethod
    def multiply(firstFactor, secondFactor):
        return firstFactor * secondFactor

    @staticmethod
    def divide(dividend, divisor):
        if divisor == 0:
            raise ValueError("Division by zero is not allowed.")
        return dividend // divisor
