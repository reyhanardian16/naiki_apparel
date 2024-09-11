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
![bagan]()
