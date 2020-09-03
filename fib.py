def fib_iter():
    "Iterate over the fibonacci numbers."
    a = 0
    b = 1
    while True:
        yield b
        i = b
        b = a + b
        a = i

def main():
    while True:
        num_fib = input('How many fibonacci numbers would you like to see? ')
        try:
            num_fib = int(num_fib)
            if num_fib <= 0:
                print("You need to choose at least one!")
                continue
            break
        except ValueError:
            print("{} is not a valid integer! Try again!".format(num_fib))

    fib = fib_iter()
    for i in range(num_fib):
        print(next(fib))

if __name__ == "__main__":
    main()
