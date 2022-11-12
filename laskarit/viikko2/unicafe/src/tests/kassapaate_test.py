import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    #Käteisostoon liittyvät testit edullisille lounaille:

    def test_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lounaita_myyty_nolla(self):
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)
    
    def test_edullinen_kateinen_vaihtoraha_toimii_jos_rahaa_riittavasti(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)
    
    def test_edullinen_kateinen_kassaan_tulee_oikea_maara_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(270)

        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_edullinen_kateinen_myytyjen_lounaiden_maara_toimii(self):
        self.kassa.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_liian_vahan_rahaa_ei_myytya_lounasta(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(239), 239)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    #Käteisostoon liittyvät testit maukkaille lounaille:

    def test_maukas_kateinen_vaihtoraha_toimii_jos_rahaa_riittavasti(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(410), 10)
    
    def test_maukas_kateinen_kassaan_tulee_oikea_maara_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(470)

        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_maukas_kateinen_myytyjen_lounaiden_maara_toimii(self):
        self.kassa.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukas_liian_vahan_kateista_ei_myytya_lounasta(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(399), 399)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    #Korttiostoihin liittyvät testit edullisille lounaille

    def test_edullinen_korttilla_osto_toimii(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullinen_kortilla_ostettu_lisää_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_kortilla_osto_ei_toimi_jos_saldoa_ei_tarpeeksi(self):
        kortti = Maksukortti(239)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.39 euroa")

    #Korttiostoihin liittyvät testit maukkaille lounaille

    def test_maukas_korttilla_osto_toimii(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukas_kortilla_ostettu_lisää_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukas_kortilla_osto_ei_toimi_jos_saldoa_ei_tarpeeksi(self):
        kortti = Maksukortti(399)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.99 euroa")

    def test_rahan_lataaminen_kortille_toimii(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 12.00 euroa")

    def test_negatiivisen_summan_lataamisella_kortille_ei_vaikutusta(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

