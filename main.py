from datetime import datetime
from veritabani import  veritabaniYoneticisi
from modeller import bug_kaydi

def ana_menu():
    db =veritabaniYoneticisi()
    while True:
        print("\n" + "="*40)
        print("💻 DEVLOG - GELİŞTİRİCİ GÜNLÜĞÜ & BUG TAKİP")
        print("="*40)
        print("1. Kategori Ekle")
        print("2. Kategorileri Listele")
        print("3. Yeni Görev/Bug Kaydı Ekle")
        print("4. Kayıtları Listele")
        print("5. Görev Durumunu Güncelle (Çözüldü yap)")
        print("6. Çıkış")

        secim = input("\nSeçiminiz (1-6): ").strip()

        if secim == "1":
            k_adi=input("kategori adı (örn: python,SQL,OOP): ").strip()
            sonuc = db.kategori_ekle(k_adi)
            print(sonuc)

        elif secim == "2":
            kategoriler = db.kategorileri_listele()
            print("----MEVCUT KATEGORİLER----")
            if not kategoriler:
                print("Henüz kategori eklenmemiş.")
            else:
                for kat_id,kat_adi in kategoriler:
                    print(f"ID:{kat_id}|kategori: {kat_adi}")
        elif secim == "3":
            kategoriler=db.kategorileri_listele()
            if not kategoriler:
                print("Hata: önce kategori eklemelisiniz!")
                continue
            print("\nKategoriler:")
            for kat_id,kat_adi in kategoriler:
                print(f"ID:{kat_id}|kategori: {kat_adi}")

            try:
                kat_id =int(input("Kategori ID seçin:"))
            except ValueError:
                print("Geçersiz ID formatı!")
                continue


            baslik = input("Görev/Bug Başlığı: ").strip()
            aciklama = input("Detay / Açıklama: ").strip()
            hata_mesaji = input("Varsa Hata Mesaji (Traceback): ").strip()

            # otomatik bug tarihi:
            tarih =datetime.now().strftime("%d.%m.%Y %H:%M")

            # OOP nesnesi:
            yeni_bug =bug_kaydi(baslik,aciklama,tarih,hata_mesaji)

            # veritabanına kaydetme

            sonuc=db.gorev_ekle(kat_id,yeni_bug.baslik,f"{yeni_bug.aciklama}| Hata:{yeni_bug.hata_mesaji}",yeni_bug.tarih)
            print(sonuc)
        elif secim == "4":
            kayitlar =db.gorevleri_listele()
            print("\n--- TÜM GÖREVLER VE BUG'LAR ---")
            if not kayitlar:
                print("kayıt bulunamadı.")
            else:
                for r in kayitlar:
                    # r = (id, kategori_adi, baslik, aciklama, durum, cozum_notu, tarih)
                    print(f"ID:{r[0]} | Kategori: {r[1]} | Durum: [{r[4]}]")
                    print(f"Başlık : {r[2]}")
                    print(f"Detay : {r[3]}")
                    if r[5]:
                        print(f"Çözüm : {r[5]}")
                    print(f"Tarih: {r[6]}")
                    print("-"*35)

        elif secim == "5":
            try:
                g_id = int(input("Güncellenecek Görev/Bug ID: "))     
            except ValueError:
                print("Geçersiz ID!")
                continue

            yeni_durum = input("Yeni Durum (Örn: Tamamlandı / Devam Ediyor): ").strip()
            cozum = input("Çözüm Notu (Eğer çözüldüyse): ").strip()

            sonuc =db.gorev_durum_guncelle(g_id,yeni_durum,cozum)
            print(sonuc)

        elif secim == "6":
            print("uygulama kapatılıyor . kod yazmaya devam!")
            break
        else:
            print("Geçersiz seçim, lütfen 1-6 arasında bir değer girin.")

if __name__ == "__main__":
    ana_menu()