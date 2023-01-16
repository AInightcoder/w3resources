def tekshirish(num, num2):

 for i in range(len(num)):
   for j in range(i+1, len(num)):
    if num[i]+num[j]==num2:
      return True
 return False     

print(tekshirish([2,6,0,8],15))

