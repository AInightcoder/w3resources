t=(1,2,3)
t1=(4,5,6)
t2=(7,8,9)

t3=tuple(map(sum, zip(t,t1,t2)))

print(t3)