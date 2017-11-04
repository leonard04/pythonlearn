def binarySearch(list,val):
	first=0
	last=len(list)-1
	found=False
	while first<=last and not found:
		middle=(first+last)/2
		if list[middle]==val:
			found=True
		else:
			if val<list[middle]:
				last=middle-1
			else:
				last=middle+1
	return found

data = [3,2,4,5,9,1,9,23,76,85,22,99,11]
val = int(input("masukkan data yang ingin anda cari: "))
print "data array:",data
binarySearch(data,val)