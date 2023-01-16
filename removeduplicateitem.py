def removeduplicate(list):
  new =[]
  for i in list:
    if i not in  new:
      new.append(i) 
  return new    

lists=[2,5,6,2,8,9,5,7]
print(removeduplicate(lists))  