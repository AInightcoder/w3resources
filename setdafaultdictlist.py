def groupdictvalues(dic):
  res ={}
  for k,v  in dic:
    res.setdefault(k,[]).append(v)
  print(res)  

colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
groupdictvalues(colors)