


def binarysearch(A,x):
    low=0
    high = len(A)-1

    while low<=high:
        mid=(low+high)
        guess=list[mid]
        if guess == x:
            return mid
            if guess > item:
                high= mid -1
            else:
                low=mid +1
            return none



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
    my_list=[1,3,5,7,9]
    B=[random.randint(0,100) for i in range (100)]
    mergesort(B)
    #print(B)
    print()
    print(binarysearch(my_list,3))
    #print(binarysearch(B,B[60]))
    #print(binarysearch(B,25))

main()
