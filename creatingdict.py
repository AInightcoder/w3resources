d=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
d2=[1, 2, 2, 3]
d3 = [4,5,9,8]

new=[{x:{y:z} for x, y, z in zip(d,d2,d3)}]
print(new)

new2=[{x:y for x,y in zip(d,d2)}]
print(new2)
