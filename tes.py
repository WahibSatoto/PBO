class ATM:
    def __init__(self):
        self.saldo = 0
        self.riwayatMutasi = []
        
    def cekSaldo(self):
        print(f"Saldo anda saat ini Rp.{self.saldo:,.2f}")
        
    def simpanUang(self):
        jumlah = float(input("Masukkan uang yang ingin di simpan :"))
        self.saldo += jumlah
        self.riwayatMutasi.append(f"Uang masuk :+Rp.{jumlah:,.2f}")
        
    def tarikUang(self):
        jumlah = float(input("Masukkan uang yang ingin di tarik :"))
        if jumlah > self.saldo:
            print(f"Saldo anda tidak mencukupi")
        else:
            self.saldo -= jumlah
            self.riwayatMutasi.append(f"Uang keluar: -Rp.{jumlah:,.2f}")
            
    def mutasi(self):
        for transaksi in self.riwayatMutasi:
            print(transaksi)
            
    def transSama(self):
        rekening = input("Masukkan nomer rekening yang dituju :")
        nominal = float(input("Masukkan nominal yang akan di transfer(Pastikan saldo cukup!): "))
        if nominal > self.saldo :
            print("Maaf saldo anda tidak cukup")
        else:
            self.saldo -= nominal
            print(f"Berhasil transfer ke {rekening} sejumlah {nominal:,.2f}")
            self.riwayatMutasi.append(f"Transfer ke {rekening} sejumlah {nominal:,.2f}")
            
def login(users):
    maxPercobaan = 3
    
    for _ in range(maxPercobaan):
        rekening = input("Masukkan Nomor Rekening Anda :")
        password = input("Masukkan Password :")
        
        if rekening in users and users[rekening] == password:
            return True
        else:
            print("ID Pengguna atau Password salah")
    print(f"Batas percobaan telah habis, akun anda terkunci")
    return False

def main():
    #data user
    users = {'050502':'pass123'}
    atm = ATM()
    if login(users):
        while True :
            print("\nATM Managament System")
            print("Hallo selamat datang di ATM Management System\nSilahkan pilih menu :")
            print("1.Cek Saldo")
            print("2.Simpan Uang")
            print("3.Tarik Uang")
            print("4.Cek Mutasi")
            print("5.Kembali")
            print("6.Keluar")
            
            pilihan = input("Masukkan pilihan anda 1/2/3/4/5/6:")
            
            if pilihan == '1':
                atm.cekSaldo()
            elif pilihan == '2':
                atm.simpanUang()
            elif pilihan == '3':
                atm.tarikUang()
            elif pilihan == '4':
                atm.mutasi()
            elif pilihan == '5':
                while True:
                    print("Menu Pembayaran")
                    print("1.Transfer")
                    print("2.Top-Up")
                    print("3.Kembali")
                    
                    pilih = input("Msukkan menu pilihan :")
                    
                    if pilih == '1':
                        while True:
                            print("1.Transfer Sesama Bank (Biaya admin Rp.0)")
                            print("2.Transfer Bank Lain (Biaya admin Rp.5.000)")
                            print("3.Kembali")
                            pilihTrans = input("Masukkan Pilihan :")
                            
                            if pilihTrans == '1':
                                atm.transSama()
                            elif pilihTrans == '2':
                                atm.transBankLain()
                            elif pilihTrans == '3':
                                continue
                            else:
                                print("Pilihan tidak valid")
                    elif pilih == '2':
                        atm.topup()
                    elif pilih == '3':
                        continue
                    else:
                        print("Pilihan tidak valid. Mohon masukkan pilihan dengan benar")
            elif pilihan == '6':
                print("Terimaksih telah menggunakan ATM Managament System")
                break
            else:
                print("Pilihan anda tidak valid")
    else:
        print("Silahkan hubungi admin")
if __name__ == "__main__":
    main()