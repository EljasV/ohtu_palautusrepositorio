from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, _):
        return self.tekoaly.anna_siirto()

    def _printtaa_osapuolien_siirrot(self, _, toka_siirto):
        print(f"Tietokone valitsi: {toka_siirto}")
