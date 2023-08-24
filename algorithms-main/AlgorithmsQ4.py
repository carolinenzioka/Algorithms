

def sum(x):
    if x == 0:
        return 0
    else:
        return (x*x) + sum(x-1)



def main():

    print("This function that finds the sum of the squares of the first n numbers.")

    x = (eval(input("Enter number:")))

    print("your sum is",sum(x))
main()
