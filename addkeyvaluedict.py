import operator
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

new = list(dic1.items())
new1 = list(dic2.items())
new3 = list(dic3.items())
new4 = new+new1+new3

print(dict(new4)) 

new5={}
for d in (dic1, dic2, dic3): 
   new5.update(d)
print(new5)   
