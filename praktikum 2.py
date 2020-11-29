file = open ("d:/data.txt", "r")

# baca baris pertama dari file
# simpan kedalam variabel bil1 sebagai int
bil1 = int(file.readline())

# baca baris pertama dari file
# simpan kedalam variabel bil2 sebagai int
bil2 = int(file.readline())

#hitung dan teampil hasil bagi
try:
    hasil= bil1/bil2
except ZeroDivisionError:
        print('Pembagian dengan nol')
