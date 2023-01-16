def additemsinmatrix(list):
   new = []

   for j in range(2):
        new.append(list[0][j]+list[1][j])
   return new   
      

list1=[[2,4],[4,5]]  
print(additemsinmatrix(list1))