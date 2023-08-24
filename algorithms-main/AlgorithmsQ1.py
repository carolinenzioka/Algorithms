
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
        if list1[i] < list2[j]:
            mylist[k]=list1[i]
            i+=1
        else:
            mylist[k]=list2[j]
            j+=1
        k+=1



def main():
    print("This program computes the mergesort of the array B")
    import random
    random.seed(0)
    B=[random.randint(0,10**7) for i in range (2**20)]
    print("The unsorted array of B[0:5]: ")
    print()
    print(B[0:5])
    print()
    print("The unsorted array of B[10000:10005]: ")
    print()
    print(B[10000:10005])
    print()
    print("The sorted array of B[0:5]: ")
    print()
    mergesort(B)
    print(B[0:5])
    print()
    print("The sorted array of B[10000:10005]: ")
    print()
    print(B[10000:10005])
    print()


main()
