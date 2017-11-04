def search(list,value):
	pos=0
	found=False
	stop=False
	while pos<len(list) and not found and not stop:
		if list[pos]==value:
			found=True
		else:
			if list[pos]>value:
				stop=True
			else:
				pos+=1
	if found:
		return pos
	else:
		return "null"

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
val = int(input("masukkan data yang ingin anda cari: "))
print "data array:",data
print "data ada di indeks:",search(data,val)