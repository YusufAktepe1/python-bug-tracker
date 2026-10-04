class Gorev:
    # tüm görev ve kayıt türleri için ana sınıf 
    def __init__(self,baslik,aciklama,tarih):
        self.baslik=baslik  
        self.aciklama=aciklama
        self.tarih=tarih
        self.durum = "Bekliyor"

    def bilgi_goster(self):
        # görevin temel bilgileri:
        return f"[{self.durum}] {self.baslik}-{self.tarih}"

class bug_kaydi(Gorev):
    #Görev sınıfından türeyen,hata ve bug'lara özel alt sınıf:
    def __init__(self, baslik, aciklama, tarih,hata_mesaji=""):
        super().__init__(baslik, aciklama, tarih)
        self.hata_mesaji =hata_mesaji
        self.cozum_notu=""
    def cozum_ekle(self,cozum_notu):
        #bug çözüldüğünde çağırılır.
        self.cozum_notu=cozum_notu
        self.durum="Tamamlandı"

    def bilgi_goster(self):
        base_info = super().bilgi_goster()
        return f"[BUG] {base_info} | Hata:{self.hata_mesaji}"