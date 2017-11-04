import random
print("daftar pilihan")
print("")
print("1.batu")
print("2.gunting")
print("3.kertas")
print("")

def game_suit():
	pilihan=["batu","gunting","kertas"]
	comchoice=random.choice(pilihan)
	player=int(input("masukkan pilihan: "))
	if player==1:
		print("anda			: batu")
		print "komputer		:",comchoice
		if comchoice=="batu":
			print("\tdraw")
		if comchoice=="gunting":
			print("\tkamu menang")
		if comchoice=="kertas":
			print("\tkamu kalah")
	if player==2:
		print("anda			: gunting")
		print "komputer		:",comchoice
		if comchoice=="batu":
			print("\tanda kalah")
		if comchoice=="gunting":
			print("\tdraw")
		if comchoice=="kertas":
			print("\tkamu menang")
	if player==3:
		print("anda			: kertas")
		print "komputer		:",comchoice
		if comchoice=="batu":
			print("\tkamu menang")
		if comchoice=="gunting":
			print("\tkamu kalah")
		if comchoice=="kertas":
			print("\tdraw")
	if player>=4:
		print "pilihan tidak ada"
game_suit()