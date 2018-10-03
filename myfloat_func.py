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

#Función adicional para solucionar problemas, genera una tupla dummie para no modificar la original.
def safe(a): #Genera una copia de la tupla a,evita modificar la tupla
        ent=a[0][:]
        dec=a[1][:]
        b=(ent,dec)
        return b

#Funciones adicionales para usar en suma y resta:
#=======================================================================
#===============================Suma1===================================
#Esta no es la función suma que el profesor pide
def suma1(a,b):
    a=safe(a)
    b=safe(b)
    #Define la longitud de cada parte de las tuplas.
    all0=len(a[0])
    all1=len(a[1])
    bll0=len(b[0])
    bll1=len(b[1])
    
    #--------------------Completa con 0 casillas-----------------
    
    if all0>bll0:
        ss=all0-bll0    
        for i in range(ss):
            b[0].insert(1,0)    
    elif all0<bll0:
        ss=bll0-all0    
        for i in range(ss):
            a[0].insert(1,0)    
    if all1>bll1:
        ss=all1-bll1    
        for i in range(ss):
            b[1].insert(bll1,0)    
    elif all1<bll1:
        ss=bll1-all1    
        for i in range(ss):
            a[1].insert(all1,0)    
    
    alle=len(a[0])
    alld=len(a[1])
    esum=list(range(alle))
    dsum=list(range(alld))
                
    #-----------------------------Suma-----------------------------
    for i in range(alld-1,-1,-1):
            suma=a[1][i]+b[1][i]
            #Por si el número de arriba es más grande.
            if suma>9:
                #Por si está en el dígito de la coma.
                if i==0:
                    #Toma la suma cono str.
                    suma=str(a[1][i]+b[1][i])
                    #suma se vuelve el segundo dígito.
                    suma=int(suma[1])
                    #Suma uno al siguiente dígito.
                    a[0][alle-1]=a[0][alle-1]+1
                #Para los demás.
                else:
                    suma=str(a[1][i]+b[1][i])
                    suma=int(suma[1])
                    a[1][i-1]=a[1][i-1]+1
            #Ingresa el valor al vector resultado.
            dsum[i]=suma
            
    for i in range(alle-1,-1,-1):
        if i==0:
            break
        suma=a[0][i]+b[0][i]
        #Por si el número de arriba es más grande.
        if suma>9:
            if i==1:
                suma=str(a[0][i]+b[0][i])
                suma=int(suma[1])
                esum[i]=suma
                esum.insert(1,1)
                break
            suma=str(a[0][i]+b[0][i])
            suma=int(suma[1])
            a[0][i-1]=a[0][i-1]+1
        #Ingresa el valor al vector resultado.
        esum[i]=suma
    
    m=(esum,dsum)
    return m

#======================================================================
#================================Resta1================================
#Esta no es la función resta que pide el profesor.
def resta1(a,b):    
    a=safe(a)
    b=safe(b)
    #Define la longitud de cada parte de las tuplas.
    all0=len(a[0])
    all1=len(a[1])
    bll0=len(b[0])
    bll1=len(b[1])
    
    #--------------------Completa con 0 casillas-----------------
    
    if all0>bll0:
        ss=all0-bll0    
        for i in range(ss):
            b[0].insert(1,0)    
    elif all0<bll0:
        ss=bll0-all0    
        for i in range(ss):
            a[0].insert(1,0)    
    if all1>bll1:
        ss=all1-bll1    
        for i in range(ss):
            b[1].insert(bll1,0)    
    elif all1<bll1:
        ss=bll1-all1    
        for i in range(ss):
            a[1].insert(all1,0)    
    
    alle=len(a[0])
    alld=len(a[1])
    eres=list(range(alle))
    dres=list(range(alld))
    #---------------------------Funciones-------------------------
    o=10**(alle-2)
    cuenta=0
    cuenta1=0
    for i in range(alle):
        if i>0:
            compa=(a[0][i]-b[0][i])*o
            cuenta=cuenta+compa
            o-=9*10**(alle-i-2)
    if cuenta<0:
        for i in range(alle):
            a[0][i],b[0][i]=b[0][i],a[0][i]
        for i in range(alld):
            a[1][i],b[1][i]=b[1][i],a[1][i]
    elif cuenta==0:
        oi=10**(alld-1)
        cuenta=0
        for i in range(alld):
            compa=(a[1][i]-b[1][i])*oi
            cuenta1=cuenta1+compa
            oi-=9*10**(alld-i-2)
            if cuenta1<0:
                for i in range(alle):
                    a[0][i],b[0][i]=b[0][i],a[0][i]
                for i in range(alld):
                    a[1][i],b[1][i]=b[1][i],a[1][i]
                break
                
    for i in range(alld-1,-1,-1):
            resta=a[1][i]-b[1][i]
            #Por si el número de arriba es más grande.
            if resta<0:
                #Por si está en el dígito de la coma.
                if i==0:
                    #Le agrega 10 al número de ''arriba'' y resta.
                    resta=a[1][i]+10-b[1][i]
                    #Quita uno al siguiente dígito.
                    a[0][alle-1]=a[0][alle-1]-1
                #Para los demás.
                else:
                    #Le agrega 10 al número de ''arriba'' y resta.
                    resta=a[1][i]+10-b[1][i]
                    #Quita uno al siguiente dígito.
                    a[1][i-1]=a[1][i-1]-1
            #Ingresa el valor al vector resultado.
            dres[i]=resta
            
    for i in range(alle-1,-1,-1):
        if i==0:
            break
        resta=a[0][i]-b[0][i]
        #Por si el número de arriba es más grande.
        if resta<0:
            #Le agrega 10 al número de ''arriba'' y resta.
            resta=a[0][i]+10-b[0][i]
            #Quita uno al siguiente dígito.
            a[0][i-1]=a[0][i-1]-1
        #Ingresa el valor al vector resultado.
        eres[i]=resta
    
    signa=a[0][0]
    m=(eres,dres)
    return m,signa
#################################### HASTA ACÁ LAS ADICIONALES ################

def suma(a, b):
    signa=a[0][0]
    signb=b[0][0]
    if signa==signb: #Si los signos son iguales suma y si no, resta.
        ss=suma1(a,b)
        ss[0][0]=signa 
        return ss
    elif signa!=signb:
        rr,rr[0][0]=resta1(a,b)
        return rr
    
def resta(a, b):
    signa=a[0][0]
    signb=b[0][0]
    if signa!=signb: #Si los signos son iguales resta y si no, suma.
        ss=suma1(a,b)
        ss[0][0]=signa
        return ss
    elif signa==signb:
        rr,rr[0][0]=resta1(a,b)
        return rr
    
def multiplicacion(a, b):
    a1=safe(a)
    b1=safe(b)
    a=safe(a)
    b=safe(b)
    #Defino los tamaños que requiero. Se asume a arriba y b abajo.
    all0=len(a[0])
    all1=len(a[1])
    bll0=len(b[0])
    bll1=len(b[1])
    allt=all0+all1-1
    bllt=bll0+bll1-1
    
    if all0==1:
        a[0].insert(1,0)
    if bll0==1:
        b[0].insert(1,0)
    if all1==0:
        a[1].insert(1,0)
    if bll1==0:
        b[1].insert(1,0)
    
    all0=len(a[0])
    all1=len(a[1])
    bll0=len(b[0])
    bll1=len(b[1])
    allt=all0+all1-1
    bllt=bll0+bll1-1

    #Crea una lista que va a albergar las listas de mult.parcial.
    c=list(range(bllt))
    
    #Crear un vector resultado con la longitud total, tal que
    #es una lista decimal con las posiciones ya definidas.
    resmulti=[list(range(allt+bllt))]
    for p in range(allt+bllt):
        resmulti[0][p]=resmulti[0][p]*0
    
    #"Translada los números decimales a la parte entera de las listas
    for i in range(all1):
        a[0].insert(all0+i,a[1].pop(0))
    for j in range(bll1):
        b[0].insert(bll0+j,b[1].pop(0))
    
    #Crea los espacios completos
    for k in range(bllt): #Para cada lista creada
        c[k]=[] #Hace una con la cantidad de elementos de a
        for q in range(allt):
            c[k].insert(0,0)

    #Multiplica
    for l in range(bllt):#Toma los valores de b
        for m in range(allt):#Toma los valores de a
            #c se toma desde la izquierda. b crece lento con l y a rápido con m.
            c[l][allt-m-1]=a[0][allt-m]*b[0][bllt-l]+c[l][allt-m-1]
            if c[l][allt-m-1]>9:
                if m==(allt-1):
                    c[l][allt-m-1]=str(c[l][allt-m-1]) #Convierte a str.
                    pd=int(c[l][allt-m-1][0]) #Guarda el valor del primer dígito.
                    c[l][allt-m-1]=int(c[l][allt-m-1][1]) #Vuelve a c el segundo dígito.
                    c[l].insert(0,pd) #Suma lo que lleva al siguiente.
                else:
                    c[l][allt-m-1]=str(c[l][allt-m-1]) #Convierte a str.
                    pd=int(c[l][allt-m-1][0]) #Guarda el valor del primer dígito.
                    c[l][allt-m-1]=int(c[l][allt-m-1][1]) #Vuelve a c el segundo dígito.
                    c[l][allt-m-2]=c[l][allt-m-2]+pd #Suma lo que lleva al siguiente.
              
    #Aumenta los números mediante el cero.
    for m in range(bllt):
        if len(c[m])==allt:
            for n in range(bllt,m,-1):
                c[m].insert(0,0)
        else:
            for n in range(bllt-1,m,-1):
                c[m].insert(0,0)
    for m in range(bllt):
        c[m]=c[m][::-1] #Los voltea para garantizar que quedarán al extremo
        n=0
        if n<m:
            while n<m:
                c[m].insert(0,0)
                n+=1
        c[m]=c[m][::-1]#Los regresa a su posición inicial.
        
    #Suma los números:
    clli=len(c[0])
    for h in range(bllt):
        for g in range(clli):
            resmulti[0][clli-g-1]=c[h][clli-g-1]+resmulti[0][clli-g-1]
            if resmulti[0][clli-g-1]>9:
                resmulti[0][clli-g-1]=str(resmulti[0][clli-g-1])
                resmulti[0][clli-g-1]=int(resmulti[0][clli-g-1][1])
                c[h][clli-g-2]=c[h][clli-g-2]+1
    
    #Quita el primer cero en caso de que se de
    if resmulti[0][0]==0:
        resmulti[0].pop(0)
    
    resl=len(resmulti[0])
    #Vuelve la lista decimal.
    resmulti.insert(1,list()) #Crea la parte decimal
    for i in range(all1+bll1):
        resmulti[1].insert(0,resmulti[0].pop(resl-i-1))

    #Incluye el signo.
    if a[0][0]==b[0][0]:
        resmulti[0].insert(0,"+")
    elif a[0][0]!=b[0][0]:
        resmulti[0].insert(0,"-")

    #Convierte la lista en tupla para que la lea imprimir.
    mm=(resmulti[0],resmulti[1])
    a=a1
    b=b1
    return mm


def division(a, b):
    pass


def comparacion(a, b):
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


def pi():
    pass


if __name__ == "__main__":
    print(imprimir(pi()))
