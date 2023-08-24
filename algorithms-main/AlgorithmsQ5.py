

def gcd(a,b):

    if((a%b) == 0):
        return b

    else:
        return gcd(b,a%b)


def main():
    print("This function finds the gcd of two non-negative numbers using the Euclidean algorithm:")
    a = eval(input("Enter a positive integer:"))
    b = eval(input("Enter another positive integer:"))

    print(gcd(a,b))

main()
