import json

jumBarang = int(input("Masukkan jumlah barang = "))

barang = []

jumHarga = 0

for i in range(jumBarang):
    nama_barang = input("Nama barang {}: ".format(i+1))
    harga = int(input("Harga barang {}: ".format(i+1)))
    jumHarga += harga
    barang.append({'nama': nama_barang, 'harga': harga})

data = {'total': jumHarga, 'barang': barang}

with open('data.json', 'w') as file:
    json.dump(data,file,indent=4)