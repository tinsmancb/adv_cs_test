def fib_iter():
    a = 0
    b = 1
    while True:
        yield b
        i = b
        b = a + b
        a = i

def main():
    fib = fib_iter()
    for i in range(15):
        print(next(fib))

if __name__ == "__main__":
    main()
