import time

depanJam = 0
jam = 0
depanMenit = 0
menit = 0
depanDetik = 0
detik = 0

if detik == 9:
	detik = 0
	depanDetik += 1

if depanDetik == 6:
	menit +=1
	depanDetik = 0
	detik = 0

if menit == 9:
	menit = 0
	depanMenit += 1   
 
if depanMenit == 6:
	jam +=1
	depanMenit = 0
	menit = 0   

if jam == 9:
	depanJam += 1
	jam = 0

print("{0}{1}:{2}{3}:{4}{5}".format(depanJam,jam,depanMenit,menit,depanDetik,detik), end="\r")