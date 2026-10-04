import sqlite3


class veritabaniYoneticisi:

    def __init__(self,db_adi="devlog.db"):

        self.db_adi=db_adi
        self.baglanti=None
        self.cursor=None
        self.baglan()
        self.tablolari_olustur()

    def baglan(self):
        #veritabanına baglanma ve foreign key desteğini açma :
        self.baglanti=sqlite3.connect(self.db_adi)
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

    def tablolari_olustur(self):

        #KATEGORİLER TABLOSU:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS kategoriler(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kategori_adi TEXT NOT NULL UNIQUE
            )
        """)        
        #GÖREVLER BUGLAR TABLOSU:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gorevler(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kategori_id INTEGER NOT NULL,
                baslik TEXT NOT NULL,
                aciklama TEXT,
                durum TEXT DEFAULT 'bekliyor',
                cozum_notu TEXT,
                tarih TEXT,
                FOREIGN KEY (kategori_id) REFERENCES kategoriler(id) ON DELETE CASCADE
            )
        """)
        self.baglanti.commit()

    def kategori_ekle(self,kategori_adi):
        #yeni kategori ekleme:
        try:
            self.cursor.execute("INSERT INTO kategoriler (kategori_adi) VALUES (?)",(kategori_adi,))
            self.baglanti.commit()
            return f"Başarılı :{kategori_adi}' kategorisi eklendi"
        except sqlite3.IntegrityError:
            return f"Hata: { kategori_adi} kategorisi zaten mevcut."

    def kategorileri_listele(self):
        #kayıtlı tüm kategorileri getirmek için:
        self.cursor.execute("SELECT id, kategori_adi FROM kategoriler")
        return self.cursor.fetchall()

    def gorev_ekle(self,kategori_id,baslik,aciklama,tarih):
        # seçilen kategoriye yeni bug veya görev kaydı ekleme:
        self.cursor.execute("""
            INSERT INTO gorevler(kategori_id,baslik,aciklama,tarih)
            VALUES(?,?,?,?)
        """,(kategori_id,baslik,aciklama,tarih))
        self.baglanti.commit()
        return "Başarılı : görev/bug sisteme kaydedildi."
    
    def gorevleri_listele(self):
        #görevleri bağlı olduğu kategori ismiyle birlikte listeler.
        self.cursor.execute("""
            SELECT g.id, k.kategori_adi, g.baslik, g.aciklama, g.durum, g.cozum_notu, g.tarih
            FROM gorevler g
            JOIN kategoriler k ON g.kategori_id=k.id
        """) 
        return self.cursor.fetchall()

    def gorev_durum_guncelle(self,gorev_id,yeni_durum,cozum_notu):
        #görev durumu güncelleme ve çözüldüyse çözüm notu kaydetme:
        self.cursor.execute("""
            UPDATE gorevler
            SET durum = ?,cozum_notu = ?
            WHERE id = ?

        """,(yeni_durum,cozum_notu,gorev_id))
        self.baglanti.commit()
        return f"Başarılı: Görev {gorev_id} guncellendi -> {yeni_durum}"