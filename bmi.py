tinggi = float(input("masukkan tinggi badan anda dalam cm: "))
tinggiinmeter = float(tinggi/100)
massa = float(input("masukkan berat badan anda dalam kg: "))
bmi = round(massa/(tinggiinmeter * tinggiinmeter),2) #round untuk membulatkan hasil decimal 2 angka di belakang koma
if bmi<18:
	stat = "kurus"
elif bmi>=18 and bmi<23:
	stat = "ideal"
elif bmi>=23 and bmi<27:
	stat = "gemuk"
elif bmi>=27 and bmi<35:
	stat = "obesitas"
else:
	stat = "obesitas morbid"

print("")
print "Body mass Index anda: ",bmi
print "Status anda: ",stat

print ""
print "===================================="
print "=======created by ignasiusleo======="
print "===================================="