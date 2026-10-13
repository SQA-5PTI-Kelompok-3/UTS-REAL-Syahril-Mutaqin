TARIF_PER_JAM = 15000
BATAS_JAM_NORMAL = 40
FAKTOR_LEMBUR = 1.5
PENGELUARAN_MINGGUAN = 600000


def hitung_upah(jam):
    if jam < 0:
        raise ValueError("jam kerja tidak boleh negatif")
    lembur = max(0, jam - BATAS_JAM_NORMAL)
    normal = jam - lembur
    return normal * TARIF_PER_JAM + lembur * TARIF_PER_JAM * FAKTOR_LEMBUR


def cek_tabungan(upah, pengeluaran=PENGELUARAN_MINGGUAN):
    if upah > pengeluaran:
        return "bisa menabung", upah - pengeluaran
    elif upah == pengeluaran:
        return "tidak bisa menabung", 0
    return "cari tambahan", 0


if __name__ == "__main__":
    for jam in (52, 41, 40, 30, 0):
        upah = hitung_upah(jam)
        print(jam, upah, cek_tabungan(upah))
