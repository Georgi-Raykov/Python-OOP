from math import floor


class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):

        result = Integer.convert_from_roman_numbers(value)
        return cls(result)
    @classmethod
    def from_string(cls, value):

        if not isinstance(value, str):
            return "wrong type"
        try:
            number = int(value)
        except:
            return "wrong type"

    @staticmethod
    def convert_from_roman_numbers(num):
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev_value = 0

        # Обхождаме символите от римското число
        for symbol in num:
            current_value = roman_values[symbol]

            # Ако текущата стойност е по-голяма от предишната, следва изваждане
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            prev_value = current_value

        return total


first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
float_numbers = Integer.from_float('2.6')
print(float_numbers)

print(Integer.from_string(567))
