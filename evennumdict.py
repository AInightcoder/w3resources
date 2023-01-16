dic = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

new = {}
for k, v in dic.items():
   for j in v:
    if j%2==0:
      new.setdefault(k,[]).append(j)
print(new)     

dic['V'][2]=25
print(dic)