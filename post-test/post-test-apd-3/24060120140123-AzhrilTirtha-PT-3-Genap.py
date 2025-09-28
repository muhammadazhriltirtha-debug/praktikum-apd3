# Program Pembayaran Uang Kuliah Tunggal (UKT)
# NIM Genap

nama_asli = "Azhril Tirtha"
nim_asli = "24060120140123"   # ganti sesuai data diri Anda

nama_input = input("Masukkan Nama: ")
nim_input = input("Masukkan NIM: ")

if nama_input == nama_asli and nim_input == nim_asli:
    print("\n=== Login Berhasil ===")
    print("Opsi Pembayaran UKT Rp 6.000.000:")
    print("1. Lunas (1x Bayar) - Biaya Admin 1%")
    print("2. Cicilan 2x - Biaya Admin 5%")
    print("3. Cicilan 4x - Biaya Admin 8%")
    print("4. Cicilan 6x - Biaya Admin 12%")

    pilihan_pembayaran = input("Pilih opsi pembayaran (1/2/3/4): ")

    uang_kuliah = 6000000
    biaya_admin = 0
    jumlah_cicilan = 1

    if pilihan_pembayaran == "1":
        biaya_admin = 0.01
        jumlah_cicilan = 1
    elif pilihan_pembayaran == "2":
        biaya_admin = 0.05
        jumlah_cicilan = 2
    elif pilihan_pembayaran == "3":
        biaya_admin = 0.08
        jumlah_cicilan = 4
    elif pilihan_pembayaran == "4":
        biaya_admin = 0.12
        jumlah_cicilan = 6
    else:
        print("Pilihan tidak valid.")
        exit()

    total_bayar = uang_kuliah + (uang_kuliah * biaya_admin)

    print("\n=== Rincian Pembayaran ===")
    print("UKT Pokok      : Rp", uang_kuliah)
    print("Biaya Admin    :", int(biaya_admin * 100), "%")
    print("Total Bayar    : Rp", int(total_bayar))

    if jumlah_cicilan > 1:
        cicilan_per_periode = total_bayar / jumlah_cicilan
        print("Jumlah Cicilan :", jumlah_cicilan, "x")
        print("Cicilan / Periode : Rp", int(cicilan_per_periode))

else:
    print("\nLogin Gagal! Nama atau NIM salah.")
