# **************************************************************
'''
Program   : SISTEM INFORMASI AKADEMIK MAHASISWA
Deskripsi : Program ini merupakan sistem manajemen data akademik mahasiswa yang mengimplementasikan
            representasi data mahasiswa, mata kuliah, transkrip, dan kumpulan transkrip menggunakan
            tipe data bentukan dan operasi fungsional.
Kelompok  : 7
Anggota   : 1. Bagus Jatmiko           - (24060125140229)
            2. Muhammad Akbar Suryawan - (24060125140221)
            3. Aryo Bimo Bagaskoro     - (24060125140191)
            4. Lionel Ivanne Siswanto  - (24060125140133)
            5. Wilyan Purbo Buwono     - (24060125130068)
Tanggal   : 13/12/2025
'''
# **************************************************************
# DEFINISI DAN SPESIFIKASI TYPE
'''
type Mhs: <nim: string, nama: string>
    {<nim: string, nama: string> adalah sebuah mahasiswa dengan nim dan nama}

type Matkul: <nama: string, sks: integer, listNilai: list of real>
    {<nim: string, nama: string> adalah sebuah Matkul dengan nama mata kuliah, jumlah sks, dan list nilai}

type Transkrip: <Mhs, list of Matkul>
    {<Mhs, list of Matkul> adalah sebuah Transkrip dengan data mahasiswa dan list mata kuliah}

type SetTranskrip: <Mhs, list of Matkul>
    {<Mhs, list of Matkul> adalah sebuah SetTranskrip dengan list kosong}
'''
# **************************************************************
# REALISASI TYPE
type Mhs = tuple[str,str]
type Matkul = tuple[str,int,list]
type Transkrip = tuple[Mhs,list]
type SetTranskrip = tuple[list]
# **************************************************************
# DEFINISI DAN SPESIFIKASI FUNGSI KONSTRUKTOR
'''
MakeMhs: 2 string -> Mhs
    {MakeMhs(nim, nama) membuat objek Mhs dengan NIM nim dan nama}

MakeMatkul: string, integer, list of real -> Matkul
    {MakeMatkul(nama, sks, listNilai) membuat objek Matkul dengan nama mata kuliah nama, jumlah SKS sks,
     dan list nilai listNilai}

MakeTranskrip: <Mhs, list of Matkul> → Transkrip
     {MakeTranskrip(M, listMK) membuat objek Transkrip dengan data mahasiswa M dan list mata kuliah listMK}

MakeSetTranskrip: → SetTranskrip
    {MakeSetTranskrip() membuat SetTranskrip kosong (list kosong)}
'''
# **************************************************************
# REALISASI FUNGSI KONSTRUKTOR
def MakeMhs(nim: str, nama: str) -> Mhs:
    return [nim, nama]

def MakeMatkul(nama: str, sks: int, listNilai: list) -> Matkul:
    return [nama, sks, listNilai]

def MakeTranskrip(M: Mhs, listMK: list) -> Transkrip:
    return [M, listMK]

def MakeSetTranskrip() -> SetTranskrip:
    return []
# **************************************************************
# DEFINISI DAN SPESIFIKASI FUNGSI SELEKTOR
'''
GetNIM: Mhs -> string
    {GetNIM(M) mengambil NIM dari mahasiswa M}

GetNama: Mhs -> string
    {GetNama(M) mengambil nama dari mahasiswa M}

GetNamaMK: Matkul -> string
    {GetNamaMK(MK) mengambil nama mata kuliah dari MK}

GetSKS: Matkul -> integer
    {GetSKS(MK) mengambil jumlah SKS dari MK}

GetNilai: Matkul -> list of real
    {GetNilai(MK) mengambil list nilai dari MK}

GetMhs: Transkrip → Mhs
    {GetMhs(T) mengambil data mahasiswa dari transkrip T}

GetListMatkul: Transkrip → list of Matkul
    {GetListMatkul(T) mengambil list mata kuliah dari transkrip T}
'''
# **************************************************************
# REALISASI FUNGSI SELEKTOR
def GetNIM(M: Mhs) -> str:
    return M[0]

def GetNama(M: Mhs) -> str:
    return M[1]

def GetNamaMK(MK: Matkul) -> str:
    return MK[0]

def GetSKS(MK: Matkul) -> int:
    return MK[1]

def GetNilai(MK: Matkul) -> list:
    return MK[2]

def GetMhs(T: Transkrip) -> Mhs:
    return T[0]

def GetListMatkul(T: Transkrip) -> list:
    return T[1]
# **************************************************************
# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
'''
{Definisi dan spesifikasi untuk fungsi antara terletak pada file list_operators.py. Implementasi fungsi
konstruktor, selektor, predikat, dan operator koleksi objek list dijelaskan pada file list_operators.py.
Fungsi di dalam file list_operators.py diimpor ke file ini menggunakan fungsi import bawaan bahasa
pemrograman python.}
'''
# **************************************************************
# REALISASI FUNGSI ANTARA
from list_operators import *

def AddNilaiPadaList(listMK, namaMK, nilai):
    if IsEmpty(listMK):
        return []
    else:
        if GetNamaMK(FirstElmt(listMK)) == namaMK:
            return Konso(MakeMatkul(GetNamaMK(FirstElmt(listMK)), GetSKS(FirstElmt(listMK)), Konsi(GetNilai(FirstElmt(listMK)), nilai)),
                         Tail(listMK))
        else:
            return Konso(FirstElmt(listMK), AddNilaiPadaList(Tail(listMK), namaMK, nilai))

def MaxTranskrip(S):
    if IsEmpty(S):
        return []
    elif IsEmpty(Tail(S)):
        return FirstElmt(S)
    else:
        if IPKTranskrip(FirstElmt(S)) >= IPKTranskrip(MaxTranskrip(Tail(S))):
            return FirstElmt(S)
        else:
            return MaxTranskrip(Tail(S))

def MKMaxPadaList(listMK, S):
    if IsEmpty(listMK):
        return ""
    elif IsEmpty(Tail(listMK)):
        return GetNamaMK(FirstElmt(listMK))
    else:
        if CountMengulangMKPadaSet(S, GetNamaMK(FirstElmt(listMK))) >= CountMengulangMKPadaSet(S, MKMaxPadaList(Tail(listMK), S)):
            return GetNamaMK(FirstElmt(listMK))
        else:
            return MKMaxPadaList(Tail(listMK), S)

def CountMengulangMKPadaSet(S, namaMK):
    if IsEmpty(S):
        return 0
    else:
        if IsEmpty(CariMatkul(FirstElmt(S), namaMK)):
            return CountMengulangMKPadaSet(Tail(S), namaMK)
        else:
            if MengulangMK(CariMatkul(FirstElmt(S), namaMK)):
                return 1 + CountMengulangMKPadaSet(Tail(S), namaMK)
            else:
                return CountMengulangMKPadaSet(Tail(S), namaMK)
# **************************************************************
# DEFINISI DAN SPESIFIKASI OPERATOR
'''
NilaiSekarangMK: Matkul → real
    {NilaiSekarangMK(MK) mengambil nilai akhir dari MK. Jika list kosong → −1.0. Jika tidak → elemen terakhir}

SudahAmbilMK: Matkul → boolean
    {SudahAmbilMK(MK) mengembalikan True jika list nilai MK tidak kosong}

MengulangMK: Matkul → boolean
    {MengulangMK(MK) mengembalikan True jika panjang list nilai MK > 1}

LulusMK: Matkul → boolean
    {LulusMK(MK) mengembalikan True jika nilai akhir MK ≥ 2.0}

CariMatkul: <Transkrip, string> → Matkul
    {CariMatkul(T, namaMK) mencari dan mengambil Matkul dari transkrip T berdasarkan nama mata kuliah namaMK}

TotalSKSLulus: Transkrip → integer
    {TotalSKSLulus(T) menjumlahkan seluruh SKS dari mata kuliah yang lulus(nilai ≥ 2.0) pada transkrip T}

JumlahMatkulMengulang: Transkrip → integer
    {JumlahMatkulMengulang(T) menghitung jumlah mata kuliah yang diulang (panjang list nilai > 1) pada transkrip T}

IPKTranskrip: Transkrip → real
    {IPKTranskrip(T) menghitung IPK dari transkrip T dengan rumus: (total NilaiAkhir × SKS)/total SKS}

AddTranskrip: <SetTranskrip, Transkrip> → SetTranskrip
    {AddTranskrip(S, T) menambahkan transkrip T ke akhir SetTranskrip S jika NIM mahasiswa pada T belum ada di S.
     jika sudah ada, tidak ditambahkan}

AddNilaiMatkul: <SetTranskrip, string, string, real> → SetTranskrip
    {AddNilaiMatkul(S, nim, namaMK, nilai) menambahkan nilai baru nilai ke mata kuliah namaMK pada transkrip
     mahasiswa dengan NIM nim di SetTranskrip S}

CariTranskripMhs: <SetTranskrip, string> → Transkrip
  {CariTranskripMhs(S, nim) mencari dan mengembalikan transkrip pertama
   dengan NIM nim dari SetTranskrip S}

TopIPK: SetTranskrip → Mhs
  {TopIPK(S) menghasilkan mahasiswa dengan IPK tertinggi dari
   SetTranskrip S }

CountMhsPernahMengulang: SetTranskrip → integer
  {CountMhsPernahMengulang(S) menghitung jumlah mahasiswa yang
   pernah mengulang minimal 1 mata kuliah pada SetTranskrip S}

CountMhsLulusSemuaMatkul: SetTranskrip → integer
  {CountMhsLulusSemuaMatkul(S) menghitung jumlah mahasiswa yang
   lulus seluruh mata kuliah yang diambil pada SetTranskrip S}

MatkulPalingSeringDiulang: SetTranskrip → string
  {MatkulPalingSeringDiulang(S) menghasilkan nama mata kuliah yang
   paling sering diulang (frekuensi tertinggi) pada SetTranskrip S}

CountMhsDenganIPKRentang: <SetTranskrip, real, real> → integer
  {CountMhsDenganIPKRentang(S, a, b) menghitung jumlah mahasiswa
   dengan IPK dalam rentang [a, b] pada SetTranskrip S}
'''
# **************************************************************
# REALISASI OPERATOR
def NilaiSekarangMK(MK: Matkul) -> float:
    if IsEmpty(GetNilai(MK)):
        return -1.0
    else:
        return LastElmt(GetNilai(MK))
    
def SudahAmbilMK(MK: Matkul) -> bool:
    if IsEmpty(GetNilai(MK)):
        return False
    else:
        return True

def MengulangMK(MK: Matkul) -> bool:
    return NbElmt(GetNilai(MK)) > 1

def LulusMK(MK: Matkul) -> bool:
    return NilaiSekarangMK(MK) >= 2.0

def CariMatkul(T: Transkrip, namaMK: str) -> Matkul:
    if IsEmpty(GetListMatkul(T)):
        return []
    else:
        if GetNamaMK(FirstElmt(GetListMatkul(T))) == namaMK:
            return FirstElmt(GetListMatkul(T))
        else:
            return CariMatkul(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))), namaMK)

def TotalSKSLulus(T: Transkrip) -> int:
    if IsEmpty(GetListMatkul(T)):
        return 0
    else:
        if LulusMK(FirstElmt(GetListMatkul(T))):
            return GetSKS(FirstElmt(GetListMatkul(T))) + TotalSKSLulus(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return TotalSKSLulus(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))

def JumlahMatkulMengulang(T: Transkrip) -> int:
    if IsEmpty(GetListMatkul(T)):
        return 0
    else:
        if MengulangMK(FirstElmt(GetListMatkul(T))):
            return 1 + JumlahMatkulMengulang(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return JumlahMatkulMengulang(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))

def TotalNilai(T):
    if IsEmpty(GetListMatkul(T)):
        return 0
    else:
        return NilaiSekarangMK(FirstElmt(GetListMatkul(T))) * GetSKS(FirstElmt(GetListMatkul(T))) + TotalNilai(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
    
def TotalSKS(T):
    if IsEmpty(GetListMatkul(T)):
        return 0
    else:
        return GetSKS(FirstElmt(GetListMatkul(T))) + TotalSKS(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))

def IPKTranskrip(T):
    return TotalNilai(T) / TotalSKS(T)

def AddTranskrip(S: SetTranskrip, T: Transkrip) -> SetTranskrip:
    if IsEmpty(S):
        return Konsi(S, T)
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == GetNIM(GetMhs(T)):
            return S
        else:
            return Konso(FirstElmt(S), AddTranskrip(Tail(S), T))

def AddNilaiMatkul(S: SetTranskrip, nim: str, namaMK: str, nilai: float) -> SetTranskrip:
    if IsEmpty(S):
        return []
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == nim:
            return Konso(MakeTranskrip(GetMhs(FirstElmt(S)), AddNilaiPadaList(GetListMatkul(FirstElmt(S)), namaMK, nilai)),
                         Tail(S))
        else:
            return Konso(FirstElmt(S), AddNilaiMatkul(Tail(S), nim, namaMK, nilai))

def CariTranskripMhs(S: SetTranskrip, nim: str) -> Transkrip:
    if IsEmpty(S):
        return []
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == nim:
            return FirstElmt(S)
        else:
            return CariTranskripMhs(Tail(S), nim)

def TopIPK(S: SetTranskrip) -> Mhs:
    if IsEmpty(S):
        return []
    else:
        return GetMhs(MaxTranskrip(S))

def CountMhsPernahMengulang(S: SetTranskrip) -> int:
    if IsEmpty(S):
        return 0
    else:
        if JumlahMatkulMengulang(FirstElmt(S)) > 0:
            return 1 + CountMhsPernahMengulang(Tail(S))
        else:
            return CountMhsPernahMengulang(Tail(S))

def CountMhsLulusSemuaMatkul(S: SetTranskrip) -> int:
    if IsEmpty(S):
        return 0
    else:
        if TotalSKSLulus(FirstElmt(S)) == TotalSKS(FirstElmt(S)):
            return 1 + CountMhsLulusSemuaMatkul(Tail(S))
        else:
            return CountMhsLulusSemuaMatkul(Tail(S))


def MatkulPalingSeringDiulang(S: SetTranskrip) -> str:
    if IsEmpty(S):
        return ""
    else:
        return MKMaxPadaList(GetListMatkul(FirstElmt(S)), S)

def CountMhsDenganIPKRentang(S: SetTranskrip, a: float, b: float) -> int:
    if IsEmpty(S):
        return 0
    else:
        if a <= IPKTranskrip(FirstElmt(S)) <= b:
            return 1 + CountMhsDenganIPKRentang(Tail(S), a, b)
        else:
            return CountMhsDenganIPKRentang(Tail(S), a, b)
# **************************************************************
# APLIKASI
M = MakeMhs("A11.2020.01234", "Reno") # -> Membuat objek Mhs
MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0]) # -> Membuat objek Matkul
MK2 = MakeMatkul("Matdis", 2, []) # -> Membuat objek Matkul
T = MakeTranskrip(M, [MK1, MK2]) # -> Membuat objek Transkrip
S1 = MakeSetTranskrip() 
M1 = MakeMhs("A11.01", "Reno")
T1 = MakeTranskrip(M1, [MK1, MK2])
S2 = AddTranskrip(S1, T1) 
S3 = AddTranskrip(S2, T1)
M2 = MakeMhs("A11.02", "Andi")
MK4 = MakeMatkul("Matdis", 2, [4.0])
T2 = MakeTranskrip(M2, [MK1, MK4])
S4 = AddTranskrip(S3, T2)
M3 = MakeMhs("A11.03", "Budi")
MK5 = MakeMatkul("Daspro", 3, [1.0, 2.0])
MK6 = MakeMatkul("Kalkulus", 4, [3.0])
T3 = MakeTranskrip(M3, [MK5, MK6])
S5 = AddTranskrip(S4, T3)
S7 = AddNilaiMatkul(S5, "A11.02", "Daspro", 4.0)

print(GetNIM(M)) # -> "A11.2020.01234"
print(GetNama(M)) # -> "Reno"

print(GetNamaMK(MK1)) # -> "Daspro"
print(GetSKS(MK1)) # -> 3
print(GetNilai(MK1)) # -> [2.0, 3.0]
print(NilaiSekarangMK(MK1)) # -> 3.0
print(NilaiSekarangMK(MK2)) # -> -1.0
print(SudahAmbilMK(MK2)) # -> False
print(MengulangMK(MK1)) # -> True
print(LulusMK(MK1)) # -> True

MK2 = MakeMatkul("Matdis", 2, [3.0, 4.0])
T = MakeTranskrip(M, [MK1, MK2])
S1 = MakeSetTranskrip() 
M1 = MakeMhs("A11.01", "Reno")
T1 = MakeTranskrip(M1, [MK1, MK2])
S2 = AddTranskrip(S1, T1) 
S3 = AddTranskrip(S2, T1)
M2 = MakeMhs("A11.02", "Andi")
MK4 = MakeMatkul("Matdis", 2, [4.0])
S4 = AddTranskrip(S3, T2)
M3 = MakeMhs("A11.03", "Budi")
MK5 = MakeMatkul("Daspro", 3, [1.0, 2.0])
MK6 = MakeMatkul("Kalkulus", 4, [3.0])
T3 = MakeTranskrip(M3, [MK5, MK6])
S5 = AddTranskrip(S4, T3)
S7 = AddNilaiMatkul(S5, "A11.02", "Daspro", 4.0)

print(GetMhs(T)) # -> M (objek Mahasiswa)
print(GetListMatkul(T)) # -> [MK1, MK2]
print(CariMatkul(T, "Daspro")) # -> MK1 (objek Matkul)
print(TotalSKSLulus(T)) # -> 5
print(JumlahMatkulMengulang(T)) # -> 2
print(IPKTranskrip(T)) # -> 3.4

MK2 = MakeMatkul("Matdis", 2, [3.0])
T = MakeTranskrip(M, [MK1, MK2])
S1 = MakeSetTranskrip() 
M1 = MakeMhs("A11.01", "Reno")
T1 = MakeTranskrip(M1, [MK1, MK2])
S2 = AddTranskrip(S1, T1) 
S3 = AddTranskrip(S2, T1)
M2 = MakeMhs("A11.02", "Andi")
MK4 = MakeMatkul("Matdis", 2, [4.0])
S4 = AddTranskrip(S3, T2)
M3 = MakeMhs("A11.03", "Budi")
MK5 = MakeMatkul("Daspro", 3, [1.0, 2.0])
MK6 = MakeMatkul("Kalkulus", 4, [3.0])
T3 = MakeTranskrip(M3, [MK5, MK6])
S5 = AddTranskrip(S4, T3)
S7 = AddNilaiMatkul(S5, "A11.02", "Daspro", 4.0)

print(CariTranskripMhs(S7,"A11.01"))
print(CariTranskripMhs(S7, "A11.03"))
print(TopIPK(S7))
print(CountMhsPernahMengulang(S7) )
print(CountMhsLulusSemuaMatkul(S7))
print(MatkulPalingSeringDiulang(S7))
print(CountMhsDenganIPKRentang(S7, 2.0, 3.0))
# **************************************************************