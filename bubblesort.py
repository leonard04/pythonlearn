#!/usr/bin/python

def BubbleSort(val):
	for x in range(len(val)-1,0,-1):
		for i in range(x):
			if val[i]>val[i+1]:
				temp = val[i]
				val[i] = val[i+1]
				val[i+1] = temp

angka = [66,89,15,222,90,17,111,84,12,0,47]
BubbleSort(angka)
print "hasilnya:"
print(angka)