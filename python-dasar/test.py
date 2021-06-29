# iseng bikin program count
genap = [2, 4, 4, 6, 1, 1, 6, 6, 8, 10, 10]
genap_saring = list(set(genap))
print(genap_saring)
for i in range(len(genap_saring)):
    hasil = genap.count(genap_saring[i])
    print(hasil)


# SOAL 2
a = 21
b = 4

jumlah = a + a
kurang = a - b
kali = a * b
bagi = a / b
print("jika ditambah hasilnya : " + str(jumlah))
print("jika dikurang hasilnya : " + str(kurang))
print("jika dikali hasilnya : " + str(kali))
print("jika dibagi hasilnya : " + str(bagi))
