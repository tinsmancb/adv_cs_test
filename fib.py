def fib_iter():
    a = 0
    b = 1
    while True:
        yield b
        i = b
        b = a + b
        a = i

def main():
    num_fib = input('How many fibonacci numbers would you like to see? ')
    num_fib = int(num_fib)

    fib = fib_iter()
    for i in range(num_fib):
        print(next(fib))

if __name__ == "__main__":
    main()
