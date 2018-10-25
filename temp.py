# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal para el proyecto de astrofísica.
"""

from PIL import Image, ImageOps

"""
sample=Image.open("sample.jpg")#Carga la imagen
#sample.show()#La muestra

ancho,alto=sample.size #Da el ancho y la altura

pixelmap=sample.load() #Crea un mapa de pixeles
pixel=pixelmap[0,0] #Obtiene el valor del primer pixel
print(pixel) 
pixelmap[0,0]=(0,0,0) #Cambia el valor del primer pixel
print(pixel)

ancho, alto=sample.size

listai=[]
listaj=[]

#for i in range(sample.size[0]):
    #for j in range(sample.size[1]):
        #pixel=pixelmap[i,j]
        #if pixel==(0,0,0):
        
for i in range(1296):
    for j in range(10):
        pixelmap[j,i]=(0,0,0)
for i in range(2000):
    for j in range(10,20):
        pixelmap[j,i]=(0,0,0)

for i in range(20):
    for j in range(alto):
        if pixelmap[i,j]!=(0,0,0):
            listai.insert(len(listai),i)
            listaj.insert(len(listai),j)
            break

        
sample.show()
"""
sol1=Image.open("sol1.jpg")  
sol1=ImageOps.autocontrast(sol1)
#sol1=ImageOps.autocontrast(sol1)
sol1p=sol1.load()
ancho, alto=sol1.size

#============================================================================#
#============================================================================#
#=====================OBTENCIÓN DEL RANGO A ESTUDIAR=========================#
#============================================================================#
#============================================================================#

lista1si=[]
lista1sj=[]
lista1ii=[]
lista1ij=[]
lista2ii=[]
lista2ij=[]
lista2ia=[]
lista2di=[]
lista2dj=[]
lista2da=[]
umbral=70
#Decide el rango en el cual se encuentra el sol
#Extremo superior
for j in range(ancho):
    for i in range(256):
        b=sol1.getpixel((i,j))
        if b>umbral:
            lista1si.insert(len(lista1si),i)
            lista1sj.insert(len(lista1sj),j)
            break
    if b>umbral:
        break
#Extremo inferior
for j in range(ancho)[::-1]:
    for i in range(256,512)[::-1]: #Se define así para evitar conflicto con los créditos
        b=sol1.getpixel((i,j))
        if b>umbral:
            lista1ii.insert(len(lista1ii),i)
            lista1ij.insert(len(lista1ij),j)
            break
    if b>umbral:
        break
#Extremo izquierdo
for j in range(lista1sj[0], lista1ij[0]):
    for i in range(ancho):
        #if pixelmap[i,j]!=(0,0,0):
        #    listai.insert(len(listai),i)
        #    listaj.insert(len(listai),j)
        #    break        
        a=sol1.getpixel((i,j))
        if a>umbral:
            lista2ii.insert(len(lista2ii),i)
            lista2ij.insert(len(lista2ij),j)
            lista2ia.insert(len(lista2ia),a)
            sol1p[i,j]=(255)
            break
#Extremo derecho
for j in range(lista1sj[0], lista1ij[0]):
    for i in range(ancho)[::-1]:
        #if pixelmap[i,j]!=(0,0,0):
        #    listai.insert(len(listai),i)
        #    listaj.insert(len(listai),j)
        #    break        
        a=sol1.getpixel((i,j))
        if a>umbral:
            lista2di.insert(len(lista2di),i)
            lista2dj.insert(len(lista2dj),j)
            lista2da.insert(len(lista2da),a)
            sol1p[i,j]=(255)
            break
        
#============================================================================#
#============================================================================#
#======================ESTUDIANDO EL SOL EN EL RANGO=========================#
#============================================================================#
#============================================================================#
#Declaro las nuevas listas
listava=[]
listavai=[]
listavaj=[]
#Analiza dentro del rango
for i in range(0,lista1ij[0]-lista1sj[0]):
    for j in range(lista2ii[i],lista2di[i]):
        aa=sol1.getpixel((j,i+lista1sj[0]))
        #if aa<70:
        #    listava.insert(len(listava),aa)
        #    listavai.insert(len(listavai),i)
        #    listavaj.insert(len(listavaj),j)
        #    sol1p[j,i+lista1sj[0]]=(255)
        

         
sol1.show()


        
        
        
        








        
        
        
        
        
        
        
        
        
        