
def inisialisasiImg(inputfoto):
    """cek alamat IMG"""
    file = f"./manipulasi citra/{inputfoto}"
    img = cv.imread(file)
    
    bagianFoto = img.shape[:2]
    lebar, tinggi = bagianFoto
    
    return img,lebar,tinggi 

Pada fungsi diatas silakan sesuaikan dengan lokasi folder anda.

 # CONTOH
file_program/
    |
    |---file/
        |
        |---main.py
        |---filegambar.jpeg
        

membacanya adalah "./file_program/file/filegambar.jpeg" jadi ambil => "./file_program/" saja tidak perlu semua
ini mungkin karna konfigurasi pada pc saya yang menggunakan linux ini ada beberapa yang kurang pas otomatis ketika
saya melakukan cv2.imread('xxx') dia tidak bisa membaca (padahal 1 folder).