import unittest
from modeller import Gorev, bug_kaydi
from veritabani import veritabaniYoneticisi

class TestDevLogModeller(unittest.TestCase):
    def test_bug_kaydi_inheritance_ve_override(self):
        """BugKaydi sınıfının Gorev'den kalıtım almasını ve metodun ezilmesini test eder."""
        bug = bug_kaydi("SQL Hatası", "Tablo oluşmuyor", "04.10.2026", "OperationalError")
        
        self.assertEqual(bug.baslik, "SQL Hatası")
        self.assertEqual(bug.durum, "Bekliyor")
        self.assertEqual(bug.hata_mesaji, "OperationalError")
        
        # Method Overriding testi ([BUG] ibaresi ekleniyor mu?)
        gosterim = bug.bilgi_goster()
        self.assertIn("[BUG]", gosterim)
        self.assertIn("OperationalError", gosterim)
        
        # Çözüm ekleme fonksiyonu testi
        cozum_sonuc = bug.cozum_ekle("Syntax hatası düzeltildi")
        self.assertEqual(bug.durum, "Tamamlandı")
        self.assertEqual(bug.cozum_notu, "Syntax hatası düzeltildi")


class TestDevLogVeritabani(unittest.TestCase):
    def setUp(self):
        """Her testten önce gerçek veritabanını bozmamak için RAM'de (:memory:) geçici DB kurar."""
        self.db = veritabaniYoneticisi(":memory:")

    def test_kategori_ekle_ve_listele(self):
        """Kategori ekleme ve listeleme işlemlerini test eder."""
        sonuc = self.db.kategori_ekle("Python")
        self.assertIn("Başarılı", sonuc)
        
        kategoriler = self.db.kategorileri_listele()
        self.assertEqual(len(kategoriler), 1)
        self.assertEqual(kategoriler[0][1], "Python")

    def test_gorev_ekle_ve_join_listeleme(self):
        """Görev ekleme ve JOIN ile kategori adını çekmeyi test eder."""
        self.db.kategori_ekle("SQL")
        kategoriler = self.db.kategorileri_listele()
        kat_id = kategoriler[0][0]
        
        ekleme_sonuc = self.db.gorev_ekle(kat_id, "Tablo Hatası", "UNIQUE eksikti", "04.10.2026")
        self.assertIn("Başarılı", ekleme_sonuc)
        
        gorevler = self.db.gorevleri_listele()
        self.assertEqual(len(gorevler), 1)
        self.assertEqual(gorevler[0][1], "SQL")  # JOIN sayesinde kategori adı geldi
        self.assertEqual(gorevler[0][2], "Tablo Hatası")

    def test_gorev_durum_guncelle(self):
        """Görev durumunun ve çözüm notunun güncellenmesini test eder."""
        self.db.kategori_ekle("OOP")
        kat_id = self.db.kategorileri_listele()[0][0]
        self.db.gorev_ekle(kat_id, "Kalıtım Hatası", "Super eksikti", "04.10.2026")
        
        gorevler = self.db.gorevleri_listele()
        gorev_id = gorevler[0][0]
        
        guncelleme = self.db.gorev_durum_guncelle(gorev_id, "Tamamlandı", "super() eklendi")
        self.assertIn("Başarılı", guncelleme)
        
        guncel_gorevler = self.db.gorevleri_listele()
        self.assertEqual(guncel_gorevler[0][4], "Tamamlandı")  # Durum
        self.assertEqual(guncel_gorevler[0][5], "super() eklendi")  # Çözüm notu

if __name__ == "__main__":
    unittest.main()