# Openstack_Microstack_Jischak
Microstack merupakan platform yang disediakan Canonical untuk memudahkan pemasangan Openstack pada Ubuntu.

# Minimal spesifikasi perangkat untuk pemasangan Microstack
- RAM: 4GB (Rekomendasi 8GB)
- HDD: 100 GB
- CPU: 2 core

# Pemasangan Microstack
Sebelum pemasangan pastikan program "snap" sudah terpasang pada PC atau server. 
Lebih jelas mengenai proses pemasangan dapat mengujungi link berikut ini: https://ubuntu.com/openstack/install.
Pada link tersebut terdapat 3 pilihan pemasangan Openstack. Saya memilih pemasangan Multi-Node seusai dengan kebutuhan
untuk membuat beberapa cluster. Saya menyediakan 3 server dengan masing-masing spesifikasinya sebagai berikut:
- OS: Ubuntu Server 18.04.4
- RAM: 4GB
- HDD: 100GB
- CPU: 2 core

# Layanan-layanan Openstack pada Microstack
Layanan/service Openstack yang didapatkan setelah pemasangan microstack. 
1. Keystone: Layanan identitas
2. Glance: Layanan image
3. Neutron: Layanan Jaringan
4. Nova: Layanan Komputasi
5. Placement

Layanan-layanan Openstack yang tidak tercantum diatas, dapat dipasang secara manual.
Dengan catatan, memperhatikan layanan-layanan yang hanya tersedia pada microstack 
di link berikut ini: https://microstack.run/.

# Direktori Openstack pada Microstack
File-file konfigurasi Openstack terdapat pada: /var/snap/microstack/common/etc

# File-file penting pada Openstack:
1) File untuk otentikasi agar pengguna dapat masuk ke Openstack: microstack.rc

Lokasi: /var/snap/microstack/common/etc/microstack.rc

2) File-file image yang diupload (create) ke repositiry glance

Lokasi: /var/snap/microstack/common/lib/images








