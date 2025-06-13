# Tumpukan Teknologi: Aplikasi To-Do List

Dokumen ini merinci teknologi yang digunakan untuk pengembangan Aplikasi To-Do List, sesuai dengan tahapan proyek yang dijelaskan dalam `dokumen-desain-produk.md`.

## Implementasi Saat Ini: GUI dengan Persistensi Data

*   **Bahasa Pemrograman:** Python (versi 3.x)
    *   **Alasan:** Python adalah bahasa yang serbaguna, mudah dibaca, dan memiliki pustaka standar yang kaya.
*   **Library GUI:** Tkinter
    *   **Alasan:** Tkinter sudah termasuk dalam instalasi standar Python, sehingga tidak memerlukan instalasi tambahan. Ini menjaga proyek tetap ringan dan mudah didistribusikan atau dijalankan di berbagai sistem.
*   **Penyimpanan Data:** File JSON (`tasks.json`)
    *   **Alasan:** Modul `json` adalah bagian dari pustaka standar Python, mudah digunakan untuk serialisasi dan deserialisasi objek Python ke format JSON, yang merupakan format teks yang dapat dibaca manusia dan mudah diparsing. Ini memungkinkan persistensi data antar sesi aplikasi.
*   **Lingkungan Eksekusi:** Lingkungan Desktop (GUI)
*   **Alat Pengembangan (Saran dari Vibe Coding):**
    *   IDE: Cursor (atau IDE lain dengan integrasi AI & Git)
    *   AI Perencana: Gemini (atau serupa)
    *   AI Coding Assistant: Jules (atau serupa, terintegrasi di IDE)
    *   Version Control: Git & GitHub

## Pertimbangan Masa Depan (Potensial)

*   **Peningkatan Tampilan GUI:** Jika tampilan yang lebih modern diinginkan dan penambahan dependensi dianggap dapat diterima, CustomTkinter dapat menjadi pilihan.
*   **Fitur Lanjutan:** Fitur seperti prioritas, tanggal jatuh tempo, dan pengeditan tugas.
*   **Aplikasi Web:** Kemungkinan transisi ke aplikasi berbasis web, melibatkan:
    *   **Backend Web Framework:** Flask atau Django (Python)
    *   **Frontend:** HTML, CSS, JavaScript (mungkin dengan framework seperti React, Vue, atau Svelte)
    *   **Database:** SQLite (untuk kesederhanaan) atau PostgreSQL/MySQL (untuk skala lebih besar)

Dokumen ini akan diperbarui jika ada perubahan atau keputusan teknologi baru selama siklus hidup proyek.
