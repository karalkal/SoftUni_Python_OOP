class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        """
        Copied from https://www.tutorialspoint.com/roman-to-integer-in-python
        """

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            if value.isnumeric():
                return cls(int(value))
        return "wrong type"

    def __str__(self):
        return f'{self.value}'


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(Integer.from_roman('XIV'))
print(Integer.from_roman("IV"))
print(Integer.from_float(3.14))
print(Integer.from_float('3.14'))
print(Integer.from_roman('IVIVVVVV'))
print(Integer.from_string('IVIVVVVV'))
print(Integer.from_string('3'))
print(Integer.from_string('3.14'))
print(Integer.from_string(1))
print(Integer.from_float(2.5))
