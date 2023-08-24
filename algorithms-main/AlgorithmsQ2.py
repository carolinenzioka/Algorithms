


def binarysearch(A,x):
    mid=len(A)//2
    if (A[mid]==x):
        print("This number,",x, " is in the array at position: ", mid)
        return x
    elif (A[mid]>x):
        return(binarysearch(A[:mid-1],x))
    elif (A[mid]<x):
        return(binarysearch(A[mid+1:],x))
    else:
        print("This number is not in the array")
        return float('inf')


def mergesort(mylist):
    i=0
    j=0
    k=0
    list1=[]
    list2=[]
    x=len(mylist)//2
    if len(mylist)>1:
        x=len(mylist)//2
        list1 = mylist[:x]
        list2 = mylist[x:]
        mergesort(list1)
        mergesort(list2)
    while i<len(list1) and j<len(list2):
        if (list1[i] < list2[j]):
            mylist[k]=list1[i]
            i+=1
        else:
            mylist[k]=list2[j]
            j+=1
        k+=1

def main():
    print("This program searches for elements in an array.")
    import random
    random.seed(0)
    B=[random.randint(0,100) for i in range (100)]
    mergesort(B)
    print(B)
    print()
    binarysearch(B,B[4])
    binarysearch(B,B[60])
    binarysearch(B,25)

main()
