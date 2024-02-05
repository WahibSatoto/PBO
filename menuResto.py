class MenuRestoran:
    def __init__(self):
        self.menu = {
            1: ('Nasi Goreng', 15000),
            2: ('Mie Goreng', 12000),
            3: ('Ayam Goreng', 20000),
            4: ('Soto Ayam', 18000),
            5: ('Es Teh Manis', 5000),
            6: ('Es Jeruk', 6000),
            7: ('Es Campur', 8000)
        }
        self.pesanan = {}

    def pesan_makanan(self):
        print("Menu Restoran:")
        for nomor, (item, harga) in self.menu.items():
            print(f"{nomor}. {item}: Rp. {harga:,.2f}")
        while True:
            try:
                nomor_pesanan = int(input("Masukkan nomor makanan yang ingin dipesan (Ketik '0' untuk selesai): "))
                
                if nomor_pesanan == 0:
                    break

                if nomor_pesanan in self.menu:
                    jumlah = int(input(f"Masukkan jumlah {self.menu[nomor_pesanan][0]}: "))
                    if nomor_pesanan in self.pesanan:
                        self.pesanan[nomor_pesanan] += jumlah
                    else:
                        self.pesanan[nomor_pesanan] = jumlah
                    print(f"{jumlah} {self.menu[nomor_pesanan][0]} ditambahkan ke pesanan.")
                else:
                    print("Nomor makanan tidak ada dalam menu. Silakan coba lagi.")
            except ValueError:
                print("Masukkan nomor makanan yang valid.")

    def hitung_total_pesanan(self):
        total = sum(self.menu[nomor][1] * jumlah for nomor, jumlah in self.pesanan.items())
        return total

    def tampilkan_pesanan(self):
        print("\nPesanan Anda:")
        for nomor, jumlah in self.pesanan.items():
            item, harga = self.menu[nomor]
            print(f"{item}: {jumlah} pcs")
            
    def proses_pembayaran(self):
        total_pesanan = self.hitung_total_pesanan()
        self.tampilkan_pesanan()
        print(f"Total Pesanan Anda: Rp. {total_pesanan:,.2f}")

        while True:
            try:
                jumlah_pembayaran = float(input("Masukkan pembayaran pelanggan: Rp. "))
                if jumlah_pembayaran < total_pesanan:
                    print("Jumlah pembayaran kurang. Silakan masukkan kembali.")
                else:
                    kembalian = jumlah_pembayaran - total_pesanan
                    print(f"\n===========Struct Pembayaran==========")
                    print(f"=============Wahib Resto==============")
                    print(f"------------------------------------------")
                    print("\nPesanan Anda:")
                    self.tampilkan_pesanan()
                    print("\n------------------------------------------")
                    print(f"Jumlah yang dibayarkan Rp{jumlah_pembayaran:,.2f} \nJumlah Kembalian Rp.{kembalian:,.2f}")
                    
                    self.pesanan = {}  # Reset pesanan setelah pembayaran
                    break
            except ValueError:
                print("Masukkan jumlah pembayaran yang valid.")

def main():
    restoran = MenuRestoran()

    while True:
        print("\nMenu Utama:")
        print("1. Pesan Makanan")
        print("2. Tampilkan Pesanan")
        print("3. Pembayaran")
        print("4. Keluar")

        pilihan = input("Masukkan nomor menu yang diinginkan: ")

        if pilihan == '1':
            restoran.pesan_makanan()
        elif pilihan == '2':
            restoran.tampilkan_pesanan()
        elif pilihan == '3':
            restoran.proses_pembayaran()
        elif pilihan == '4':
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
