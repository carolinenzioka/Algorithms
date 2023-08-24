def Fibonacci(x):

    if x == 0:
        return 0

    elif x == 1:
        return 1

    else:
        return Fibonacci(x-1) + Fibonacci(x-2)


def main():

    print("This function calculates any given Fibonacci number.")

    x = (eval(input("Enter a positive integer:")))

    print("The Fibonacci number is:", Fibonacci(x))

main()
