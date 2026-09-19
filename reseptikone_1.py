## RESEPTIKONE
# Tee python-koodi, joka arpoo joka viikolle 7 suosikkireseptiäsi.
# Käytä tyylinä olio-ohjelmointia rakentaen resepteille oma luokka.
# Luokka sisältää reseptin nimen, linkin reseptiin, ruoan tyypin ja kuinka paljon se vie aikaa (min)
# Ruoan tyyppi = herkkuruoka, arkiruoka
# JATKOKEHITYS: parametriksi voisi antaa kasvis, kala, liha (max. 2 lihaa per viikko ja min. 2 kalaa)

# Random-kirjastoa tarvitaan reseptien arpomiseen
import random

class Resepti:
    def __init__(self, ruoka: str, linkki: str | None, tyyppi: str, valmistusaika: int):
        self.ruoka = ruoka
        self.linkki = linkki
        self.tyyppi = tyyppi
        self.valmistusaika = valmistusaika

    # Määritellään str-metodilla, miten vastaus näytetään.
    def __str__(self):
        if self.linkki:
            return(f"{self.ruoka} ({self.valmistusaika} min): {self.linkki}")
        return self.ruoka
    
    # TARVITAANKO TÄTÄ????? MITÄ TÄMÄ __REPR__ MEINASIKAAN?
    def __repr__(self):
        return self.ruoka

## ARPOMINEN (jaetaan useampaan funktioon)
# 1. Tehdään luokka ReseptiKone, johon arpoja tulee.
class ReseptiKone:
    # Luokan Resepti sisältö on listana.
    def __init__(self, reseptit: list [Resepti]):
        self.reseptit = reseptit

    # Erottele arkiruoat herkuista.
    def jaa_tyypin_mukaan(self):
        arki = [resepti for resepti in self.reseptit if resepti.tyyppi == "arkiruoka"]
        herkku = [resepti for resepti in self.reseptit if resepti.tyyppi == "herkku"]
        return arki, herkku
    
    # Yhden viikon arvonta.
    # perättäisillä viikoilla ei saa esiintyä samaa reseptiä kahdesti
    # Viikossa voi olla vain kaksi herkkuruokaa.
    # ehto: ma-pe reseptit eivät saa viedä yli 30 min
    def arvo_viikko(self, kaytetyt):
        # Käytetään kahta koria: arki- ja herkkuruoat.
        arki, herkku = self.jaa_tyypin_mukaan()
        # Katsotaan, onko resepti jo käytetty. Jos ei, lisätään jompaankumpaan koriin.
        arki = [resepti for resepti in arki if resepti not in kaytetyt]
        herkku = [resepti for resepti in herkku if resepti not in kaytetyt]
        # Arvotaan 5 arkiruokaa.
        vk_arkiruoat = random.sample(arki, 5)
        # Ja herkkuruoat
        vk_herkut = random.sample(herkku, 2)

        viikko = vk_arkiruoat + vk_herkut
        # Shufflella sama resepti voi tulla vain kerran.
        random.shuffle(viikko)
        return viikko
    
    def arvo_2_viikkoa(self):
        # Luodaan tyhjä lista käytetyille resepteille.
        kaytetyt = []
        # Arvotaan eka viikko edellä luodulla arvo_viikko-metodilla.
        viikko1 = self.arvo_viikko(kaytetyt)
        # Lisätään käytettyihin resepteihin kaikki viikolle 1 valitut reseptit.
        kaytetyt.extend(viikko1)
        # Arvotaan toinen viikko.
        viikko2 = self.arvo_viikko(kaytetyt)
        return viikko1, viikko2

if __name__ == "__main__":
    # Miten oliot kannattaisi syöttää koneelle fiksummin? Yksi tiedosto, jota voisi päivittää?
    # Ehkä Driveen tästä taulukko?
    mojo = Resepti("Mojo ja perunat", "https://www.meillakotona.fi/reseptit/punainen-kastike-mojo-picon", "arkiruoka", 30)
    tortellini = Resepti("Tortellinipannu", "https://www.instagram.com/p/DPCAegJjPC7/", "arkiruoka", 20)
    nakkikastike = Resepti("Nakkikastike ja muusi", "ulkomuistista", "arkiruoka", 30)
    linssikeitto = Resepti("Linssikeitto", "ulkomuistista", "arkiruoka", 20)
    nachopelti = Resepti("Nachopelti", "https://www.valio.fi/reseptit/nachopelti/", "herkku", 25)
    kreikkalainen_salaatti = Resepti("Kreikkalainen salaatti", "ulkomuistista", "arkiruoka", 15)
    gnocchivuoka = Resepti("Gnocchivuoka", "https://www.valio.fi/reseptit/gnocchi-tuoremakkaravuoka/", "arkiruoka", 30)
    lohikeitto = Resepti("Kylmäsavulohikeitto", "https://yhteishyva.fi/reseptit/kosijan-kylmasavulohikeitto/recipe-22520", "arkiruoka", 30)
    epäruoka = Resepti("Epäruoka eli uunipelti", "ulkomuistista", "arkiruoka", 20)
    nuudelikeitto = Resepti("Maapähkinävoi-nuudelikeitto", "http://valio.fi/reseptit/imanin-ja-leenan-maapahkinavoi-nuudelikeitto/", "arkiruoka", 15)
    pinaattifetapiiras = Resepti("Pinaatti-fetapiirakka ja salaatti", "https://www.meillakotona.fi/reseptit/pinaatti-fetapiirakka", "herkku", 70)
    pizza = Resepti("Pizza", "ulkomuistista", "herkku", 50)
    wolttaa = Resepti("Wolttaa tai käy ulkona", "ei reseptiä", "herkku", 60)
    pinaattikeitto = Resepti("Pinaattikeitto", "pakasteesta", "arkiruoka", 15)
    lasagne = Resepti("Lasagne", "https://www.valio.fi/reseptit/lasagne/", "arkiruoka", 120)
    riisipuuro = Resepti("Riisipuuro", "https://www.martat.fi/reseptit/riisipuuro/", "arkiruoka", 60)
    padthai = Resepti("Pad thai", "https://www.soppa365.fi/reseptit/kala-arjen-nopeat/pad-thai-eli-paistetut-nuudelit", "arkiruoka", 30)
    filee = Resepti("Filee ja perunat", "ulkomuistista", "herkku", 30)
    tonnikalapasta = Resepti("Tonnikalapasta", "https://www.valio.fi/reseptit/tonnikalapasta/", "arkiruoka", 20)
    bouillabaissepasta = Resepti("Bouillabaisse-tuorepasta", "https://www.hs.fi/ruoka/reseptit/art-2000008522713.html", "herkku", 45)
    ribollita = Resepti("Ribollita", "https://www.alko.fi/fi/reseptit/ruokareseptit/ribollita", "arkiruoka", 40)
    tortillat = Resepti("Tortillat", "ulkomuistista", "herkku", 25)
    juustoinen_peurakeitto = Resepti("Juustoinen peurakeitto", "https://www.valio.fi/reseptit/juustoinen-porokeitto/", "arkiruoka", 20)
    katkarapukeitto = Resepti("Thaimaalainen katkarapukeitto", "https://www.soppa365.fi/reseptit/kala-arjen-nopeat/thaimaalainen-katkarapukeitto", "arkiruoka", 30)
    okonomiyaki = Resepti("Okonomiyaki", "https://www.k-ruoka.fi/reseptit/okonomiyaki-eli-japanilainen-kaalipannukakku", "arkiruoka", 60)
    sitruunagnocchit = Resepti("Sitruunagnocchit ja tofu", "https://chocochili.net/2023/03/rapea-mantelitofu-ja-sitruuna-salviagnocchit/", "arkiruoka", 40)
    lihapullat = Resepti("Nonna Giovannan lihapullat", "https://www.k-ruoka.fi/reseptit/nonna-giovannan-italialaiset-lihapullat?gclsrc=aw.ds&utm_source=google&utm_medium=cpc&utm_campaign=10108_K-br%C3%A4ndi_Taktinen_K-Ruoka_Reseptit%20SEA_vk1-52%202025_Jatkuvat&utm_id=1772125894&gad_source=1&gad_campaignid=1772125894&gbraid=0AAAAADrsJv6jMLaf2uM2T2mrdBazLj9Hi&gclid=Cj0KCQjw37nNBhDkARIsAEBGI8PyUGIkcX62dkZjPnqDCBRHAezXvKzn5bv3aihiLLovyaa-icY_770aAtUbEALw_wcB", "arkiruoka", 60)

    reseptit = [
        mojo, tortellini, nakkikastike, linssikeitto, nachopelti,
        kreikkalainen_salaatti, gnocchivuoka, lohikeitto, epäruoka,
        nuudelikeitto, pinaattifetapiiras, pizza, wolttaa,
        pinaattikeitto, lasagne, riisipuuro, padthai, filee,
        tonnikalapasta, bouillabaissepasta, ribollita, tortillat,
        juustoinen_peurakeitto, katkarapukeitto, okonomiyaki,
        sitruunagnocchit
    ]

    kone = ReseptiKone(reseptit)

    viikko1, viikko2 = kone.arvo_2_viikkoa()

    paivat = ["ma", "ti", "ke", "to", "pe", "la", "su"]

    print("VIIKKO 1")
    for paiva, resepti in zip(paivat, viikko1):
        print(paiva, "-", resepti)

    print("\nVIIKKO 2")
    for paiva, resepti in zip(paivat, viikko2):
        print(paiva, "-", resepti)
