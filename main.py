import cv2 as cv
import time as tm 
import os
import numpy as np



def welcome(nameUser,delay=0.1):
    """Tulisan Welcome"""
    text = f"Selamat Datang {nameUser}\n\n"
    for karakter in text:
        print(karakter, end='', flush=True)
        tm.sleep(delay)

def inisialisasiImg(inputfoto):
    """cek alamat IMG"""
    file = f"./manipulasi citra/{inputfoto}"
    img = cv.imread(file)
    
    bagianFoto = img.shape[:2]
    lebar, tinggi = bagianFoto
    
    return img,lebar,tinggi   
    
def opsiPilih():
    """Opsi Pilih"""
    for i in range(4):
        number = i+1
        if number == 1:
            print(f"{number} Penskalaan Img".upper())
        elif number  == 2:
            print(f"{number} Totasi Img".upper())
        elif number == 3:
            print(f"{number} Translasi Img".upper())
        elif number == 4:
            print(f"{number} Exit\n".upper())

def clean():
    """Clean terminal"""
    os.system('clear')

def tampilkanfoto(nameUser,img):
    """Menampilkan GUI IMAGE"""
    cv.imshow(nameUser,img)
    
    key = cv.waitKey(0) & 0xFF 
    if key == ord('x'):
        cv.destroyAllWindows()
        clean()
            
def menupenskalaan(img,scale_x,scale_y):
    """Menu 1 penskalaan"""
    # Melakukan penskalaan citra
    resizeImg = cv.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv.INTER_LINEAR)
    return resizeImg

def menuRotasiImg(img,rotasi,tinggi,lebar):
    """Rotasi IMG"""
    titiktengah = (lebar // 2, tinggi // 2)
    M = cv.getRotationMatrix2D(titiktengah, rotasi, 1.0)
    rotated_img = cv.warpAffine(img, M, (tinggi, lebar))
    
    return rotated_img

def menuTranslasiCitra(img,lebar,tinggi,kanan,bawah):
    """Translasi Citra"""
    M = np.float32([[1, 0, kanan], [0, 1, bawah]])
    translated_img = cv.warpAffine(img, M, (tinggi, lebar))
    
    return translated_img

def Konversicitrawarna(img,inputwarna):
    if inputwarna == 1:
        ubahRBG = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return ubahRBG
        
    elif inputwarna == 2:
        ubahHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        return ubahHsv
    
    elif inputwarna == 3:
        ubahgrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return ubahgrey
    
def main():
    
    while True:
        inputName = input("Input Nama Anda\t:")
        inputFoto = input("Input Alamat Img:")
        
        img, lebar, tinggi = inisialisasiImg(inputFoto)
        
        if inputFoto == inputFoto:
            clean()
            welcome(inputName)
            opsiPilih()
            
            
            mainMenu = int(input('Pilih Menu (1,2,3,4) :'))
            
            
            if mainMenu == 1:
                print('== Start Menu 1 ==\n')
                print('Nilai Standar adalah 0.5.'.center(50))
                
                try:
                    sumbuX = float(input("Masukkan Value Sumbu X : "))
                    sumbuY = float(input("Masukkan Value Sumbu Y : "))
                except:
                    print('Mohon Gunakan Angka!!!')
                    
                foto = menupenskalaan(img,sumbuX,sumbuY)
                tampilkanfoto(inputName,foto)
            
            elif mainMenu == 2:
                print('Start Menu 2')
                
                try:
                    inputRotasi = int(input('Masukkan Rotasi IMG : '))
                except:
                    print('Mohon Gunakan Angka!!!')
                    
                dataRotasi = menuRotasiImg(img,inputRotasi,tinggi,lebar)
                tampilkanfoto(inputName,dataRotasi)    
                
            elif mainMenu == 3:
                print('Start Menu 3')
                
                try:
                    sudutKanan = int(input("Masukkan Sudut kanan : "))
                    sudutBawah = int(input("Masukkan Sudut Bawah : "))
                
                except:
                    print('Gunakan Angka!!!')
                
                dataTranslasiCitra = menuTranslasiCitra(img,lebar,tinggi,sudutKanan,sudutBawah)
                tampilkanfoto(inputName,dataTranslasiCitra)
                
            elif mainMenu == 4:
                clean()
                exit(f"Terima Kasih {inputName} ")
                break
                
            else:
                print("Input Salah")
        else:
            print('Adanya Kesalahan Mohon Ulangi....')    
            
            

if __name__ == "__main__":
    main()