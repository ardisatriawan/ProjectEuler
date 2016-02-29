import time
start_time = time.clock()

def spell(n):
	#dapatkan ratusan, puluhan, satuan
	ratusan = int(n/100)%10
	puluhan = int(n/10)%10
	satuan = n%10
	
	if n == 1000:
		return "onethousand"
	else:
		# Untuk angka ratusan
		if ratusan == 9:
			angkaratusan = "nine"
		elif ratusan == 8:
			angkaratusan = "eight"
		elif ratusan == 7:
			angkaratusan = "seven"
		elif ratusan == 6:
			angkaratusan = "six"
		elif ratusan == 5:
			angkaratusan = "five"
		elif ratusan == 4:
			angkaratusan = "four"
		elif ratusan == 3:
			angkaratusan = "three"
		elif ratusan == 2:
			angkaratusan = "two"
		elif ratusan == 1:
			angkaratusan = "one"
		else:
			angkaratusan = ""
		
		# untuk kata "hundred"
		if ratusan != 0:
			ratus = "hundred"
		else:
			ratus = ""
			
		# untuk kata "and"
		if n >= 100 and n%100 != 0:
			dan = "and"
		else:
			dan = ""
			
		# untuk puluhan, kecuali belasan
		if puluhan == 2:
			angkapuluhan = "twenty"
		elif puluhan == 3:
			angkapuluhan = "thirty"
		elif puluhan == 4:
			angkapuluhan = "forty"
		elif puluhan == 5:
			angkapuluhan = "fifty"
		elif puluhan == 6:
			angkapuluhan = "sixty"
		elif puluhan == 7:
			angkapuluhan = "seventy"
		elif puluhan == 8:
			angkapuluhan = "eighty"
		elif puluhan == 9:
			angkapuluhan = "ninety"
		else:
			angkapuluhan = ""
		
		# untuk satuan, ada dua kasus: belasan dan satuan biasa
		if puluhan == 1: #belasan
			if satuan == 0:
				angkasatuan = "ten"
			elif satuan == 1:
				angkasatuan = "eleven"
			elif satuan == 2:
				angkasatuan = "twelve"
			elif satuan == 3:
				angkasatuan = "thirteen"
			elif satuan == 4:
				angkasatuan = "fourteen"
			elif satuan == 5:
				angkasatuan = "fifteen"
			elif satuan == 6:
				angkasatuan = "sixteen"
			elif satuan == 7:
				angkasatuan = "seventeen"
			elif satuan == 8:
				angkasatuan = "eighteen"
			elif satuan == 9:
				angkasatuan = "nineteen"
		else: #satuan biasa
			if satuan == 9:
				angkasatuan = "nine"
			elif satuan == 8:
				angkasatuan = "eight"
			elif satuan == 7:
				angkasatuan = "seven"
			elif satuan == 6:
				angkasatuan = "six"
			elif satuan == 5:
				angkasatuan = "five"
			elif satuan == 4:
				angkasatuan = "four"
			elif satuan == 3:
				angkasatuan = "three"
			elif satuan == 2:
				angkasatuan = "two"
			elif satuan == 1:
				angkasatuan = "one"
			else:
				angkasatuan =""
		
	return angkaratusan+ratus+dan+angkapuluhan+angkasatuan

length = 0	
for i in xrange (1,1001):
	length += len(spell(i))

print length
print "Running time:", time.clock() - start_time, "seconds"