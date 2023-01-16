# list1=['white', 'bleck', 'green', 'red', 'darkblue']
# list2=['green', 'white', 'yellow']
# list3=[]
# num=len(list1)-1
# while num>0:
#      if list1[num] not in list2:
#        list3.append(list1[num]) 
#      num=num-1  
# print(list3)  
# 
def nocolor(list1, list2):
  list3=[]
  num= len(list1)-1 
  while num>0:
    if list1[num] not in list2:
      list3.append(list1[num])
    num=num-1
  return list3
list1=['white', 'bleck', 'green', 'red', 'darkblue']
list2=['green', 'white', 'yellow']
print(nocolor(list1, list2))         