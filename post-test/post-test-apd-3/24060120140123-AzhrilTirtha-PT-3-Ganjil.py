# Program Pembayaran Biaya Langganan Aplikasi Musik
# NIM Ganjil

nama_asli = "Azhril Tirtha"
nim_asli = "24060120140123"   # ganti sesuai data diri Anda

nama_input = input("Masukkan Nama: ")
nim_input = input("Masukkan NIM: ")

if nama_input == nama_asli and nim_input == nim_asli:
    print("\n=== Login Berhasil ===")
    print("Opsi Paket Langganan Musik Rp 1.500.000:")
    print("1. Bronze  - Admin 1% | Akses dasar lagu populer")
    print("2. Silver  - Admin 3% | Lagu premium + playlist kustom")
    print("3. Gold    - Admin 5% | Premium + playlist kustom + offline")
    print("4. Platinum- Admin 7% | Semua fitur + eksklusif artis")

    pilihan_paket = input("Pilih paket (1/2/3/4): ")

    biaya_langganan = 1500000
    biaya_admin = 0
    keuntungan = ""

    if pilihan_paket == "1":
        biaya_admin = 0.01
        keuntungan = "Akses dasar ke lagu-lagu populer"
    elif pilihan_paket == "2":
        biaya_admin = 0.03
        keuntungan = "Akses lagu premium dan playlist kustom"
    elif pilihan_paket == "3":
        biaya_admin = 0.05
        keuntungan = "Akses lagu premium, playlist kustom, dan mode offline"
    elif pilihan_paket == "4":
        biaya_admin = 0.07
        keuntungan = "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"
    else:
        print("Pilihan tidak valid.")
        exit()

    total_bayar = biaya_langganan + (biaya_langganan * biaya_admin)

    print("\n=== Rincian Pembayaran ===")
    print("Biaya Langganan : Rp", biaya_langganan)
    print("Biaya Admin     :", int(biaya_admin * 100), "%")
    print("Total Bayar     : Rp", int(total_bayar))
    print("Keuntungan Paket:", keuntungan)

else:
    print("\nLogin Gagal! Nama atau NIM salah.")
