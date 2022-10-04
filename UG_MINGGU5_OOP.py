import pandas 
from tabulate import tabulate

class KartuKeluarga:
    #KONSTRUKTOR KartuKeluarga
    def __init__(self):
        
        self.anggota = []
        self.dictionary1 = []
        self.dictionary2 = []

    #METHOD UNTUK MENAMBAHKAN ANGGOTA
    def tambah_anggota(self, anggota):
        self.anggota.append(anggota)

    #METHOD UNTUK MENGGANTI ATTRIBUT PEKERJAAAN PADA SALAH SATU DATA
    def ganti_pekerjaan(self, person, mengganti_pekerjaan):
        for i in range(len(self.anggota)):
            if self.anggota[i]['namaLengkap']== person:
                self.dictionary1[i]['pekerjaan'] = mengganti_pekerjaan
                self.anggota[i]['pekerjaan'] = mengganti_pekerjaan

    #METHOD UNTUK MENGGANTI ATTRIBUT SEKOLAH PADA SALAH SATU DATA 
    def ganti_sekolah(self, person, mengganti_sekolah):
        for i in range(len(self.anggota)):
            if self.anggota[i]['namaLengkap']== person:
                self.dictionary1[i]['pendidikan'] = mengganti_sekolah
                self.anggota[i]['pendidikan'] = mengganti_sekolah
    
    #METHOD UNTUK MENGGANTI ATTRIBUT PASSPORT PADA SALAH SATU DATA 
    def mengganti_pasport(self, person, mengganti_passport):
        for i in range(len(self.anggota)):
            if self.anggota[i]['namaLengkap']== person:
                self.dictionary2[i]['nomorPaspor'] = mengganti_passport
                self.anggota[i]['nomorPaspor'] = mengganti_passport
            
    #METHOD UNTUK MEMASUKKAN DATA PADA DICTIONARY1 YANG DI MANA MERUPAKAN TABEL PERTAMA SERTA DICTIONARY2 YANG DI MANA MERUPAKAN TABEL KEDUA
    def tambah_anggota_dictionary(self, dictionary1,dictionary2):
        self.dictionary1.append(dictionary1)
        self.dictionary2.append(dictionary2)

    #METHOD UNTUK MENGOUTPUTKAN ISI DATA PADA TABEL KARTU KELUARGA
    def cetak_KartuKeluarga(self):
        
        tabel1 = pandas.DataFrame(self.dictionary1)
        tabel1.index+=1
        header1 = ['No', "Nama Lengkap", "NIK", "Jenis Kelamin", "Tempat Lahir", "Tanggal Lahir", "Agama", "Pendidikan", "Pekerjaan"]
        
        print(tabulate(tabel1, headers=header1, tablefmt="grid", stralign="center", numalign="center"))

        print("")
       


        tabel2 = pandas.DataFrame(self.dictionary2)
        tabel2.index+=1
        header2 = ['No', 'Status Perkawinan', "Status Hubungan Keluarga", "Kewarganegaraan", "No Paspor", "No KITAS", "Ayah", "Ibu"]
        print(tabulate(tabel2, headers=header2, tablefmt="grid", stralign="center", numalign="center"))
        
        print()
        print()

        return ""
        


class Dictionary:
    #KONSTRUKTOR CLASS Dictionary
    def __init__(self, nama_lengkap, nik, jenis_kelamin, tempat_lahir, tanggal_lahir, agama, pendidikan, pekerjaan, status_perkawinan,\
                  status_hubunganKeluarga, kewarganegaraan, no_paspor, no_kitas, ayah, ibu):
        self.dictionary = {'namaLengkap': nama_lengkap,'nik' : nik, 'gender': jenis_kelamin, 'tempatLahir' : tempat_lahir,'tanggalLahir': tanggal_lahir,\
                        'agama' : agama,'pendidikan': pendidikan,'pekerjaan': pekerjaan,'statusPerkawinan' : status_perkawinan,\
                        'status': status_hubunganKeluarga,'kewarganegaraan': kewarganegaraan, 'no_paspor': no_paspor,\
                       'no_kitas': no_kitas,'ayah' : ayah, 'ibu' : ibu}
        self.dictionary1 = {'namaLengkap': nama_lengkap,'nik' : nik, 'gender': jenis_kelamin, 'tempatLahir' : tempat_lahir,'tanggalLahir': tanggal_lahir,'agama' : agama,'pendidikan': pendidikan,'pekerjaan': pekerjaan}
        self.dictionary2 =  {'statusPerkawinan' : status_perkawinan,'status': status_hubunganKeluarga,'kewarganegaraan': kewarganegaraan, 'nomorPaspor': no_paspor,'no_kitas': no_kitas,'ayah' : ayah, 'ibu' : ibu}
    
    #METHOD UNTUK PEMBUATAN GETTER DICTIONARY
    def get_dictionary(self):
        return self.dictionary
    
    #METHOD UNTUK PEMBUATAN GETTER DICTIONARY1 YANG DI MANA MERUPAKAN TABEL 1  
    def _dictionary1(self):
        return self.dictionary1

    #METHOD UNTUK PEMBUATAN GETTER DICTIONARY YANG DI MANA MERUPAKAN TABEL 2
    def _dictionary2(self):
        return self.dictionary2

#FUNGSI UTAMA
if __name__=="__main__":
    
    kk = KartuKeluarga()
    kamus = Dictionary('MINATO',999888111,'Laki-Laki', 'YOGYAKARTA', '9-10-98', 'KRISTEN', 'S1', 'KARYAWAN SWASTA', 'MENIKAH', 'KEPALA KELUARGA', 
    'INDONESIA', '555667','9933', 'JACK', 'JULIET')
    getter_dict = kamus.get_dictionary()

    #TABEL DATA KK KOSONG
    print("DATA KK KOSONG")
    print(kk.cetak_KartuKeluarga())

    #MENAMBAH DATA KK
    kk.tambah_anggota(getter_dict)
    getter_kamus1 = kamus._dictionary1()
    getter_kamus2 = kamus._dictionary2()
    print()
    print("PENAMBAHAN DATA")
    kk.tambah_anggota_dictionary( getter_kamus1,getter_kamus2)
    print(kk.cetak_KartuKeluarga())

    #MENGUBAH SUATU ATTRIBUT PADA SALAH SATU DATA PADA TABEL KK
    print("METODE PENGUBAHAN PROFESI, PENDIDIKAN, SERTA PASSPORT PADA DATA KK ")
    kk.ganti_pekerjaan('MINATO', "PENGUSAHA")
    kk.ganti_sekolah('MINATO', "S3")
    kk.mengganti_pasport('MINATO', "6666")
    print(kk.cetak_KartuKeluarga())
    
    



