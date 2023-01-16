import os.path , time

lastmodify="%s"%time.ctime(os.path.getmtime('1.py'))
print(lastmodify)
createdtime="%s"%time.ctime(os.path.getctime('1.py'))
print(createdtime)