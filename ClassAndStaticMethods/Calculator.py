class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result = result * num
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for num in args[1:]:
            result /= num

        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result


print(Calculator.add(1, 2, 3, 4))
print(Calculator.multiply(1, 2, 3, 4))
print(Calculator.divide(120, 2, 2))
print(Calculator.subtract(90, 30, 30, 20))
