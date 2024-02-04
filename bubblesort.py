import math
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]    
    return
    
arr=[1,4,3,7,2]
bubble_sort(arr)
print(arr)

# first loop is for doing it n times, and other loop is to bring each bubble up
