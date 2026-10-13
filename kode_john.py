jam = 52
tarif = 15000
if jam > 40:
    upah = 40 * tarif + (jam - 40) * tarif * 1.5
else:
    upah = jam * tarif
pengeluaran = 600000
if upah > pengeluaran:
    print("bisa menabung")
    print("tabungan:", upah - pengeluaran)
if upah == pengeluaran:
    print("tidak bisa menabung")
else:
    print("cari tambahan")
