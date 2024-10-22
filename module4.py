N = int(input("Please enter a positive integer N : "))
numbers = []
for i in range(N):
    number = int(input(f"Please enter number {i+1}: "))
    numbers.append(number)

X = int(input("Please enter an integer X: "))
if X in numbers:
    print(numbers.index(X) + 1)
else:
    print("-1")