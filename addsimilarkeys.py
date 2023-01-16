def addvaluessimilarkys(dic,dic1):
  
  for k, v in dic.items():
      new={}
      for t, d in dic1.items():
        if k==t:
           new[k]=v+d      
      print(new)        
         
       
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}   
addvaluessimilarkys(d1,d2) 

# second mathod 

from collections import Counter
d = Counter(d1)+Counter(d2)
print(d)

   

