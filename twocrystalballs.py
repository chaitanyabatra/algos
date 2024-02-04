import math
def search(arr):
    jump=math.floor(len(arr)**0.5)
    for i in range(0,len(arr),jump):
             if breaks[i]:
                k=i
                break
    
    i-=jump
    for j in range(i,i+jump):
        if breaks[j]:return j
    
breaks=[0]*5+[1]*6
print(search(breaks))

# lo is inclusive , hi is exclusive
