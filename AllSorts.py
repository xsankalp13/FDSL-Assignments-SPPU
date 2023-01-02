import array


def selectionSort(arr):
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
def bubbleSort(arr):
    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def insertionSort(arr):
    for i in range(n):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp
def shellSort(arr):
    intv = n//2
    while intv>0:
        for i in range(intv,n):
            if arr[i-intv] > arr[i]:
                arr[i-intv],arr[i]=arr[i],arr[i-intv]
        intv = intv//2

def partition(arr,low,high):
    pivot=arr[high]
    i = low -1
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)

        quickSort(arr,low,pi)
        quickSort(arr,pi+1,high)
        




arr = array.array('f',[])

n = int(input("Enter the number of student: "))
for i in range(n):
    per = float(input("Enter the percentage: "))
    arr.append(per)

ch = int(input("\n1.Selection Sort\n2.Bubble Sort\3.Inserstion Sort\n4.Shell Sort\n5.Quick Sort"))

if(ch == 1):
    selectionSort(arr)
elif(ch == 2):
    bubbleSort(arr)
elif(ch==3):
    insertionSort(arr)
elif(ch==4):
    shellSort(arr)
elif(ch==5):
    quickSort(arr,0,n)
