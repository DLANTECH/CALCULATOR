print(''''
==================================================
\t\t    CALCULATOR
==================================================
[#] Author : Muhammad Fadlan Alfian
[#] Program : Kalkulator
[#] Created : 12 Desember 2020
==================================================
1.Penambahan
2.Pengurangan
3.Perkalian
4.Pembagian
''')
pilih = int(input('Pilih Operasi :'))

def main():
	'fitur calculator'
	if pilih == 1:
		print('==========PERTAMBAHAN==========')
		tambah(nilai1 = int(input('Nilai Utama :')),nilai2 = int(input('Nilai Akhir :')))
		
def main2():
	'fitur calculator'
	if pilih == 2:
		print('==========PENGURANGAN==========')
		kurang(nilai1 = int(input('Nilai Utama :')),nilai2 = int(input('Nilai Akhir :')))

		
def main3():
	'fitur calculator'
	if pilih == 3:
		print('==========PERKALIAN==========')
		kali(nilai1 = int(input('Nilai Utama :')),nilai2 = int(input('Nilai Akhir :')))
		
def main4():
	'fitur calculator'
	if pilih == 4:
		print('==========PEMBAGIAN==========')
		bagi(nilai1 = int(input('Nilai Utama :')),nilai2 = int(input('Nilai Akhir :')))

def tambah(nilai1,nilai2):
	print('==========HASIL==========')
	total = nilai1 + nilai2
	print(nilai1,'+',nilai2,'=',total)

def kurang(nilai1,nilai2):
	print('==========HASIL==========')
	total = nilai1 - nilai2
	print(nilai1,'-',nilai2,'=',total)

def kali(nilai1,nilai2):
	print('==========HASIL==========')
	total = nilai1 * nilai2
	print(nilai1,'*',nilai2,'=',total)

def bagi(nilai1,nilai2):
	print('==========HASIL==========')
	total = nilai1 / nilai2
	print(nilai1,'/',nilai2,'=',total)
	
main()
main2()
main3()
main4()
