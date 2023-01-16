from itertools import combinations 
def combinationnalues(dic):
  new=[]
  for k, v in dic.items():
      new.append(v)
  print(list(combinations(new,2)))

d = {1:[2,3], 3:[7,9], 4:[8,10]}
combinationnalues(d)


import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
	   