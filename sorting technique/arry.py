arr=[6,9,2,2,3,4,2]
k=arr[2:4]
print(k)
print(max(arr))
print(min(arr))
kk=sorted(arr)
print(kk)
# j=0
for i in range(len(arr)):
    
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
           arr[j],arr[i]=arr[i],arr[j]
print(arr)
del arr[3] 
print(arr)
