# ! / usr / bin / env python
# coding = UTF-8

impor os
socket impor
operator impor
dari impor termcolor berwarna
impor sys
waktu impor
sys.stdout.write ( " \ x1b [8; {rows} ; {cols} t " .format ( baris = 64 , cols = 200 )) # set window ke layar penuh

os.system ( ' cat /root/WifiAttackAutoloaderProject/autoloaderBanner.txt ' )
print berwarna ( ' Autoloader, ditulis oleh Chang Tan Lister \ n Ditujukan untuk mengurangi kesulitan pengaturan awal Kali Wireless Attack Tools \ n Terima kasih khusus ditujukan kepada pengembang Mana-Toolkit, Fern Wifi Cracker, dan Aircrack Suite ' , ' merah ' , ' on_white ' )
os.system ( ' cat / root / WifiAttackAutoloaderProject / DISCLAIMER ' )

def  step_1_check ():
    step_One =  str ( raw_input ( " Masukkan Kartu Wi-Fi eksternal Anda, lalu ketik LANJUTKAN: " ))
    jika step_One ==  " CONTINUE " :
        step_2_check ()
    lain :
        print berwarna ( ' Silakan ketik LANJUTKAN di semua topi ' , ' merah ' , ' on_white ' )
        step_1_check ()
def  step_2_check ():
    step_Two =  str ( raw_input ( " Menggunakan Kartu Wi-Fi PCI INTERNAL Anda, hubungkan ke sumber uplink internet Anda menggunakan Wicd, lalu ketik LANJUTKAN: " ))
    jika step_Two ==  " CONTINUE " :
        print berwarna ( ' Menghidupkan kembali antarmuka jaringan untuk membawa semua kartu Wi-Fi ke atas ' , ' merah ' , ' on_white ' )
        os.system ( ' /root/WifiAttackAutoloaderProject/bring_Interfaces_Down.sh ' )
        os.system ( ' /root/WifiAttackAutoloaderProject/bring_Interfaces_Up.sh ' )
        print berwarna ( ' Mulai Mana ' , ' merah ' , ' on_white ' )
        # os.system ('/ usr / share / mana-toolkit / run-mana / start-nat-full.sh')
        os.system ( " gnome-terminal -e 'bash -c \" /usr/share/mana-toolkit/run-mana/start-nat-full.sh; exec bash \ " ' " )
        mana_toolkit ()

    lain :
        print berwarna ( ' Silakan ketik LANJUTKAN di semua topi ' , ' merah ' , ' on_white ' )
        step_2_check ()

def  mana_toolkit ():
    opt_List = [
        ' \ n \ t #INSTALL. Instal Prasyarat Mana-Toolkit ' ,
        ' #BANTUAN. Pelajari bagaimana Mana-Tookit berfungsi dan apa yang harus dikonfigurasi di # 1 dan # 2 ' ,
        ' # 1. Konfigurasikan mulai-nat-penuh, ubah file hostapd mana yang akan digunakan, dll ' ,
        ' # 2. Konfigurasikan Pengaturan Mana-Tookit (file hostapd), Ubah Nama BSSID, Alamat MAC, dll ' ,
        ' # 3. Mulai Mana Man-In-The-Middle Attack ' ,
        ' # 4. Buka FireLamb untuk memeriksa Cookies dan Creded Intercepted (saat MANA sedang berjalan) ' ,
        ' # 5. Jalankan TCPDump saat serangan sedang berjalan untuk mulai menangkap paket ' ,
        ' # 999. Restart All Network Interfaces (Jika ada yang salah dengan deteksi kartu wifi di Mana) ' ,
        ' # 0. Kembali ke Menu Utama '
    ]
    print ( " \ n \ t " .join (opt_List))
    opt_Choice =  str ( raw_input ( " Masukkan OPSI: " ))
        # Contoh membuka kode jendela terminal baru dari proyek lain
        # os.system ("gnome-terminal -e 'bash -c \" python /root/ArmsCommander/IDS_flood.py; exec bash \ "'")

    if opt_Choice ==  " INSTALL " :
        os.system ( ' clear ' )
        os.system ( " gnome-terminal -e 'bash -c \" python /root/WifiAttackAutoloaderProject/Mana_Installer.py; exec bash \ " ' " )
        mana_toolkit ()
    elif opt_Choice ==  " 1 " :
        os.system ( " gnome-terminal -e 'bash -c \" nano /usr/share/mana-toolkit/run-mana/start-nat-full.sh; exec bash \ " ' " )
        mana_toolkit ()
    elif opt_Choice ==  " 2 " :
        os.system ( " gnome-terminal -e 'bash -c \" nano /etc/mana-toolkit/hostapd-mana.conf \ " ' " )
        mana_toolkit ()
    elif opt_Choice ==  " 3 " :
        step_1_check ()
    elif opt_Choice ==  " 4 " :
        os.system ( " gnome-terminal -e 'bash -c \" /usr/share/mana-toolkit/run-mana/firelamb-view.sh; exec bash \ " ' " )
    elif opt_Choice ==  " 5 " :
        timestr = time.strftime ( " % Y% m % d -% H% M% S " )
        basic_Filename =  " / root / WifiAttackAutoloaderProject / logs / TCPDump_ "
        modified_Filename = basic_Filename + timestr +  ' .pcap '
        tcp_Dump_String =  " gnome-terminal -e 'bash -c \" sudo tcpdump -i wlan1 -w {0} ; exec bash \ " ' " .format (
            modified_Filename
        )
        os.system (tcp_Dump_String)
    elif opt_Choice ==  " 999 " :
        os.system ( ' /root/WifiAttackAutoloaderProject/bring_Interfaces_Down.sh ' )
        os.system ( ' /root/WifiAttackAutoloaderProject/bring_Interfaces_Up.sh ' )
        mana_toolkit ()
    elif opt_Choice ==  " HELP " :
        os.system ( ' cat /root/WifiAttackAutoloaderProject/HowToConfigureMana.txt ' )
        mana_toolkit ()
    elif opt_Choice ==  " 0 " :
        utama()
    lain :
        cetak berwarna ( ' Anda telah memasukkan pilihan yang tidak valid ' , ' merah ' , ' on_white ' )
        mana_toolkit ()


def  fern_wifi_cracker ():
    opt_List = [
        ' \ n \ t #INSTALL. Instal Fern-Wifi-cracker Prequisites ' ,
        ' # 1. Mulai Fern-Wifi-Cracker ' ,
        ' # 0. Kembali ke Menu Utama '
    ]

    print ( " \ n \ t " .join (opt_List))
    opt_Choice =  str ( raw_input ( " Masukkan OPSI: " ))

    if opt_Choice ==  " INSTALL " :
        cetak berwarna ( ' Memperbarui Repositori APT ' , ' merah ' , ' on_white ' )
        os.system ( ' sudo apt-get update ' )
        print berwarna ( ' Instalasi Fern-Wifi-Cracker ' , ' merah ' , ' on_white ' )
        os.system ( ' sudo apt-get install fern-wifi-cracker ' )
        fern_wifi_cracker ()
    elif opt_Choice ==  " 1 " :
        cetak berwarna ( ' Membawa antarmuka ke bawah dan ke atas untuk memastikan semuanya berfungsi ' , ' merah ' , ' on_white ' )
        os.system ( ' /root/WifiAttackAutoloaderProject/bring_Interfaces_Down.sh ' )
        os.system ( ' /root/WifiAttackAutoloaderProject/bring_Interfaces_Up.sh ' )
        os.system ( ' airmon-ng wlan1 start ' )
        os.system ( ' airodump-ng wlan1mon ' )
        print berwarna ( ' Mulai Fern Wifi Cracker ' , ' merah ' , ' on_white ' )
        os.system ( " gnome-terminal -e 'bash -c \" pakis-wifi-cracker; exec bash \ " ' " )
        utama()
def  aircrack_suite ():
    os.system ( " gnome-terminal -e 'bash -c \" python /root/WifiAttackAutoloaderProject/CrackHead.py; exec bash \ " ' " )
    utama()

def  main ():
    print berwarna ( ' MAIN MENU ' , ' merah ' , ' on_white ' )
    opt_List = [
        ' \ n \ t # 1. Jalankan Mana-Toolkit "Evil Twin" MitM Attacks ' ,
        ' # 2. Jalankan Fern-Wifi-Cracker Suite ' ,
        ' # 3. Jalankan Aircrack Suite '
    ]

    print ( " \ n \ t " .join (opt_List))

    opt_Choice =  str ( raw_input ( " Masukkan OPSI: " ))

    jika opt_Choice ==  " 1 " :
        os.system ( ' clear ' )
        mana_toolkit ()
    elif opt_Choice ==  " 2 " :
        os.system ( ' clear ' )
        fern_wifi_cracker ()
    elif opt_Choice ==  " 3 " :
        os.system ( ' clear ' )
        aircrack_suite ()
    lain :
        cetak berwarna ( ' Anda telah memasukkan pilihan yang tidak valid ' , ' merah ' , ' on_white ' )
        utama()

utama ()
