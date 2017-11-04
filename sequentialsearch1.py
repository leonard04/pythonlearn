def search(list,value):
	pos=0
	found=False
	while pos<len(list) and not found:
		if list[pos]==value:
			found=True
		else:
			pos+=1
	if found:
		return pos
	else:
		return "data tidak ada"

data = [3,2,4,5,9,1,9,23,76,85,22,99,11]
val = int(input("masukkan data yang ingin anda cari: "))
print "data array:",data
print "data ada di indeks:",search(data,val)