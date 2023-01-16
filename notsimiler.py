def toplam(data):
  if len(data)==len(set(data)):
    return True
  else:
     return False
print(toplam([2,39,4,5,5,6]))      