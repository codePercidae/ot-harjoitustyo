class Kassapaate:

    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti_kateisella(self, maksu):
        return self.syo_kateisella(maksu, 240, True)

    def syo_maukkaasti_kateisella(self, maksu):
        return self.syo_kateisella(maksu, 400, False)
    
    def syo_kateisella(self, maksu, hinta, edullinen):
        if maksu >= hinta:
            self.kassassa_rahaa = self.kassassa_rahaa + hinta
            if edullinen:
                self.edulliset += 1
            else:
                self.maukkaat += 1
            return maksu - hinta
        else:
            return maksu

    def syo_edullisesti_kortilla(self, kortti):
        return self.syo_kortilla(kortti, 240, True)

    def syo_maukkaasti_kortilla(self, kortti):
        return self.syo_kortilla(kortti, 400, False)
    
    def syo_kortilla(self, kortti, hinta, edullinen):
        if kortti.saldo >= hinta:
            kortti.ota_rahaa(hinta)
            if edullinen:
                self.edulliset += 1
            else:
                self.maukkaat += 1
            return True
        else:
            return False
        
    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return