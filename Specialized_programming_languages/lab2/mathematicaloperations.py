from math import sqrt


class MathematicalOperations():

    def addition(self, first_param, second_param):
        return first_param + second_param

    def subtraction(self, first_param, second_param):
        return first_param - second_param

    def multiplication(self, first_param, second_param):
        return first_param * second_param

    def division(self, first_param, second_param):
        if second_param == 0:
            raise ZeroDivisionError("Division by zero error, division by zero is not possible")
        else:
            return first_param / second_param

    def exponentiation(self, first_param, second_param):
        return first_param ** second_param

    def square_root(self, param):
        if param < 0:
            return "Cannot take the square root of a negative number!"
        else:
            return sqrt(param)

