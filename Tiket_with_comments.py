try: #Perintah untuk menguji kode blok
	with open("database.txt", "x") as file: #Membuka file dengan mode x (membuat file baru)
		file.write("admin,admin") #Menulis isi file
except FileExistsError: #Perintah untuk menangani eror jika file yang dibuat telah tersedia
	None #Jika file yang dibuat sudah tersedia maka file tersebut tidak akan dibuat lagi
	

def signin(username, password): #Fungsi masuk
	id = False #Mengatur variabel menjadi False
	pw = False 

	with open("database.txt", "r") as file:
		for i in file: #Membuat perulangan dengan range berupa isi dari file
			a,b = i.split(",") #variabel 'a' dan 'b' sama dengan isi dari file yang dipisahkan oleh tanda koma 
			b = b.strip() #Menghapus spasi setelah variabel 'b'

			if a == username and b == password: #kondisi jika username dan password terdapat pada file
				id = True #variabel yang awalnya bernilai false akan berubah menjadi nilai true
				pw = True 
				break #Menghentikan perulangan for

			elif a == username and b != password: #Kondisi jika password salah / tidak ada di dalam file
				id = True #Variabel yang awalnya bernilai False akan berubah menjadi nilai True
				pw = False #Variabel tetap bernilai False
				print("\n" + "Password salah, silahkan masukkan ulang")
				break #Menghentikan perulangan for

	if id and pw: #Kondisi jika variabel 'id' dan 'pw' bernilai True
		return True #Akan mengembalikan nilai True
	
	elif id and pw == False: #kondisi jika variabel id bernilai True dan pw bernilai False
		return False #Akan mengembalikan nilai False
	
	else: #Kondisi jika ekpresi yang diberikan oleh if dan elif tidak terpenuhi
		print("\n" + "Username tidak ditemukan, silahkan membuat akun baru")
		return False #Akan mengembalikan nilai False

def signup(username, password): #Fungsi membuat akun
	id = False #Mengatur variabel menjadi False

	with open("database.txt", "r") as file:
		for i in file:
			a,b = i.split(",")
			b = b.strip()

			if a == username: #Kondisi jika username ada di dalam file
				id = True #Variabel yang awalnya bernilai False akan berubah menjadi nilai True
				print("\n" + "Username telah dipakai")
				break #Menghentikan perulangan for

	if id == False: #Kondisi jika variabel 'id' bernilai False
		file = open("database.txt", "a")
		file.write("\n" + username + "," + password) #username dan password akan disimpan kedalam file(database)
		print("\n" + "Akun telah berhasil di buat")	

from getpass import getpass #Mengimport modul getpass dari paket bernama getpass
#Modul di atas berfungsi untuk menyembunyikan input

while True: #Perulangan yang akan terus berjalan jika tidak ada kondisi yang menghentikannya
		print("\n" + "~"*114)
		print(" "*50 + "Selamat Datang" + " "*50)
		print("~"*114)
		print("\nSebelum masuk ke aplikasi, anda perlu login terlebih dahulu")
		print("Jika anda belum memiliki akun, silahkan membuatnya terlebih dahulu")
		print("\n" + "1. Masuk")
		print("2. Buat Akun" + "\n")

		pilihan = input("Masukkan pilihan (1/2): ")
		
		print("\n" + "~"*114)

		if pilihan == '1': #Kondisi jika input '1' diberikan
			print("~"*51, "Menu Masuk", "~"*51 + "\n")

			#Inputan untuk memasukkan username dan password
			username = input("Masukkan Username: ") 
			password = getpass("Masukkan Password: ")

			if signin(username, password) == True: #Kondisi jika fungsi 'signin' bernilai True
				print("\n" + "~"*49, "Login berhasil", "~"*49)
				break #Perulangan while akan dihentikan

			else:
				continue
		
		elif pilihan == '2': #Kondisi jika input '2' diberikan
			#Inputan untuk memasukkan username dan password
			username = input("\n" + "Masukkan Username: ")
			password = getpass("Masukkan Password: ")

			signup(username, password) #Fungsi 'signup' akan dipanggil

		else: #Kondisi jika iput yang diberikan selain '1' dan '2'
			print("\n" + "Pilihan tidak valid, silahkan ulangi")
			
from datetime import datetime #Mengimport modul datetime dari paket bernama datetime
#Modul datetime berfungsi untuk menangani tanggal dan waktu

class TiketPesawat: #Kelas bernama 'TiketPesawat'
	def __init__(self, asal, destinasi, waktu, biaya): #Konstruktor untuk menginisialisasi objek
		self.penumpang = [] #Atribut penumpang yang memuat list kosong yang nantinya akan diisi saat objek dibuat

		#Atribut di bawah berfungsi untuk mengatur nilai atribut terhadap objek yang sedang dibuat
		self.asal = asal
		self.destinasi = destinasi
		self.waktu = waktu
		self.biaya = biaya

		self.waktu_pemesanan = datetime.now() #Mengatur nilai dari atribut berupa waktu saat objek dibuat

	def tambah_penumpang(self, nama): #Method yang berfungsi untuk menambahkan nama penumpang
		self.penumpang.append(nama) #Menambahkan nama penumpang ke dalam list pada atribut 'penumpang'
	
	def simpan_ke_file(self): #Method yang berfungsi untuk menyimpan ke dalam file saat objek dibuat
		with open ("Tiket.txt", "w") as file:
			file.write(" "*20 + "Informasi Penerbangan"+ "\n")
			file.write("-"*61 + "\n")

			#Yang berada pada kurung kurawal di bawah ({}) itu merujuk pada nilai dari atribut pada objek yang dibuat
			file.write(f"Daerah awal       : {self.asal}" + "\n")
			file.write(f"Daerah Tujuan     : {self.destinasi}" + "\n")
			file.write(f"Waktu penerbangan : {self.waktu}" + "\n")
			file.write(f"Biaya             : Rp. {self.biaya:,.2f}" + "\n")
			file.write("\n")
			file.write(f"Waktu pemesanan   : {self.waktu_pemesanan:%H:%M}" + "\n") #%H merujuk pada jam dan %M merujuk pada menit
			file.write("\n")
			file.write("\n")
			file.write(" "*21 + "Informasi Penumpang"+ "\n")
			file.write("-"*61 + "\n")

			urutan = 0 #Variabel 'urutan' yang memuat angka yang dimulai dari nol

			for penumpang in self.penumpang: #Perulangan dengan range berupa isi dari atribut penumpang
				urutan += 1 #Di setiap perulangan, angka dari variabel 'urutan' akan bertambah 1
				file.write(f"{urutan}. {penumpang}" + "\n") 
				'''Disetiap perulangan, nilai dari variabel urutan dan- 
				elemen dari atribut penumpang akan di tulis ke dalam file'''

def biaya(asal, destinasi, jumlah_penumpang): #Fungsi 'biaya' dengan parameter asal, destinasi, jumlah_penumpang
#Fungsi ini akan menghitung biaya berdasarkan asal dan destinasi yang dipilih saat memberikan input nanti

	harga = [1000000.00, 1250000.00, 1500000.00]

	if asal == '1' and destinasi == '2' or asal == '2' and destinasi == '1': #Kondisi jika 'asal' sama dengan '1' dan 'destinasi sama dengan '1' atau sebaliknya 
		return (harga[1])*jumlah_penumpang #Akan mengembalikan nilai pada indeks 1 dari variabel 'harga' dikali dengan 'jumlah penumpang 
	elif asal == '1' and destinasi == '3' or asal == '3' and destinasi == '1': #Kondisi jika 'asal' sama dengan '1' dan 'destinasi sama dengan '3' atau sebaliknya 
		return (harga[2])*jumlah_penumpang #Akan mengembalikan nilai pada indeks 2 dari variabel 'harga' dikali dengan 'jumlah penumpang 
	elif asal == '2' and destinasi == '3' or asal == '3' and destinasi == '2':  #Kondisi jika 'asal' sama dengan '2' dan 'destinasi sama dengan '3' atau sebaliknya 
		return (harga[0])*jumlah_penumpang #Akan mengembalikan nilai pada indeks 0 dari variabel 'harga' dikali dengan 'jumlah penumpang 


while True: #Perulangan yang akan terus berjalan jika tidak ada kondisi yang menghentikannya
	print("~"*114 + "\n")
	sapaan = (f"Selamat datang, {username}")
	print(sapaan)
	print("~"*len(sapaan), "\n")
	
	penumpang = [] #Variabel yang berisi list kosong
	daerah = ["Balikpapan", "Singapore", "Kuala Lumpur"]
	jam = ["07:00", "13:00", "20:30"]
	urutan = 0 #Variabel 'urutan' yang memuat angka yang dimulai dari nol

	jumlah_penumpang = int(input("Masukkan jumlah penumpang terlebih dahulu: ")) #Inputan untuk memasukkan jumlah penumpang

	print("\n" + "Pilih tempat awal penerbangan:")

	#Perulangan dibawah akan menampilkan tempat awal penerbangan
	for i in daerah: #Perulangan for dengan range berupa isi dari variabel 'daerah'
		urutan += 1 #Variabel 'urutan' bertambah 1 disetiap perulangan
		print(f"{urutan}. {i}") #Variabel 'urutan' dan elemen dari variabel 'daerah' akan di print
		
	urutan = 0 #Variabel 'urutan' akan direset menjadi angka 0 kembali

	asal = input("Masukkan pilihan (dalam bentuk nomor): ") #Inputan untuk memasukkan pilihan dari tempat awal penerbangan

	if asal > str(0) and asal <= str(len(daerah)): #Kondisi jika inputan yang diberikan lebih dari nol dan kurang dari sama dengan jumlah isi pada variabel 'daerah'
		print("\n" + "Pilih destinasi penerbangan:")

		#Perulangan dibawah akan menampilkan destinasi penerbangan
		for i in daerah: #Akan membuat perulangan for dengan range berupa isi dari variabel 'daerah'
			urutan += 1 #Variabel 'urutan' bertambah 1 disetiap perulangan
			print(f"{urutan}. {i}") #Variabel 'urutan' dan elemen dari variabel 'daerah' akan di print

		urutan = 0 #Variabel 'urutan' akan direset menjadi angka 0 kembali

		destinasi = input("Masukkan pilihan (dalam bentuk nomor): ") #Inputan untuk memasukkan pilihan dari destinasi penerbangan

		if destinasi == asal: #Kondisi jika input yang diberikan dari variabel destinasi sama dengan pada variabel asal
			print("Destinasi dan asal tidak boleh sama" + "\n")

		elif destinasi > str(0) and destinasi <= str(len(daerah)): #Kondisi jika inputan yang diberikan lebih dari nol dan kurang dari sama dengan jumlah isi pada variabel 'daerah' 
			print("\n" + "Pilih jam penerbangan:")

			#Perulangan dibawah akan menampilkan destinasi penerbangan
			for i in jam: #Akan membuat perulangan for dengan range berupa isi dari variabel 'jam'
				urutan += 1 #Variabel 'urutan' bertambah 1 disetiap perulangan
				print(f"{urutan}. {i}") #Variabel 'urutan' dan elemen dari variabel 'jam' akan di print

			urutan = 0 #Variabel 'urutan' akan direset menjadi angka 0 kembal

			waktu = input("Masukkan pilihan (dalam bentuk nomor): ") #Inputan untuk memasukkan pilihan dari waktu penerbangan

			if waktu > str(0) and waktu <= str(len(jam)): #Kondisi jika inputan yang diberikan lebih dari nol dan kurang dari sama dengan jumlah isi pada variabel 'jam'  
				print("\n" + f"Biayanya adalah: Rp. {biaya(asal, destinasi, jumlah_penumpang):,.2f}") #Menampilkan total biaya

				pilihan = input("Apakah anda yakin (ya/tidak): ")

				print(" ")

				if pilihan.lower() == "ya": #Kondisi jika inputan yang diberika sama dengan 'ya' 
					
					#Perulangan dibawah berguna untuk memasukkan nama sebanyak jumlah penumpang yang diberikan
					for i in range (0, jumlah_penumpang): #Akan membuat perulangan for dengan range berupa isi dari 0 sampai inputan dari variabel 'jumlah_penumpang'
						urutan += 1 #Variabel 'urutan' bertambah 1 disetiap perulangan
						nama = input(f"Masukkan nama penumpang Ke-{urutan} :  ") #Inputan untuk memasukkan nama
						penumpang.append(nama) #Nama yang telah di input akan dimasukkan ke dalam list pada variabel 'penumpang'
					
					print("\n" + "Tiket anda berhasil dibuat" + "\n")
					print("~"*114 + "\n")

					break

				elif pilihan.lower() == "tidak": #Kondisi jika inputan yang diberikan sama dengan 'tidak'
					continue #Akan kembali ke perulangan while True

				else: #Kondisi jika inputan yang diberikan tidak sesuai dengan kondisi yang ada
					print("Masukkan keyword yang benar" + "\n")

			else:
				print("\n" + "Pilihan tidak valid" + "\n")

		else:
			print("\n" + "Pilihan tidak valid" + "\n")

	else:
		print("\n" + "Pilihan tidak valid" + "\n")

#Variabel yang ada di bawah berfungsi untuk mengubah variabel 'asal', 'destinasi', dan 'waktu' menjadi integer kemudian dikurang 1
#Hal tersebut berfungsi untuk menyesuaikan index dalam pemberian nilai pada objek nanti
index_asal = int(asal) - 1 
index_destinasi = int(destinasi) - 1
index_waktu = int(waktu) - 1

#Di bawah merupakan pembuatan objek dari kelas TiketPesawat / Instasiasi objek
tiket = TiketPesawat(daerah[index_asal], daerah[index_destinasi], jam[index_waktu], biaya(asal, destinasi,jumlah_penumpang))
#Nilai yang diberikan antara lain pada pembuatan objek di atas yait:
#Atribut 'asal' pada kelas TiketPesawat diberi nilai sesuai nilai pada variabel 'daerah' dengan indexnya berupa nilai dari variabel 'index_asal'
#Atribut 'destinasi' pada kelas TiketPesawat diberi nilai sesuai nilai pada variabel 'daerah' dengan indexnya berupa nilai dari variabel 'index_destinasi'
#Atribut 'waktu' pada kelas TiketPesawat diberi nilai sesuai nilai pada variabel 'jam' dengan indexnya berupa nilai dari variabel 'index_waktu'
#Atribut 'biaya' pada kelas TiketPesawat diberi nilai sesuai nilai dari fungsi 'biaya'

jumlah = 0 #Variabel 'jumlah' yang dimulai dari nol
for i in penumpang: #Membuat perulangan dengan range berupa isi dari variabel 'penumpang'
	tiket.tambah_penumpang(penumpang[jumlah]) #Disetiap perulangan, akan memanggil method 'tambah_penumpang' dari objek 'tiket' 
	#(penumpang[jumlah]) Merupakan nilai yang diberikan pada parameter untuk method 'tambah_penumpang' dari objek 'tiket'
	#Nilai yang diberikan pada parameter yaitu berupa nilai pada variabel 'penumpang' dengan indexnya sesuai nilai pada variabel 'jumlah'
	jumlah += 1 #Variabel jumlah akan bertambah 1 disetiap perulangan

tiket.simpan_ke_file() #Memanggil method 'simpan_file' dari objek 'tiket' 

with open ("Tiket.txt", "r") as file:
		print(file.read())
