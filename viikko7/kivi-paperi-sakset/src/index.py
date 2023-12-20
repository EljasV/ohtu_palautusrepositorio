from pelitehdas import Pelitehdas


def main():
    tehdas = Pelitehdas()
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = tehdas.tee_peli(vastaus)

        if peli is None:
            break

        peli.pelaa()


if __name__ == "__main__":
    main()
