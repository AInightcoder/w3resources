dic = {1:3,4:5,6:8,1:7}
new=[]
for i in dic.items():
  if i not in new:
    new.append(i)
print(dict(new))    


ndic={}
for k, v in dic.items():
   if v not in ndic:
     ndic[k]=v
print(ndic)     