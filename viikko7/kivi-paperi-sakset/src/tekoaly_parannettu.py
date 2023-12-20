# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def aseta_siirto(self, siirto):
        if self._vapaa_muisti_indeksi == len(self._muisti):
            for i in range(1, len(self._muisti)):
                self._muisti[i - 1] = self._muisti[i]

            self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi - 1

        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1

    def anna_siirto(self):
        if self._vapaa_muisti_indeksi in (0, 1):
            return "k"

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]

        kivien_maara = 0
        papereiden_maara = 0
        saksien_maara = 0

        for i in range(0, self._vapaa_muisti_indeksi - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]

                if seuraava == "k":
                    kivien_maara = kivien_maara + 1
                elif seuraava == "p":
                    papereiden_maara = papereiden_maara + 1
                else:
                    saksien_maara = saksien_maara + 1


        if kivien_maara > papereiden_maara or kivien_maara > saksien_maara:
            return "p"
        if papereiden_maara > kivien_maara or papereiden_maara > saksien_maara:
            return "s"
        return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
