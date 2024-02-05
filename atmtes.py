class ATM:
  def __init__(self):
      self.saldo = 0
      self.riwayat_mutasi = []  # Menyimpan riwayat uang masuk dan keluar

  def cek_saldo(self):
      print(f"Saldo Anda saat ini: Rp. {self.saldo:,.2f}")

  def simpan_uang(self):
      jumlah = float(input("Masukkan jumlah uang yang ingin disimpan: Rp. "))
      self.saldo += jumlah
      self.riwayat_mutasi.append(f"Uang Masuk: +Rp. {jumlah:,.2f}")

      print(f"Rp. {jumlah:,.2f} berhasil disimpan. Saldo total Anda sekarang: Rp. {self.saldo:,.2f}")

  def ambil_uang(self):
      jumlah = float(input("Masukkan jumlah uang yang ingin diambil: Rp. "))
      if jumlah > self.saldo:
          print("Saldo tidak mencukupi.")
      else:
          self.saldo -= jumlah
          self.riwayat_mutasi.append(f"Uang Keluar: -Rp. {jumlah:,.2f}")

          print(f"Rp. {jumlah:,.2f} berhasil diambil. Saldo total Anda sekarang: Rp.{self.saldo:,.2f}")

  def mutasi(self):
      print("\nRiwayat Mutasi:")
      for transaksi in self.riwayat_mutasi:
          print(transaksi)

def login(users):
    maxPercobaan = 3
    for _ in range(maxPercobaan):
        user_id = input("Masukkan ID Pengguna: ")
        password = input("Masukkan Kata Sandi: ")

        if user_id in users and users[user_id] == password:
            return True
        else:
            print("ID Pengguna atau Password salah")
    
    print("Akun terkunci, batas percobaan login telah habis")

def main():
  # Contoh daftar pengguna (ID Pengguna: Kata Sandi)
  users = {'user123': 'pass123', 'user456': 'pass456'}

  if login(users):
      atm = ATM()

      while True:
          print("\nMenu ATM:")
          print("1. Cek Saldo")
          print("2. Simpan Uang")
          print("3. Ambil Uang")
          print("4. Mutasi (Riwayat Uang Masuk dan Keluar)")
          print("5. Kembali")
          print("6. Keluar")

          pilihan = input("Masukkan nomor menu yang diinginkan: ")

          if pilihan == '1':
              atm.cek_saldo()
          elif pilihan == '2':
              atm.simpan_uang()
          elif pilihan == '3':
              atm.ambil_uang()
          elif pilihan == '4':
              atm.mutasi()
          elif pilihan == '5':
              continue  # Kembali ke menu utama
          elif pilihan == '6':
              print("Terima kasih. Sampai jumpa!")
              break
          else:
              print("Pilihan tidak valid. Silakan coba lagi.")
  else:

    print("\nSilahkan hubungi petugas!")

        


if __name__ == "__main__":
  main()
