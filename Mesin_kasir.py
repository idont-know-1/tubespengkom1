import os

# Tampilkan jenis barang yang tersedia
def tampilkan_menu_utama():
    print('''    | KODE|   JENIS BARANG |
    |  1  | Kosmetik       |
    |  2  | Makanan Ringan |
    |  3  | Pecah Belah    |
    |  4  | Sembako        |
    |  5  | Minuman        |
''')

# Inisialisasi keranjang belanja
keranjang = {}

def tampilkan_keranjang():
    if keranjang:
        print("\nBarang di keranjang:")
        total_harga = 0
        for barang, (jumlah, harga) in keranjang.items():
            print(f"{barang} x {jumlah} = {harga * jumlah}")
            total_harga += harga * jumlah
        print(f"Total belanja: {total_harga}\n")
    else:
        print("\nKeranjang Anda masih kosong.\n")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar
    tampilkan_menu_utama()
    
    tipe_barang = input('Jenis barang apa yang akan anda beli \n(masukkan nomor kode atau ketik selesai untuk mengakhiri transaksi): ').lower()

    if tipe_barang == '1':
        barang_kosmetik = {
            "Masker" : 12000,
            "Bedak"  : 10000,
            "Parfum" : 25000,
            "Shampo" : 3000,
            "Sabun"  : 4000
        }
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar
            for i in barang_kosmetik:
                print('|',i, '\t\t\t|Harga:', barang_kosmetik[i])

            beli_kosmetik = input(f'masukkan nama barang yang akan anda beli\n(atau ketik "kembali" untuk kembali ke menu sebelumnya atau "selesai" untuk mengakhiri program): ').capitalize()
            if beli_kosmetik == 'Kembali':
                break
            elif beli_kosmetik == 'Selesai':
                tampilkan_keranjang()
                print('Terima kasih telah berbelanja di minimarket subur.')
                exit()  # Mengakhiri program
            elif beli_kosmetik not in barang_kosmetik:
                print('Barang tidak ditemukan, masukkan nama barang yang tersedia.')
                input('Tekan Enter untuk melanjutkan...')
                continue
            
            jumlah_kosmetik = int(input('Berapa barang yang akan anda beli: '))
            if beli_kosmetik in keranjang:
                keranjang[beli_kosmetik] = (keranjang[beli_kosmetik][0] + jumlah_kosmetik, barang_kosmetik[beli_kosmetik])
            else:
                keranjang[beli_kosmetik] = (jumlah_kosmetik, barang_kosmetik[beli_kosmetik])
            print(f"{jumlah_kosmetik} {beli_kosmetik} telah ditambahkan ke dalam keranjang.")
            input('Tekan Enter untuk melanjutkan...')

    elif tipe_barang == '2':
        barang_makanan_ringan = {
            "Oreo"  : 12000,
            "Wafer" : 10000,
            "Beter" : 25000,
            "Tango" : 3000,
            "Beng"  : 4000
        }
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar
            for i in barang_makanan_ringan:
                print('|',i, '\t\t\t|Harga:', barang_makanan_ringan[i])

            beli_makanan_ringan = input(f'masukkan nama barang yang akan anda beli\n(atau ketik "kembali" untuk kembali ke menu sebelumnya atau "selesai" untuk mengakhiri program): ').capitalize()
            if beli_makanan_ringan == 'Kembali':
                break
            elif beli_makanan_ringan == 'Selesai':
                tampilkan_keranjang()
                print('Terima kasih telah berbelanja di minimarket subur.')
                exit()  # Mengakhiri program
            elif beli_makanan_ringan not in barang_makanan_ringan:
                print('Barang tidak ditemukan, masukkan nama barang yang tersedia.')
                input('Tekan Enter untuk melanjutkan...')
                continue

            jumlah_makanan_ringan = int(input('Berapa barang yang akan anda beli: '))
            if beli_makanan_ringan in keranjang:
                keranjang[beli_makanan_ringan] = (keranjang[beli_makanan_ringan][0] + jumlah_makanan_ringan, barang_makanan_ringan[beli_makanan_ringan])
            else:
                keranjang[beli_makanan_ringan] = (jumlah_makanan_ringan, barang_makanan_ringan[beli_makanan_ringan])
            print(f"{jumlah_makanan_ringan} {beli_makanan_ringan} telah ditambahkan ke dalam keranjang.")
            input('Tekan Enter untuk melanjutkan...')

    elif tipe_barang == 'selesai':
        tampilkan_keranjang()
        print('Terima kasih telah berbelanja di minimarket subur.')
        break

    else:
        print('Kode invalid, masukkan kode yang sesuai.')
        input('Tekan Enter untuk melanjutkan...')
