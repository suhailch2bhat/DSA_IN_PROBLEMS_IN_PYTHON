# # //// MERSORT
# def mergesort(arr):
#         if len(arr)>1:
#             mid=len(arr)//2
#             L=arr[:mid]
#             R=arr[mid:]
#             mergesort(L)
#             mergesort(R)
#             i=0
#             j=0
#             k=0
#             while i<len(L) and j<len(R):
#                 if L[i]<R[j]:
#                     arr[k]=L[i]
#                     i+=1
#                 else:
#                     arr[k]=R[j]
#                     j+=1
#                 k+=1
#             while i<len(L):
#                 arr[k]=L[i]
#                 i+=1
#                 k+=1
#             while j<len(R):
#                 arr[k]=R[j]
#                 j+=1
#                 k+=1  
# arr=[5,2,1,6,3]            
# mergesort(arr)   
# print(arr,"''''")
# # ////// QUIK SORT
# def quicksort(arr,left,right):
#     if left<right:
#         # left=0
#         # right=len(arr)-1
#         p=partition(arr,left,right)
#         quicksort(arr,left,p-1)
#         quicksort(arr,p+1,right)
# def partition(arr,left,right):
#     lo=left
#     hi=right
#     povit=arr[lo]
#     while lo<hi:
#         while arr[lo]<=povit and lo<=hi :
#             lo+=1
#         while arr[hi]>=povit and lo<=hi:
#             hi-=1
#         if lo<hi:    
#             arr[lo],arr[hi]=arr[hi],arr[lo]        
#     arr[hi],arr[left]=arr[left],arr[hi]
#     return hi
# arr=[8, 7, 2, 1, 0, 9, 6]
# left=0
# right=len(arr)-1
# quicksort(arr,left,right)
# print(arr)
# //////////////insertion sort
# def insersort(arr):
#     for i in range(len(arr)):
#         temp=arr[i]
#         j=i-1
#         while j>=0  and temp<=arr[j]:
#              arr[j+1]=arr[j]
#              j-=1
#         arr[j+1]=temp 
# arr=[8, 7, 2, 1, 0, 9, 6]            
# insersort(arr)
# print(arr)
#///////////////selsetionsort
# arr=[8, 7, 2, 1, 0, 9, 6]   
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]>arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
# print(arr,"()()")            
           
