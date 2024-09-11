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
