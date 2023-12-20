import kivi_paperi_sakset
import tekoaly_parannettu


class KPSParempiTekoaly(kivi_paperi_sakset.KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = tekoaly_parannettu.TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto

    def _printtaa_osapuolien_siirrot(self, _, toka_siirto):
        print(f"Tietokone valitsi: {toka_siirto}")
