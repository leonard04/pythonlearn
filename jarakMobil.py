t = 1
v0 = float(input("kecepatan mula-mula: "))
a = float(input("percepatan: "))

while (t<11):
	print "t    = ",t,"s"
	s = (v0*t) + ((a*t*t)/2)
	print "S(t) = ",s,"m"
	t+=1

print ""
print "===================================="
print "=======created by ignasiusleo======="
print "===================================="