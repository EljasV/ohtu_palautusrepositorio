from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


class Pelitehdas:
    def tee_peli(self, vaihtoehto):
        pelivaihtoehdot = {
            "a": KPSPelaajaVsPelaaja,
            "b": KPSTekoaly,
            "c": KPSParempiTekoaly
        }

        if vaihtoehto not in pelivaihtoehdot.keys():
            return None

        return pelivaihtoehdot[vaihtoehto]()
