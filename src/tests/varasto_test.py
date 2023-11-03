import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_alku_tilavuus_alle0(self):
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_alku_saldo_alle0(self):
        v = Varasto(0,-1)
        self.assertAlmostEqual(v.saldo, 0)

    def test_alku_tilavuus_alle0(self):
        v = Varasto(1,2)
        self.assertAlmostEqual(v.saldo, 1)

    def test_lisaa_varastoon_maara_negatiivinen(self):
        self.varasto.lisaa_varastoon(-30)
        self.assertAlmostEqual(self.varasto.saldo,0)

    def test_lisaa_varastoon_maara_liian_suuri(self):
        self.varasto.lisaa_varastoon(30)
        self.assertAlmostEqual(self.varasto.saldo,10)

    def test_ota_varastosta_maara_liian_pieni(self):
        asia = self.varasto.ota_varastosta(-30)
        self.assertAlmostEqual(asia,0.0)

    def test_ota_varastosta_maara_liian_suuri(self):
        asia = self.varasto.ota_varastosta(30)
        self.assertAlmostEqual(asia,0)

    def test_kuvaus_varastosta(self):
        mjono = str(self.varasto)
        vastaus = f"saldo = {0}, vielä tilaa {10}"
        self.assertAlmostEqual(mjono, vastaus)