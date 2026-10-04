# 💻 DevLog CLI - Geliştirici Günlüğü & Bug Takip Sistemi

Python, SQLite ve Nesne Yönelimli Programlama (OOP) ilkeleri kullanılarak geliştirilmiş, komut satırı (CLI) tabanlı bir geliştirici ve hata takip uygulamasıdır.

## 🚀 Öne Çıkan Özellikler
* **İlişkisel Veritabanı Mimarisi:** `FOREIGN KEY` kısıtlamaları ve `ON DELETE CASCADE` desteğiyle birbirine bağlı `kategoriler` ve `gorevler` tabloları.
* **Nesne Yönelimli Programlama (OOP):** Ortak özellikler için ana `Gorev` sınıfı, özelleştirilmiş alanlar ve davranışlar için `BugKaydi` alt sınıfı (**Inheritance** & **Method Overriding**).
* **Birim Testleri (`unittest`):** Hem model mimarisini hem de bellek içi (`:memory:`) SQLite veritabanı işlemlerini test eden otomatik test süiti.

## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python 3.x
* **Veritabanı:** SQLite3
* **Test Çerçevesi:** Unittest

## ⚙️ Kurulum ve Çalıştırma

1. Projeyi klonlayın veya indirin.
2. Terminalde proje klasörüne gidin:
   ```bash
   cd DevLog