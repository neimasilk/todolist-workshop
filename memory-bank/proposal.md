# Proposal Proyek: Aplikasi To-Do List dengan Python

## Bab 1: Pendahuluan

### Latar Belakang
Aplikasi to-do list adalah proyek klasik dalam pengembangan perangkat lunak yang mencakup operasi dasar seperti membuat, membaca, memperbarui, dan menghapus (CRUD) data. Proyek ini akan digunakan sebagai studi kasus untuk menerapkan metodologi "Vibe Coding" secara disiplin.

Tujuannya bukan sekadar membuat aplikasi, melainkan untuk membangunnya secara iteratif, dimulai dari versi *command-line interface* (CLI) yang sangat sederhana, lalu secara bertahap menambahkan kompleksitas seperti antarmuka grafis (GUI), hingga kemungkinan menjadi aplikasi web. Pendekatan ini sangat cocok untuk menguji alur kerja kolaborasi manusia-AI yang dianjurkan dalam Vibe Coding.

### Rumusan Masalah
Bagaimana cara menerapkan metodologi Vibe Coding secara efektif untuk mengembangkan sebuah aplikasi dari nol, mulai dari versi paling sederhana hingga menjadi produk yang lebih kompleks dan kaya fitur, sambil memastikan setiap langkah terdokumentasi dengan baik dan kualitas kode tetap terjaga?

### Tujuan Proyek
1.  **Tujuan Utama:** Mengimplementasikan dan mendokumentasikan proses pengembangan aplikasi menggunakan alur kerja Vibe Coding.
2.  **Tujuan Sekunder:** Menghasilkan aplikasi to-do list fungsional berbasis Python dengan beberapa tingkatan kompleksitas (CLI, GUI).
3.  **Tujuan Tersier:** Membangun fondasi kode dan dokumentasi yang dapat dikembangkan lebih lanjut menjadi aplikasi web di masa depan.

---

## Bab 2: Dasar Teori

### Aplikasi To-Do List
Secara fungsional, aplikasi ini akan mengelola daftar tugas. Fitur dasarnya meliputi:
* Menambah tugas baru.
* Melihat semua tugas yang ada.
* Menandai tugas sebagai selesai.
* Menghapus tugas.

Fitur lanjutan yang bisa dikembangkan meliputi:
* Prioritas tugas.
* Tanggal jatuh tempo.
* Pengeditan tugas.
* Penyimpanan data secara persisten (misalnya dalam file JSON atau database).

### Metodologi Vibe Coding
Proyek ini akan sepenuhnya mengadopsi filosofi Vibe Coding, yang menekankan:
* **Manusia sebagai Arsitek Utama:** Perencanaan strategis dilakukan oleh pengembang.
* **AI sebagai Pelaksana:** AI digunakan untuk eksekusi tugas-tugas yang sudah didefinisikan dengan jelas.
* **Konteks adalah Kunci:** Semua informasi proyek disimpan dalam "Memory Bank" yang selalu diperbarui untuk AI.
* **Iterasi "Baby Steps":** Pekerjaan dipecah menjadi tugas-tugas kecil yang dapat diuji.
* **Tes Berkelanjutan:** Setiap langkah kecil harus divalidasi sebelum melanjutkan.

---

## Bab 3: Metodologi dan Rancangan Proyek

### Metodologi Pengembangan
Pengembangan akan mengikuti siklus iteratif yang didefinisikan dalam panduan Vibe Coding, mulai dari Tahap 0 (persiapan), Tahap 1 (setup), hingga Tahap 2 (siklus pengembangan).

### Rancangan Tahapan Proyek
Proyek akan dikembangkan dalam beberapa fase utama:

1.  **Fase 1: MVP (Minimum Viable Product) - CLI Sederhana**
    * **Fitur:** Menambah tugas, menampilkan daftar tugas, dan keluar dari aplikasi.
    * **Teknologi:** Python standar.
    * **Penyimpanan:** Data hanya tersimpan selama aplikasi berjalan (dalam sebuah list atau dictionary).

2.  **Fase 2: Peningkatan CLI & Persistensi Data**
    * **Fitur:** Menandai tugas sebagai selesai, menghapus tugas, dan menyimpan/memuat daftar tugas dari sebuah file (misal: `tasks.json`).
    * **Teknologi:** Python standar dengan modul `json`.

3.  **Fase 3: Transisi ke GUI (Graphical User Interface)**
    * **Fitur:** Semua fungsionalitas dari Fase 2, tetapi disajikan dalam jendela aplikasi grafis.
    * **Teknologi:** Python dengan library `Tkinter` (karena sudah termasuk dalam instalasi standar Python) atau `CustomTkinter` untuk tampilan yang lebih modern.

4.  **Fase 4 (Potensial): Fitur Lanjutan**
    * **Fitur:** Menambahkan prioritas, tanggal jatuh tempo, dan kemampuan untuk mengedit tugas yang sudah ada.
    * **Teknologi:** Pengembangan lebih lanjut dari aplikasi GUI.

### Struktur Proyek
Sesuai panduan, proyek akan memiliki folder `memory-bank` yang berisi semua dokumen perencanaan, termasuk proposal ini, `dokumen-desain-produk.md`, `tumpukan-teknologi.md`, dan dokumen hidup lainnya.