def countprimenumber(dic):
  counter=0
  for k, v in  dic.items():
      for t in v:
        for x in range(2,t):
           if t%x==0 and t%t==0:
              break
        else:
            counter+=1  
  return counter

d = {1:[2,5,6], 2:[9,11,13], 3:[3,4]}
print(countprimenumber(d))

# list = [2,5,9,4]
# counter = 0
# for x in list:
#   for j in range(2,x):
#     if x%j==0 and x%x==0:
#       break
#   else:
#      counter+=1  
# print(counter)      
