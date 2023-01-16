import time, datetime


print(time.ctime())


#bu timeni digital shakilda chiqarish

now=datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))