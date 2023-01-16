
original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]

new_list=[{k: v for k, v in d.items() if k!='key1'} for d in original_list]
print(new_list)

print("=========================")
newlist=[]
print(len(original_list))
for k in original_list:
  for v in k.items():
   if v[0]!='key1':
    newlist.append(v)
print(newlist)    
