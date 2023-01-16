str = "uzbekistanuz"
for i in range(1,len(str)):
  bel=str[0]
  if str[i]==bel:
    text=str.replace(str[i],"$")
print(text)   
     