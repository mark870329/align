import os
from os import listdir
txtlist = list()
imagelist = list()
removelist = list()
txt = listdir('/home/mark/mark/new_bbox')
images = listdir('/home/mark/mark/png/image_2')
for t in txt:
	txtlist.append(t[:-4])
for i in images:
	imagelist.append(i[:-4])
a1=set(txtlist)
b1=set(imagelist)
remove=(b1.difference(a1))
for r in remove:
	removelist.append(r+'.png')
for item in removelist:
	os.remove('/home/mark/mark/png/image_2/'+item)
