def findindex(arr, l, low, high):
  if low>=l:
    mid=l+(low-l)//2
    if arr[mid]==high:
      return mid
    elif arr[mid]>high:
      return findindex(arr, l, mid-1, high)
    elif arr[mid]<high:
      return findindex(arr, mid+1, low, high)
  
  return -1 

arr = [4,5,6,8,12,15]
high=8
res=findindex(arr,0, len(arr)-1, high)
if res!=-1:
  print(res)
else:
  print(False)  


print("\U0001F61D")
