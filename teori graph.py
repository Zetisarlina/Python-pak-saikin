def temukan_jalur(graf, awal, akhir, jalur=[]):
    jalur = jalur + [awal]
    if awal == akhir:
        return jalur
    if not graf.has_key(awal):
        return None
    for titik in graf[awal]:
        if titik not in jalur:
            jalur_baru = temukan_jalur(graf, titik, akhir, jalur)
            if jalur_baru:
                return jalur_baru
    return None
