class ATM :
   def __init__ (self):
      self.saldo = 0
      self.mutasi_pembayaran[]

   def uangMasuk(self):
      masuk = float(input("Masukkan jumlah uang yang akan di simpan: "))
      self.saldo + masuk
      self.mutasi_pembayaran.append(f"Uang masuk +Rp.{masuk,.2f}")

   def tarikUang(self):
      keluar = float(input("masukkan jumlah uang yang akan ditarik, pastikan saldo cukup: "))
      if keluar > self.saldo:
         print("saldo tidak mencukupi")
      else:
         self.saldo - keluar
         print(f"Berhasil mengambil uang Rp. {keluar,.2f}, sisa saldo anda {self.saldo,.2f}")
         self.mutasi_pembayaran.append(f"uang keluar -Rp. {keluar,.2f}")

   def cekSaldo(self):
      print(f"saldo anda Rp. {self.saldo,.2f}")

def main():
   users = {"user123":"pass123", "user456":"pass456"}