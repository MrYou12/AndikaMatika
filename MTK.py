import os
os.system('clear')
print '\t >>>>>AndikaMatika<<<<<'
print '\t Note:Isi 1 Per 1 Ya:)'
print
print '1.Penjumlahan'
print '2.Pengurangan'
print '3.Perkalian'
print '4.Pembagian'
print '5.Sisa Bagi'
print '6.Pemangkatan'

pilih = input('Pilih Angka : ')

if pilih == 1:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 + angka_2 
	print 'totalnya : ',total
	
elif  pilih == 2:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 - angka_2
	print 'totalnya : ',total
	
elif  pilih == 3:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 * angka_2
	print 'totalnya : ',total
	
elif  pilih == 4:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 / angka_2
	print 'totalnya : ',total
	
elif  pilih == 5:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 % angka_2
	print 'totalnya : ',total
	
elif  pilih == 6:
	print
	angka_1 = input('Angka Pertama : ')
	angka_2 = input('Angka Kedua : ')
	total = angka_1 ** angka_2
	print 'totalnya : ',total