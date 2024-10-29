class Num:
    def __init__(self):
        self.numbers = []

    def input_numbers(self, n):
        for i in range(n):
            num = int(input(f"Please enter number {i+1}: "))
            self.numbers.append(num)

    def search(self, x):
        try:
            return self.numbers.index(x)+1
        except ValueError:
            return -1