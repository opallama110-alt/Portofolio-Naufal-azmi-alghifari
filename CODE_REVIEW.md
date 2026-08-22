# Usulan Tugas Hasil Tinjauan Codebase

Tinjauan ini berfokus pada halaman produksi `index.html`. Berkas
`stitch_naufal_azmi_developer_portfolio/code.html` tampak sebagai artefak hasil
ekspor/desain, bukan entry point situs.

## 1. Salah ketik: betulkan kapitalisasi merek GitHub

**Temuan:** Tautan footer menampilkan `Github`, sedangkan nama merek yang benar
dan judul tautan sosial lain di halaman yang sama menggunakan `GitHub`.

**Tugas:** Ubah label footer `Github` menjadi `GitHub` dan periksa seluruh teks
yang terlihat oleh pengguna agar kapitalisasi nama produk konsisten.

**Kriteria penerimaan:**

- Tidak ada lagi teks pengguna `Github` di entry point.
- URL profil dan atribut aksesibilitas yang sudah benar tidak berubah.

## 2. Bug: buat tombol Download CV benar-benar mengunduh CV

**Temuan:** Tombol `Download CV` saat ini memiliki `href="#contact"`, sehingga
klik hanya menggulir halaman ke bagian kontak dan tidak mengunduh berkas apa pun.

**Tugas:** Tambahkan berkas CV yang memang boleh dipublikasikan ke aset situs,
arahkan tautan ke berkas tersebut, dan gunakan atribut `download` dengan nama
berkas yang bermakna. Jika CV belum tersedia, ganti label tombol agar tidak
menjanjikan aksi unduh.

**Kriteria penerimaan:**

- Klik tombol mengunduh/membuka CV yang valid, bukan berpindah ke `#contact`.
- Jalur aset tetap berfungsi saat situs disajikan dari direktori lokal maupun
  static hosting.
- Tautan dapat digunakan dengan keyboard dan mempunyai nama yang jelas bagi
  pembaca layar.

## 3. Dokumentasi: selaraskan spesifikasi radius dengan konfigurasi Tailwind

**Temuan:** `DESIGN.md` menetapkan `DEFAULT: 0.25rem`, `lg: 0.5rem`, dan
`xl: 0.75rem`, tetapi konfigurasi Tailwind entry point menetapkan nilai yang
berbeda (`DEFAULT: 0.125rem`, `lg: 0.25rem`, dan `xl: 0.5rem`). Dokumentasi juga
menyebut kartu memakai radius 8 px, sementara markup kartu memakai
`rounded-3xl` (1.5 rem pada konfigurasi saat ini).

**Tugas:** Tentukan satu sumber kebenaran untuk radius, lalu perbarui
`DESIGN.md` dan konfigurasi/kelas komponen agar token serta contoh penggunaan
sesuai. Dokumentasikan dengan jelas bila kartu proyek sengaja menjadi
pengecualian dari aturan umum.

**Kriteria penerimaan:**

- Nilai token radius dalam dokumentasi sama dengan konfigurasi yang dijalankan.
- Panduan komponen menyebut kelas/radius yang benar-benar dipakai kartu,
  tombol, dan input.
- Pemeriksaan manual pada viewport desktop dan seluler memastikan perubahan
  tidak merusak hierarki visual.

## 4. Pengujian: tambahkan smoke test otomatis untuk kontrak halaman statis

**Temuan:** Repositori belum memiliki manifest test, direktori test, atau
workflow pemeriksaan otomatis. Perilaku penting seperti menu seluler, scroll
spy, anchor internal, tautan eksternal, dan tombol CV karena itu mudah mengalami
regresi tanpa terdeteksi.

**Tugas:** Tambahkan test runner ringan (misalnya Playwright) dan CI yang
menyajikan `index.html`, lalu menguji kontrak utama halaman.

**Kriteria penerimaan:**

- Test memastikan setiap `href="#..."` menunjuk ke ID yang ada dan semua ID
  unik.
- Test membuka menu seluler, memastikan status tampil/sembunyi dan atribut
  `aria-expanded` ikut berubah, lalu memastikan menu tertutup setelah navigasi.
- Test memastikan tautan `target="_blank"` mempunyai `rel="noopener noreferrer"`.
- Test memastikan aksi `Download CV` mengarah ke aset yang tersedia dan bukan
  anchor bagian lain.
- Test dijalankan pada setiap pull request dan menyediakan satu perintah lokal
  yang terdokumentasi.
