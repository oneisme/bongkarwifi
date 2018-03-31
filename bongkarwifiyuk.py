# ! / usr / bin / env python
# coding = UTF-8

impor os
socket impor
operator impor
dari impor termcolor berwarna
impor sys
sys.stdout.write ( " \ x1b [8; {rows} ; {cols} t " .format ( baris = 64 , cols = 200 )) # set window ke layar penuh

os.system ( ' cat /root/WifiAttackAutoloaderProject/banner_CrackHead.txt ' )
def  airmon (): # Tidak perlu untuk kelas di sini, hanya satu variabel
    capture_Interface =  str ( raw_input ( " Masukkan ANTARMUKA nirkabel yang ingin Anda tangkap dengan: " ))
    cmd_String =  "  airmon -ng start % s " % capture_Interface
    print berwarna (cmd_String, ' red ' , ' on_white ' )
    os.system (cmd_String)
    # sample Join syntax (bergabung di KIRI)
    # print () "\ n \ t" .join (capture_Interface))
    mon_String =  " mon "
    airodump_String = capture_Interface + mon_String
    cetak berwarna ( ' Antarmuka airodump Anda adalah ... ' , ' merah ' , ' on_white ' )
    print berwarna (airodump_String, ' red ' , ' on_white ' )
    print  " Ingat string ini untuk langkah selanjutnya, AIRODUMP "
    utama()
    kembali



def  airodump ():
    opt_List = [
        ' \ n \ t # 0. Kembali ke Menu Utama ' ,
        ' # 1. PENGUMPULAN INFORMASI, mulai Airodump untuk mencari target yang bagus untuk menyerang ' ,
        ' # 2. TARGETED CAPTURE, ubah parameter Airodump-ng untuk menangkap paket dari router yang ditargetkan '
    ]

    print ( " \ n \ t " .join (opt_List))
    opt_Choice =  str ( raw_input ( " Masukkan OPSI: " ))

    jika opt_Choice ==  " 1 " :
        os.system ( " gnome-terminal -e 'bash -c \" python /root/WifiAttackAutoloaderProject/CrackHead_Recon.py; exec bash \ " ' " )
        airodump ()
    elif opt_Choice ==  " 0 " :
        utama()
    elif opt_Choice ==  " 2 " :
        os.system ( " gnome-terminal -e 'bash -c \" python /root/WifiAttackAutoloaderProject/CrackHead_Targeted.py; exec bash \ " ' " )
        airodump ()


        kembali
    lain :
        cetak berwarna ( ' Anda telah memasukkan pilihan yang tidak valid ' , ' merah ' , ' on_white ' )
        airodump ()
    kembali


def  aireplay ():
    os.system ( " gnome-terminal -e 'bash -c \" python /root/WifiAttackAutoloaderProject/CrackHead_Replay.py; exec bash \ " ' " )
    utama()
    kembali

def  aircrack ():
    os.system ( " gnome-terminal -e 'bash -c \" python /root/WifiAttackAutoloaderProject/CrackHead_Aircrack.py; exec bash \ " ' " )
    utama()
    kembali

def  main ():
    opt_List = [
        ' \ n \ t # 1. AIRMON, mulai antarmuka pengambilan gambar ' ,
        ' # 2. AIRODUMP, mulai memindai titik akses lokal dalam jangkauan dan / atau ambil paket ' ,
        ' # 3. AIREPLAY, kirim paket otorisasi untuk memutuskan klien target dan menangkap jabat tangan 4 arah ' ,
        ' # 4. AIRCRACK, mencoba memecahkan jabat tangan 4 arah dengan daftar kata (serangan kamus) '
    ]

    print ( " \ n \ t " .join (opt_List))
    opt_Choice =  str ( raw_input ( " Masukkan OPSI: " ))

    jika opt_Choice ==  " 1 " :
        os.system ( ' clear ' )
        airmon ()
    elif opt_Choice ==  " 2 " :
        os.system ( ' clear ' )
        airodump ()
    elif opt_Choice ==  " 3 " :
        os.system ( ' clear ' )
        aireplay ()
    elif opt_Choice ==  " 4 " :
        os.system ( ' clear ' )
        aircrack ()
    lain :
        cetak berwarna ( ' Anda telah memasukkan pilihan yang tidak valid ' , ' merah ' , ' on_white ' )
        utama()
    kembali
utama()
