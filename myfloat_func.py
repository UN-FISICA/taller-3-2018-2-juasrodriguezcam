def imprimir(a):
    pc=len(a[0])
    sc=len(a[1])
    temp=0
    entero=""
    decimal=""

    for i in range (pc):
        temp=str(a[0][i])
        entero=str(entero)+temp
    for j in range (sc):
        temp=str(a[1][j])
        decimal=str(decimal)+temp
    return print ("{},{}".format(entero,decimal))

def safe(a): #Genera una copia de la tupla a,evita modificar la tupla
        ent=a[0][:]
        dec=a[1][:]
        b=(ent,dec)
        return b

#========================================================================
#==============================Suma======================================
#========================================================================

def suma(a,b,sincero=1):
    #Se guardan
    a=safe(a)
    b=safe(b)
    #Quito y guardo el signo
    signa=a[0].pop(0)
    signb=b[0].pop(0)
    #Guardo cuántos decimales hay
    deca=len(a[1])
    decb=len(b[1])
    #Igualo la parte decimal
    if deca>decb: #a mayor
        for i in range(deca-decb):
            b[1].append(0) 
    if decb>deca: #b mayor
        for i in range(decb-deca):
            a[1].append(0)
    deca=len(a[1])
    #Igualo la parte entera
    if len(a[0])>len(b[0]):
        for i in range(len(a[0])-len(b[0])):
            b[0].insert(0,0)    
    if len(b[0])>len(a[0]):
        for i in range(len(b[0])-len(a[0])):
            a[0].insert(0,0)
    #Paso la parte decimal a la misma lista del entero
    for i in range(len(a[1])):
        a[0].insert(len(a[0]),a[1].pop(0))
    for i in range(len(b[1])):
        b[0].insert(len(b[0]),b[1].pop(0))
    #Busco el más grande
    for i in range(len(a[0])):
        comp=a[0][i]-b[0][i]
        if comp<0:
            signa,signb=signb,signa
            for k in range(len(a[0])):
                a[0][k],b[0][k]=b[0][k],a[0][k] #En caso de que b sea más grande lo ubica en a
            break
        elif comp>0:
            break
    #Crea la lista resultado
    resul=[]
    for i in range(len(a[0])):
        resul.insert(0,0)
    #Opera
    if signa==signb: #Signos iguales suma
        for i in range(len(a[0])-1,-1,-1): #Toma valores de mayor a menor para la longitud
            aux=a[0][i]+b[0][i] #Suma el valor que haya en cada lista
            if aux<10: 
                resul[i]+=aux #Lo suma al resultado
            else:
                aux=str(aux) #Separa como string el número y guarda la última cifra
                aux=aux[1]
                aux=int(aux)
                resul[i]+=aux #Suma esta cifra al resultado
                if i==0:
                    resul.insert(0,1) #Si es el último para sumar le agrega un uno al inicio
                else:
                    resul[i-1]+=1 #Si no solo suma un uno a la casilla siguiente
            if resul[i]>9:
                if i==0:
                    resul[i]=str(resul[i])
                    lleva,resul[i]=int(resul[i][0]),int(resul[i][1])
                    resul.insert(0,lleva)
                else:    
                    resul[i]=str(resul[i])
                    lleva,resul[i]=int(resul[i][0]),int(resul[i][1])
                    resul[i-1]+=lleva
    elif signa!=signb: #Signos distintos resta
        for i in range(len(a[0])-1,-1,-1):
            aux=a[0][i]-b[0][i] #Resta los valores de cada lista
            if aux<0:
                resul[i]+=10
                a[0][i-1]-=1
                resul[i]+=aux
            else:
                resul[i]+=aux
    #Convierte a tupla
    deci=[]
    for i in range(deca):
        deci.insert(0,resul.pop(len(resul)-1))
    resul.insert(0,signa)
    if sincero==1:
        for i in range(1,len(resul)):
            if resul[1]!=0:
                break
            if len(resul)<3:
                break
            resul.pop(1)
    fin=(resul,deci)
    return fin

#=======================================================================
#==============================Resta====================================
#=======================================================================
def resta(a,b):
    #Se guardan
    a=safe(a)
    b=safe(b)
    signa=a[0][0]
    signb=b[0][0]
    if signa!=signb:
        b[0][0]=a[0][0]
    elif signa==signb:
        if signa=='+':
            b[0][0]='-'
        elif signa=='-':
            b[0][0]='+'
    return suma(a,b)

#=======================================================================
#===========================Multiplicación==============================
#=======================================================================
def multiplicacion(a,b):
    #Se guardan
    a=safe(a)
    b=safe(b)
    #Quito y guardo el signo
    signa=a[0].pop(0)
    signb=b[0].pop(0)
    #Guardo cuántos decimales hay
    deca=len(a[1])
    decb=len(b[1])
    #Paso la parte decimal a la misma lista del entero
    for i in range(len(a[1])):
        a[0].insert(len(a[0]),a[1].pop(0))
    for i in range(len(b[1])):
        b[0].insert(len(b[0]),b[1].pop(0))
    #Creo una lista que contendrá el resultado de cada multiplicación como una lista
    resul=[]
    for i in range(len(b[0])):
        resul.append([0]*(len(a[0])+1+i)) #Creo los ceros a la derecha que permitirán sumar estas listas
        for j in range(len(a[0])):
            #Multiplica y acomoda a la izquierda (len(resul)-i-1) de los ceros
            mul=a[0][len(a[0])-j-1]*b[0][len(b[0])-i-1]
            if mul>9: #Soluciona el que en una casilla la multiplicación de dos dígitos
                mul=str(mul)
                lleva,mul=int(mul[0]),int(mul[1])
                resul[i][len(a[0])-j]+=mul
                resul[i][len(a[0])-j-1]+=lleva
            else: #Otro caso
                resul[i][len(a[0])-j]+=mul
            parcial=resul[i][len(a[0])-j]
            if parcial>9: #Soluciona el que al sumar lo que se llevaba, nuevamente de dos dígitos
                parcial=str(parcial)
                lleva1,parcial1=parcial[0],parcial[1]
                lleva1,parcial1=int(lleva1),int(parcial1)
                resul[i][len(a[0])-j]=parcial1
                resul[i][len(a[0])-j-1]+=lleva1
        resul[i].insert(0,'+') #Agrega el signo a la lista
        resul[i]=(resul[i],[]) #Vuelve esa lista una tupla
    cuenta=(['+',0],[]) #Crea la lista que llevará la suma
    for i in range(len(resul)):
        cuenta=suma(cuenta,resul[i],sincero=0) #suma todas las listas de resul (los escalones)
    for i in range(deca+decb): #Pasa la parte decimal a la lista derecha
        cuenta[1].insert(0,cuenta[0].pop(len(cuenta[0])-1))  
    for i in range(1,len(cuenta[0])):#Por la naturaleza del código pueden quedar ceros al inicio, los quita
        if cuenta[0][1]!=0:
            break
        if len(cuenta[0])<3:
            break
        cuenta[0].pop(1)
    if signa!=signb: #En caso de que los signos originales sean distintos, pone un menos
        cuenta[0][0]='-'
    return cuenta

#=======================================================================
#============================División===================================
#=======================================================================
def division(a,b,cifras=100):  
    #Se guardan
    a=safe(a)
    b=safe(b)
    #Guardo los signos y los vuelvo positivos (para asegurar restar efectivamente)
    signa=a[0][0]
    signb=b[0][0]
    a[0][0]='+'
    b[0][0]='+'
    #Paso la parte decimal a la misma lista del entero
    diva=0 #Los contadores de las veces que se 'dividió' por 10
    divb=0
    for i in range(len(a[1])):
        a[0].insert(len(a[0]),a[1].pop(0))
        diva+=1
    for i in range(len(b[1])):
        b[0].insert(len(b[0]),b[1].pop(0))
        divb+=1   
    #En caso de que a sea menor que b:
    cuentadiez=0 #Cuántas veces se multiplicó por diez
    diez=(['+',1,0],[])
    for i in range(len(b[0])-len(a[0])):
        a=multiplicacion(a,diez)
        cuentadiez+=1
    #Divide
    seccion=(['+'],[]) #La sección de 'a' a usar
    for i in range(len(b[0])-1): #quita uno por el signo
        seccion[0].insert(len(seccion[0]),a[0][i+1])
    #for j in range(len(a[0])-1): #Necesario para tomar la cantidad de cifras en la linea ''seccion''
    #    for i in range(len(b[0])-1):
    #        seccion[0].insert(len(seccion[0]),a[i])
    cociente=(['+'],[])
    for j in range(len(a[0])-len(b[0])+1): #Mediante este hallo toda la parte entera
        for i in range(11): #Ciclo for destinado a hallar el siguiente dígito de cociente
            candidato=(['+',i],[]) #El número por el que va a multiplicar (en tupla)
            busca=multiplicacion(b,candidato) 
            resto=resta(seccion,busca)
            if resto[0][0]=='-':
                candidato=(['+',i-1],[]) #Estas tres lineas que siguen es para hacer lo mismo...
                busca=multiplicacion(b,candidato) #... pero con el número anterior, pues candidato...
                resto=resta(seccion,busca) #... se pasa para lograr el negativo
                seccion=resto #los primeros digitos de seccion son resto
                cociente[0].insert(len(cociente[0]),candidato[0][1]) #Guarda el candidato en insert
                #print(busca,resto,candidato)
                if j==len(a[0])-len(b[0]): #Range llega hasta un número antes, por eso aquí no hay +1
                    break #Se rompe pues no hay más números para 'bajar'
                seccion[0].insert(len(seccion[0]),a[0][len(b[0])+j]) #'Baja' el siguiente número
                #print(busca,resto,candidato)
                break
    if seccion[0][1]!=0: #Si la división no es exacta
        seccion[0].insert(len(seccion[0]),0) #Se anexa un cero por haber llegado a la coma
        for j in range(cifras):
            for i in range(11): 
                candidato=(['+',i],[]) 
                busca=multiplicacion(b,candidato) 
                resto=resta(seccion,busca)
                if resto[0][0]=='-':
                    candidato=(['+',i-1],[])
                    busca=multiplicacion(b,candidato) 
                    resto=resta(seccion,busca)
                    seccion=resto
                    cociente[1].insert(len(cociente[1]),candidato[0][1])
                    seccion[0].insert(len(seccion[0]),0)
                    #print(busca,resto,candidato)
                    break
    #Para corregir las cifras decimales que se corrieron al principio
    cerouno=(['+',0],[1])
    potencia=-diva+divb
    if potencia!=0:
        if potencia>0:
            for i in range(potencia):
                cociente=multiplicacion(cociente,diez)
        elif potencia<0:
            for i in range(-potencia):
                cociente=multiplicacion(cociente,cerouno)
    #Para correr las cifras decimales que se corrieron al multiplicar por diez en valores pequeños.
    if cuentadiez>0:
        for i in range(cuentadiez):
            cociente=multiplicacion(cociente,cerouno)
    #Para dejar exactas las cifras decimales que se quiere:
    if len(cociente[1])>cifras:
        for i in range(len(cociente[1])-cifras):
            cociente[1].pop(len(cociente[1])-1)
    #El signo
    if signa==signb:
        cociente[0][0]='+'
    elif signa!=signb:
        cociente[0][0]='-'
    return cociente
 
#========================================================================
#===========================Comparación==================================
#========================================================================
def comparacion(a,b):
    lona=len(a)
    lonb=len(b)
    if lona!=lonb:
      print("Son tuplas diferentes")
    elif lona==lonb:
      for i in range(lona):
        ver1=lona-1
        loninta=len(a[i])
        lonintb=len(b[i])
        if loninta!=lonintb:
          print("Son tuplas diferentes")
          break
        elif loninta==lonintb:
          for j in range(loninta):
            ver2=loninta-1
            x=a[i][j]
            y=b[i][j]
            if x!=y:
              print("Son tuplas diferentes")
              break
            elif i==ver1:
              if j==ver2:
                print("Son tuplas iguales")
        if x!=y:
          break
#========================================================================
#================================== Pi ==================================
#========================================================================        
def pi():
    cuatro=(['+',4],[])
    dos=(['+',2],[])
    uno=(['+',1],[])
    menosuno=(['-',1],[])
    dividendo=(['-',1],[])
    cuenta=(['+',0],[])
    kha=(['-',1],[])
    for k in range(600000):
        kha=suma(uno,kha)
        dosk=multiplicacion(dos,kha)
        divisor=suma(dosk,uno)
        dividendo=multiplicacion(menosuno,dividendo)
        total=division(dividendo,divisor,30)
        cuenta=suma(cuenta,total)
        #print(kha)
    pi=multiplicacion(cuatro,cuenta)
    return pi


if __name__ == "__main__":
    print(imprimir(pi()))
