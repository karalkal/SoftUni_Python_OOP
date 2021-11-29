class vowels:
    all_vowels = "ayouei" + "ayouei".upper()

    def __init__(self, text):
        self.text = text
        self.current_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_idx < len(self.text) - 1:
            self.current_idx += 1
            if self.text[self.current_idx] in self.all_vowels:
                return self.text[self.current_idx]

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
