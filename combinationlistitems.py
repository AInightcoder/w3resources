from itertools import combinations
def combinationitems(list1, r):
   
   return list(combinations(list1, r))

list1 = [2,3,5,9,7,4,51]
print(combinationitems(list1,4))   