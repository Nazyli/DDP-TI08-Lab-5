print("NIM\t\t : 0110220045")
print("Nama\t :Evry Nazyli Ciptanto")
print("Program Studi Teknik Informatika\n")

def cetak_nama(nama=''):
  # Tulis kode fungsi cetak_nama di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # buat kondisi jika nama string kosong
  if(nama == ''):
    # tampilkan pesan tidak ada yg dicetak
    print('Tidak ada nama yang dicetak')
  # jika nama ada nilai nya
  else:
    i = 0 #mengatur perulangan dari index-0
    # membuat perulangan
    while (i < len(nama)): 
      i = i+1 #mendapatkan kata awalan
      # menampilkan per kata sesuai panjang i
      print(nama[0:i])

def hitung_kesamaan(kata1, kata2):
  # Tulis kode fungsi hitung_kesamaan di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # membuat kondisi perulangan, diambil dari panjang kata yang paling pendek
  lengChar = len(kata1) if len(kata1) <= len(kata2) else len(kata2)
  sama = 0; #set awalan persamaan kata bernilai 0
  # melakukan perulangan dengan for sesuai panjang lengchar
  for i in range (lengChar):
    # membuat kondisi yg memiliki kesamaan posisi dan nilai karakter
    if(kata1[i] == kata2[i]):
      # jika kondisi terpenuhi sama increment 1
      sama = sama + 1
  # mengambalikan nilai total sama
  return sama

def hitung(bil1, bil2, operator='+'):
  # Tulis kode fungsi hitung() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # membuat kondisi jika operator -
  if(operator == '-'):
    # melakukan pengurangan dan mengembalikan nilai
    return bil1 - bil2
  # membuat kondisi jika operator *
  elif operator == '*':
    # melakukan perkalian dan mengambalikan nilai 
    return bil1 * bil2
  else: #kondisi default
    # melakukan pertambahan dan mengambalikan nilai
    return bil1 + bil2


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

if __name__ == '__main__':
  test()