def selectionSort(list):
	for i in range(0,len(list)-1):
		print "Langkah ke-",(i+1)
		firstposition = len(list)-1
		for j in range(len(list)-2,i-1,-1):
			if list[j]<list[firstposition]:
				firstposition = j
		temp=list[i]
		list[i]=list[firstposition]
		list[firstposition]=temp
		print(list)

data = [14,10,6,5,23,2,0,45,21,19,11]
selectionSort(data)