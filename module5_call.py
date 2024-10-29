from module5_mod import Num


def main():
    module = Num()
    n = int(input("Please enter a positive integer: "))
    module.input_numbers(n)
    x = int(input("Enter a integer to search: "))
    result = module.search(x)
    print(result)


if __name__ == "__main__":
    main()