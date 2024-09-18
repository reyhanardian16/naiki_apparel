1. Penjelasan Checklist
   
   - Membuat proyek django baru
       Dengan membuat direktori baru, menginstall dependencies, dan menghubungkan repositori git lokal dengan github
   - Membuat aplikasi dengan nama main
       Dengan membuat direktori baru main, dan melengkapi file-file yang diperlukan seperti template, urls, dll
   - Melakukan routing pada proyek dengan aplikasi main
       Dengan memodifikasi berkas urls.py
   - Membuat model pada aplikasi main dengan nama Product
       Dengan menambahkan atribut-atribut yang diperlukan seperti name, price, description pada class Product di berkas models.py
   - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
       Dengan melengkapi data-data yang diperlukan oleh template agar dapat ditampilkan pada html
   - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
       Dengan menambahkan isi baru dari url_patterns
   - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
      Dengan melakukan push pada direktori awal, lalu melakukan push terhadap tws agar dapat melakukan deployment
     
2. Penjelasan Request client terhadap aplikasi web yang berbasis django
   
   - Client Request
    Client mengirimkan permintaan HTTP (seperti GET atau POST) untuk mengakses halaman tertentu.
   - urls.py
   Django akan memeriksa pola URL di urls.py untuk menentukan view mana yang akan diaktifkan berdasarkan permintaan URL.
   - views.py    
    View yang sesuai akan dieksekusi, di mana logika aplikasi diproses. Jika diperlukan, view akan mengakses data dari model di models.py.
   - models.py
    Berisi struktur data dan logika untuk berinteraksi dengan database. Jika view memerlukan data, ia akan mengambil atau memanipulasinya melalui model ini.
   - HTML Template
    Setelah data diproses di view, hasilnya akan dimasukkan ke template HTML yang akan dirender menjadi halaman web dinamis yang akan ditampilkan kepada pengguna.
   - Response to Client
    Setelah template dirender, respons HTML dikirim kembali ke client untuk ditampilkan di browser.

![bagan](output.png)


3. Git dalam pengembangan perangkat lunak
   
      Git adalah alat pengontrol versi yang memungkinkan pengembang melacak, menyimpan, dan mengelola perubahan kode secara efisien. Dalam pengembangan perangkat lunak, Git berfungsi untuk memfasilitasi kolaborasi tim dengan mendukung banyak pengembang bekerja secara paralel melalui fitur *branching* dan *merging*. Dengan sistem ini, setiap pengembang dapat membuat cabang sendiri untuk bekerja tanpa mengganggu kode utama, lalu menggabungkannya setelah stabil. Git juga memungkinkan pengelolaan konflik kode, pencatatan perubahan historis, serta menyediakan cadangan otomatis karena sifatnya yang terdistribusi, menjadikannya esensial dalam proyek perangkat lunak.
   
4. Mengapa Django dijadikan permulaan pengerjaan perangkat lunak
   
      Django sering dijadikan permulaan pembelajaran pengembangan perangkat lunak karena sifatnya yang batteries-included, artinya Django menyediakan banyak fitur bawaan yang memudahkan pengembang pemula memulai tanpa harus mencari atau mengonfigurasi banyak alat tambahan. Django memiliki struktur yang jelas dan konvensi yang kuat, yang membantu pemula memahami prinsip-prinsip dasar pengembangan web seperti MVC (Model-View-Controller), manajemen database melalui ORM, serta konsep routing dan template. Selain itu, Django memiliki dokumentasi yang sangat baik dan komunitas yang besar, yang memudahkan pemula mendapatkan bantuan dan contoh kode. Django juga mendukung pengembangan proyek dari kecil hingga besar, sehingga pemula dapat dengan mudah meningkatkan keterampilan mereka seiring pertumbuhan proyek.
   
5. Mengapa model pada django disebut sebagai ORM
   
      Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ini untuk menghubungkan atau memetakan objek dalam kode Python ke tabel dalam basis data relasional. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan objek dan metode Python tanpa harus menulis perintah SQL secara langsung.

6. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

   Data delivery diperlukan dalam pengimplementasian sebuah platform karena platform modern sering kali melibatkan interaksi antar aplikasi atau antar komponen yang berjalan pada berbagai sistem atau perangkat. Data delivery memastikan data yang dikirimkan atau diterima dapat diproses secara efisien dan konsisten oleh komponen-komponen yang berinteraksi tersebut.

7. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

   Antara XML dan JSON, pilihan terbaik tergantung pada kebutuhan spesifik. Namun, secara umum, JSON lebih sering dipilih dalam pengembangan aplikasi modern. Berikut adalah beberapa alasan perbandingan antara keduanya:

   JSON lebih ringkas: JSON menggunakan struktur yang lebih sederhana dan lebih kompak daripada XML. JSON tidak memerlukan penutupan tag seperti XML, sehingga file JSON cenderung lebih kecil.
Mudah dibaca manusia dan mesin: JSON lebih mudah dibaca oleh manusia karena tidak memerlukan tag penutup, dan lebih mudah diproses oleh mesin (khususnya pada aplikasi berbasis web yang menggunakan JavaScript).
Integrasi yang lebih baik dengan JavaScript: JSON sangat sesuai dengan bahasa JavaScript, karena JSON pada dasarnya adalah subset dari sintaksis objek JavaScript. Ini membuatnya sangat populer dalam pengembangan web, terutama pada aplikasi yang menggunakan AJAX.
   Parsing lebih cepat: Parsing JSON umumnya lebih cepat dan lebih efisien dibandingkan XML, karena JSON hanya memiliki satu tipe data (key-value pairs), sementara XML memiliki lebih banyak elemen struktural.
JSON lebih populer karena lebih ringan, cepat, dan memiliki integrasi yang baik dengan teknologi web modern. XML lebih digunakan dalam situasi yang memerlukan validasi data yang lebih kompleks dan lebih formal, seperti dalam aplikasi enterprise atau ketika menggunakan standar seperti SOAP.

8. Fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkannya?

   Method is_valid() pada form Django berfungsi untuk:

   Memvalidasi data form: Method ini memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang ditentukan pada form tersebut (seperti tipe data, batas panjang, format, dll.).
Mengakses data yang divalidasi: Jika validasi berhasil, Django akan menyimpan data yang telah dibersihkan dalam atribut cleaned_data, yang dapat digunakan untuk keperluan selanjutnya (misalnya untuk menyimpan data ke dalam database).
   Menangani error: Jika validasi gagal, Django akan menyimpan informasi mengenai error di atribut errors, sehingga kita dapat memberikan umpan balik kepada pengguna.
Kita membutuhkan method ini untuk memastikan bahwa data yang diterima dari pengguna aman dan sesuai dengan kriteria yang diharapkan sebelum melakukan operasi seperti penyimpanan ke database. Jika tidak, data yang tidak valid atau berbahaya bisa merusak aplikasi atau menyebabkan masalah keamanan.

9. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

   Kita membutuhkan csrf_token saat membuat form di Django untuk mencegah serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang mengirimkan permintaan berbahaya atas nama pengguna tanpa sepengetahuan atau persetujuan mereka. Token CSRF bekerja dengan cara memastikan bahwa permintaan yang diterima oleh server berasal dari sumber yang sah, yaitu dari halaman yang benar-benar diakses oleh pengguna. Penyalahgunaan otorisasi: Serangan CSRF dapat dimanfaatkan untuk melakukan tindakan atas nama pengguna yang sudah login, seperti mengirim pesan atau menghapus data penting, karena server menganggap permintaan tersebut berasal dari pengguna yang sah. Dengan adanya csrf_token, server dan aplikasi dapat memverifikasi bahwa setiap permintaan POST, PUT, atau DELETE berasal dari sumber yang valid, yaitu halaman aplikasi yang dikontrol oleh server tersebut, sehingga serangan CSRF dapat dicegah.

10. Penjelasan checklist tugas 3
   - Membuat input form untuk menambahkan objek model pada app sebelumnya.
     ![ss1](Screenshot 2024-09-18 115203.png)
   - Menambahkan fungsi views
     ![ss2](Screenshot 2024-09-18 115213.png)
   - Membuat routing URL
     ![ss3](Screenshot 2024-09-18 115227.png)

