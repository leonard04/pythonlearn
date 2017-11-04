import os
import sys

global anak,gajiPokok,gajiKotor,hitungLembur,hitungAnak,persen,total,nama
def pindahHalaman(label):
	global nomor
	nomor = label

def bersihkanLayar():
	os.system('clear')

def keluar():
	sys.exit();

def inputSalah():
	print "input keyboard anda salah"
	ulangi()

def ulangi():
	ulang = raw_input("Do you want to try again? [y/n]")
	if ulang == "y" or ulang == "Y":
		pindahHalaman(0)
		bersihkanLayar()
	elif ulang == "n" or ulang == "N":
		bersihkanLayar()
		keluar()
	else:
		inputSalah()

def rumusHitung():
	anak = 50000
	hitungLembur = jmlLembur * lembur
	if jmlAnak > 3:
		hitungAnak = anak * 3
	else:
		hitungAnak = anak * jmlAnak

	gajiKotor = gajiPokok + hitungLembur + hitungAnak
	persen = gajiKotor * (5 / 100)
	total = gajiKotor - persen

def tampilkan():
	print "===================================="
	print "Aplikasi Gaji Karyawan dengan Python"
	print "===================================="
	print ('| Nama   				: ',nama)
	# print "| NIK   					: ",nik
	# print "| Jabatan   				: ",jabatan
	# print "| Gaji Kotor   			: ",gajiKotor
	# print "| Pajak Penghasilan 5%   : ",persen
	# print ""
	# print "==> Total Gaji yang diterima: ",total
	# print ""

def Main():
	bersihkanLayar()
	print "------------------------------------"
	print "Aplikasi Gaji Karyawan dengan Python"
	print "------------------------------------"
	print ""
	nama = raw_input("Masukkan nama : ")
	# nik = raw_input("Masukkan NIK: ")
	# golongan = raw_input("Masukkan golongan[1.direktur, 2.Manajer, 3.Supervisor, 4.Operator]: ")
	# jmlAnak = raw_input("Masukkan Jumlah anak: ")
	# jmlLembur = raw_input("Masukkan Jumlah jam lembur: ")
		
	print(tampilkan())

		# if golongan == 1:
		# 	nomor = 1
		# elif golongan == 2:
		# 	nomor = 2
		# elif golongan == 3:
		# 	nomor = 3
		# elif golongan == 4:
		# 	nomor = 4
		# else:
		# 	nomor = 0

	# elif nomor == 1:
	# 	jabatan = "Direktur"
	# 	gajiPokok = 8000000
	# 	lembur = 90000
	# 	bersihkanLayar()
	# 	rumusHitung()
	# 	tampilkan()
	# 	ulangi()

	# elif nomor == 2:
	# 	jabatan = "Manager"
	# 	gajiPokok = 5000000
	# 	lembur = 70000
	# 	bersihkanLayar()
	# 	rumusHitung()
	# 	tampilkan()
	# 	ulangi()

	# elif nomor == 3:
	# 	jabatan = "Supervisor"
	# 	gajiPokok = 3500000
	# 	lembur = 60000
	# 	bersihkanLayar()
	# 	rumusHitung()
	# 	tampilkan()
	# 	ulangi()

	# elif nomor == 4:
	# 	jabatan = "Operator"
	# 	gajiPokok = 2500000
	# 	lembur = 50000
	# 	bersihkanLayar()
	# 	rumusHitung()
	# 	tampilkan()
	# 	ulangi()

	# else:
	# 	keluar()

print(Main())