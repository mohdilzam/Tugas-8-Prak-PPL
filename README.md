# 🛍️ Katalog Produk Django

Proyek ini adalah sebuah aplikasi web sederhana yang dibangun menggunakan **Django**. Aplikasi ini menampilkan daftar produk berdasarkan kategori, menampilkan detail produk, serta menyediakan halaman toko dan informasi tentang aplikasi.

---

## 👥 Kelompok 6

- Cut Sula Fhatia Rahma
- Fathiya Namira Fardhi
- Iwani Khairina

---

## 📂 Fitur Utama

- 🔎 Halaman dashboard untuk melihat semua kategori produk
- 📁 Halaman kategori untuk melihat daftar produk per kategori
- 🧾 Halaman detail produk
- 🏪 Halaman toko yang menampilkan semua produk dari toko tertentu
- ℹ️ Halaman "Tentang Kami"

---

## 🧑‍💻 Teknologi yang Digunakan

- [Django 5.2](https://docs.djangoproject.com/en/5.2/)
- [Python 3.11+](https://www.python.org/)
- [Bootstrap 5](https://getbootstrap.com/)

---

##  📁 Struktur Proyek

```
katalog/
├── katalog/              # Konfigurasi utama proyek Django
│   └── urls.py           # Routing URL utama
├── produk/               # Aplikasi utama (produk)
│   ├── templates/
│   │   └── produk/       # Template HTML untuk aplikasi produk
│   ├── static/
│   │   └── produk/       # File statis (CSS, JS, gambar)
│   ├── views.py          # Fungsi-fungsi tampilan (view logic)
│   └── urls.py           # Routing URL untuk aplikasi produk
├── manage.py             # Command-line utility Django
└── db.sqlite3            # Database SQLite (otomatis dibuat)
```

---

## 🚀 Instalasi dan Menjalankan Proyek

1. **Clone repositori ini**
   ```
   git clone https://github.com/csulafr/Tugas-8-PPL.git
   cd katalog-produk
   ```

2. Aktifkan Virtual Environment (opsional tapi direkomendasikan)
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
   
4. Migrate database
   ```
   python manage.py migrate
   ```
   
6. Jalankan server
   ```
   python manage.py runserver
   ```
   
8. Akses aplikasi
   ```
   http://127.0.0.1:8000/
   ```
   
