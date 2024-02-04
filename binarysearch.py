
def search(arr,lo,hi,n):
    while lo<hi:
        m=lo+(hi-lo)//2
        v=arr[m]
        if v==n:print(1)
        elif v>n:
            lo=m+1
        else:
            hi=m
    print(0)
search([1,2,3,4,5],0,5,2)

# lo is inclusive , hi is exclusive
