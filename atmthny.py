class ATM:
    def __init__(self):
        self.saldo=0
        self.riwayatMutasi = []
        
    def cekSaldo(self):
        print(f"Saldo anda adalah Rp. {self.saldo:,.2f}")
        
    def tambahUang(self):
        jumlah=float(input("Masukkan jumlah uang yang akan di simpan: Rp."))
                self.riwayatMutasi.append(f"uang masuk +Rp.{jumlah:,.2f}")
def login(users):
    userId = input("Masukkan ID Pengguna: ")
    password = input("Masukkan Password: ")
    
    if userId in users and users[userId] == password:
        return True
    else:
        return False
    
def main():
    users = {"user123":"pass123","user456":"pass456"}
    atm = ATM()
    if login(users):
        while True:
            print("\nSistem Managemen ATM")
            print("1.Cek saldo")
            print("2.Simpan uang")
            
            pilihan = input("Masukkan menu yang anda pilih 1/2/3/4 :")
            
            if pilihan == '1':
                print("Next")
            else:
                return False
    else:
        print("ID Pengguna atau Password salah")