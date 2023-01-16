# list=[4,6,8,9,15,24,156,24]
# all= len(list)
# isx=0
# for x in range(all):
#   isx=(2+isx)%all
#   print(list.pop(isx))
#   all-=1

def removingitem(list):
  xs = 0
  all = len(list)
  while all>0:
    xs = (2+xs)%all
    print(list.pop(xs))
    all-=1
list1=[4,6,8,9,15,24,156,24]    
removingitem(list1)    
