try:
	with open("database.txt", "x") as file:
		file.write("admin,admin")
except FileExistsError:
	None
	

def signin(username, password):
	id = False
	pw = False

	with open("database.txt", "r") as file:
		for i in file:
			a,b = i.split(",")
			b = b.strip()

			if a == username and b == password:
				id = True
				pw = True
				print("\n" + "Login berhasil")
				break

			elif a == username and b != password:
				id = True
				pw = False
				print("\n" + "Password salah, silahkan masukkan ulang")
				break

	if id and pw:
		return True
	
	elif id and pw == False:
		return False
	
	else:
		print("\n" + "Username tidak ditemukan, silahkan membuat akun baru")
		return False

def signup(username, password):
	id = False

	with open("database.txt", "r") as file:
		for i in file:
			a,b = i.split(",")
			b = b.strip()

			if a == username:
				id = True
				print("\n" + "Username telah dipakai")
				break

	if id == False:
		file = open("database.txt", "a")
		file.write("\n" + username + "," + password)
		print("\n" + "Akun telah berhasil di buat")	

from getpass import getpass 

while True:
		print("\n" + "~"*114)
		print(" "*50 + "Selamat Datang" + " "*50)
		print("~"*114)
		print("\nSebelum masuk ke aplikasi, anda perlu login terlebih dahulu")
		print("Jika anda belum memiliki akun, silahkan membuatnya terlebih dahulu")
		print("\n" + "1. Masuk")
		print("2. Buat Akun" + "\n")

		pilihan = input("Masukkan pilihan (1/2): ")
		
		print("\n" + "~"*114)

		if pilihan == '1':
			print("~"*51, "Menu Masuk", "~"*51 + "\n")

			username = input("Masukkan Username: ")
			password = getpass("Masukkan Password: ")
			if signin(username, password) == True:
				print("\n" + "~"*114 + "\n")
				break
		
		elif pilihan == '2':
			username = input("\n" + "Masukkan Username: ")
			password = getpass("Masukkan Password: ")
			signup(username, password)

		else:
			print("\n" + "Pilihan tidak valid, silahkan ulangi")
			
from datetime import datetime

class TiketPesawat:
	def __init__(self, asal, destinasi, waktu, biaya):
		self.penumpang = []
		self.asal = asal
		self.destinasi = destinasi
		self.waktu = waktu
		self.biaya = biaya
		self.waktu_pemesanan = datetime.now()

	def tambah_penumpang(self, nama):
		self.penumpang.append(nama)
	
	def simpan_ke_file(self):
		with open ("Tiket.txt", "w") as file:
			file.write(" "*20 + "Informasi Penerbangan"+ "\n")
			file.write("-"*61 + "\n")
			file.write(f"Daerah awal       : {self.asal}" + "\n")
			file.write(f"Daerah Tujuan     : {self.destinasi}" + "\n")
			file.write(f"Waktu penerbangan : {self.waktu}" + "\n")
			file.write(f"Biaya             : Rp. {self.biaya:,.2f}" + "\n")
			file.write("\n")
			file.write(f"Waktu pemesanan   : {self.waktu_pemesanan:%H:%M}" + "\n")
			file.write("\n")
			file.write("\n")
			file.write(" "*21 + "Informasi Penumpang"+ "\n")
			file.write("-"*61 + "\n")

			urutan = 0

			for penumpang in self.penumpang:
				urutan += 1
				file.write(f"{urutan}. {penumpang}" + "\n")

daerah = ["Balikpapan", "Singapore", "Kuala Lumpur"]
harga = [1000000.00, 1250000.00, 1500000.00]

def biaya():
	if asal == daerah[0] or daerah [1] and destinasi == daerah[0] or daerah [1]:
		return (harga[1])*jumlah_penumpang
	elif asal == daerah[0] or daerah [2] and destinasi == daerah[0] or daerah [2]:
		return (harga[2])*jumlah_penumpang
	elif asal == daerah[1] or daerah [2] and destinasi == daerah[1] or daerah [2]:
		return (harga[0])*jumlah_penumpang

while True:
	print(f"Selamat datang, {username}")
	print("\n")
	
	penumpang = []
	urutan = 0
	jam = ["07:00", "13:00", "20:30"]

	jumlah_penumpang = int(input("Masukkan jumlah penumpang terlebih dahulu: "))

	print("\n" + "Pilih tempat awal penerbangan:")
	for i in daerah:
		urutan += 1
		print(f"{urutan}. {i}")
	urutan = 0
	asal = input("Masukkan pilihan: ")

	if int(asal) <= len(daerah):
		print("\n" + "Pilih destinasi penerbangan:")
		for i in daerah:
			urutan += 1
			print(f"{urutan}. {i}")
		urutan = 0
		destinasi = input("Masukkan pilihan: ")

		if destinasi == asal:
			print("Destinasi dan asal tidak boleh sama")

		elif int(destinasi) <= len(daerah):
			print("\n" + "Pilih jam penerbangan:")
			for i in jam:
				urutan += 1
				print(f"{urutan}. {i}")
			waktu = input("Masukkan pilihan: ")

			if int(waktu) <= len(jam):
				print("\n" + f"Biayanya adalah: Rp. {biaya():,.2f}")

				pilihan = input("Apakah anda yakin (ya/tidak): ")
				print(" ")
				if pilihan.lower() == "ya":
					asal = int(asal) - 1
					destinasi = int(destinasi) - 1
					waktu = int(waktu) - 1

					for i in range (0, jumlah_penumpang):
						nama = input("Masukkan nama penumpang: ")
						penumpang.append(nama)
					print("\n" + "Tiket anda berhasil dibuat" + "\n")
					print("~"*114 + "\n")
					break

				elif pilihan.lower() == "tidak":
					continue

				else:
					print("Masukkan keyword yang benar" + "\n")
			else:
				print("Pilihan tidak valid" + "\n")
		else:
			print("Pilihan tidak valid" + "\n")

	else:
		print("Pilihan tidak valid" + "\n")

jumlah = 0
tiket = TiketPesawat(daerah[asal], daerah[destinasi], jam[waktu], biaya())
for i in range (0, int(jumlah_penumpang)):
	tiket.tambah_penumpang(penumpang[jumlah])
	jumlah += 1
tiket.simpan_ke_file()

with open ("Tiket.txt", "r") as file:
		print(file.read())
