def countprimenum(num):
  countre=0

  for x in range(num):

    if x<=1:
       continue
    for i in range(2,x):
      if x%i==0:
        break
    else:
        countre+=1
  print(countre)

countprimenum(5) 
countprimenum(10)    
countprimenum(15) 