import operator

d = {1:4, 2:1,3:8,4:5}
print(d)

sort_dic=sorted(d.items(), key=operator.itemgetter(1))
print(sort_dic)
sort_dic.reverse()
print(dict(sort_dic))

