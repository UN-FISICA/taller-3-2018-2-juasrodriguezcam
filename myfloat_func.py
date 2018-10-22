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

#=======================================================================
#===============================Suma====================================
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
    signa=a[0][0]
    signb=b[0][0]
    #---------------------------Funciones-------------------------
    o=10**(alle-2)
    cuenta=0
    cuenta1=0
    for i in range(alle):
        if i>0:
            compa=(a[0][i]-b[0][i])*o
            cuenta=cuenta+compa
            o-=9*10**(alle-i-2) 
    if cuenta<0: #intercambia el orden de la tupla dependiendo del entero
        for i in range(alle):
            a[0][i],b[0][i]=b[0][i],a[0][i]
        for i in range(alld):
            a[1][i],b[1][i]=b[1][i],a[1][i]
        signa=a[0][0]
        signb=b[0][0]
        if signa==signb:
            if signa=="+":
                signa="-"
            elif signa=="-":
                signa="+"
    elif cuenta==0: #intercambia el orden de la tupla dependiendo del decimal
        oi=10**(alld-1)
        for i in range(alld):
            compa=(a[1][i]-b[1][i])*oi
            cuenta1=cuenta1+compa
            oi-=9*10**(alld-i-2)    
            if cuenta1<0:
                for i in range(alle):
                    a[0][i],b[0][i]=b[0][i],a[0][i]
                for i in range(alld):
                    a[1][i],b[1][i]=b[1][i],a[1][i]
                signa=a[0][0]
                signb=b[0][0]
                if signa==signb:
                    if signa=="+":
                        signa="-"
                    elif signa=="-":
                        signa="+"
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
    
    m=(eres,dres)
    return m,signa
    
#========================================================================
#==============================Suma======================================

def suma(a,b):
    signa=a[0][0]
    signb=b[0][0]
    if signa==signb: #Si los signos son iguales suma y si no, resta.
        ss=suma1(a,b)
        ss[0][0]=signa 
        return ss
    elif signa!=signb:
        rr,rr[0][0]=resta1(a,b)
        return rr

#=======================================================================
#==============================Resta====================================

def resta(a,b):
    signa=a[0][0]
    signb=b[0][0]
    if signa!=signb: #Si los signos son iguales resta y si no, suma.
        ss=suma1(a,b)
        ss[0][0]=signa
        return ss
    elif signa==signb:
        rr,rr[0][0]=resta1(a,b)
        return rr

#=======================================================================
#===========================Multiplicación==============================
def multiplicacion(a,b):
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
    #Quita los ceros adicionales atrás
    
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
    
    while resmulti[0][1]==0:
        if len(resmulti[0])==2:
            break
        else:
            resmulti[0].pop(0)  
            
    #Convierte la lista en tupla para que la lea imprimir.
    mm=(resmulti[0],resmulti[1])
    a=a1
    b=b1
    return mm

#=======================================================================
#============================División===================================
def division(a,b,cifrasd=100):  
    a=safe(a)
    b=safe(b)
    #Borro ceros a la izquierda:
    while len(a[0])>1:
        if a[0][1]==0:
            a[0].pop(1)
        else:
            break
    while len(b[0])>1:
        if b[0][1]==0:
            b[0].pop(1)
        else:
            break        
    
    #Borro ceros a la derecha:
    while a[1][len(a[1])-1]==0:
        if len(a[1])-1==0:
            break
        a[1].pop(len(a[1])-1)
    while b[1][len(b[1])-1]==0:
        if len(b[1])-1==0:
            break
        b[1].pop(len(b[1])-1)
        
    #Defino longitudes
    all0=len(a[0])
    all1=len(a[1])
    bll0=len(b[0])
    bll1=len(b[1])
    
    #Borro el último cero adicional
    if all1==1:
        if a[1][len(a[1])-1]==0:
            a[1].pop(len(a[1])-1)
            all1=len(a[1])
    if bll1==1:
        if b[1][len(b[1])-1]==0:
            b[1].pop(len(b[1])-1)
            bll1=len(b[1])
    
    #Paso a la parte decimal
    for i in range(all0-1):
        a[1].insert(0,a[0].pop(all0-i-1))
    for i in range(bll0-1):
        b[1].insert(0,b[0].pop(bll0-i-1))
        
    #Tomo la nueva longitud
    alla=len(a[1])
    bllb=len(b[1])
    difll=alla-bllb #Diferencia entre todos los valores
    ff=0

    if difll<0:
        for i in range(abs(difll)):
            a[1].insert(len(a[1]),0)
            all0+=1
            ff+=1
            
    alla=len(a[1])
    bllb=len(b[1])
    difll=alla-bllb
    
    difeea=alla-all0+1 
    difeeb=bllb-bll0+1
    dife=difeea-difeeb
    #Creo la lista del cociente:
    cocientee=[]
    cociented=[]
    
    ############## La cuestión es cómo llegar hasta la coma #################
    #Que lena<lenb:
    def cocientef(a,b):
        a=safe(a)
        b=safe(b)
        
        #Defino longitudes
        all0=len(a[0])
        bll0=len(b[0])
        #Paso a la parte decimal
        for i in range(all0-1):
            a[1].insert(0,a[0].pop(all0-i-1))
        for i in range(bll0-1):
            b[1].insert(0,b[0].pop(bll0-i-1))
        #Tomo la nueva longitud
        alla=len(a[1])
        bllb=len(b[1])
        difll=alla-bllb
        #Creo la lista del cociente:
        cocientee=[]
        ddivis=(['+'],[])
        ddividen=(["+"],[])
        for i in range(bllb):
            #Copio el divisor a la lista ddivis
            ddivis[1].insert(i,b[1][i])
            ddivisu=safe(ddivis)
            ddividen[1].insert(bllb-1,a[1][i])
        while difll>=0:
            cuenta1=0
            aux2=len(ddividen[1])-len(ddivis[1])
            if aux2>0:
                ddivisu[1].insert(0,0)
                bllb+=1
            compal2=([],[])
            for i in range(11):
                #multiplico ddivis por el candidato a siguiente número
                deter=multiplicacion(ddivisu,(['+'],[i]))
                if deter[1][0]==0:# Dada la definición, puede haber un 0 adicional
                    deter[1].pop(0)
                o=10**(bllb-1)
                cuenta=0
                #print(ddividen,deter,ddivis)
                compal=resta(safe(ddividen),deter)
                for j in range(bllb):# Hace la cuenta del resto
                    intcompa=str()
                    for t in range(len(compal[1])):
                        intcompa=str(compal[1][len(compal[1])-1-t])+intcompa
                    compa=int(intcompa[j])*o
                    cuenta=cuenta+compa #Crea el resto
                    o-=9*10**(bllb-j-2)
                    if i>0:
                        if cuenta>cuenta1:
                            compal[0][0]="-"
                    #print(cuenta1, cuenta,deter,i,j,compal, difll, dife)
                    if compal[0][0]=="-": #Cuando encuentre el número
                        cuenta1=str(cuenta1)
                        cuenta2=(['+'],[])
                        for k in range(len(cuenta1)):
                            cuenta2[1].insert(k,int(cuenta1[k]))
                        ddividen=safe(cuenta2) #El nuevo dividendo es cuenta2
                        for s in range(len(compal2[1])):
                            if compal2[1][s]!=0:
                                break
                            if s>0:
                                if compal2[1][s]==0:
                                    ddividen[1].insert(0,0)
                        cocientee.insert(len(cocientee),i-1) #+Cociente
                        if difll==0:
                            break
                        ddividen[1].insert(len(ddividen[1]),a[1][alla-difll])# "Baja el siguiente dig.."
                        break
                    aux=bllb-1
                    if j==aux:
                        cuenta1=cuenta
                        compal2=safe(compal)
                if compal[0][0]=="-": #Como ya encontró el número, no tiene que seguir.
                    if aux2>0:
                        ddivisu=safe(ddivis)
                        bllb-=1
                        aux5=len(ddividen[1])-len(ddivis[1])
                        while aux5>1:
                            ddividen[1].pop(0)
                            aux5=len(ddividen[1])-len(ddivis[1])
                    break  
            if difll==0:
                break
            difll=difll-1
        return cocientee
    
    #Si el número a dividir tiene más decimales
    if dife>0:
        cocientee=cocientef(a,b) #Crea la parte entera
        if dife<len(cocientee):
            for i in range(dife):
                cocientee.pop(len(cocientee)-1)#Quita dígitos decimales como dife diga
            while cocientee[0]==0:
                cocientee.pop(0)
                if len(cocientee)==0:
                    cocientee=[0]
                    break 
            for i in range(cifrasd): #Aumenta a para dar más dígitos decimales
                a[1].insert(len(a[1]),0)    
            cociented=cocientef(a,b) #Crea la parte decimal
            for i in range(len(cocientee)):
                cociented.pop(0) #Quita dígitos enteros como haya en la parte entera
            while len(cociented)>cifrasd:
                cociented.pop(len(cociented)-1)
                
        elif dife>=len(cocientee):
            lenc=len(cocientee)
            #print(cocientee)
            while cocientee[0]==0:
                cocientee.pop(0)
                if len(cocientee)==0:
                    cociented=[0]
            cocientee=[0]
            for i in range(cifrasd+len(cocientee)): #Aumenta a para dar más dígitos decimales
                a[1].insert(len(a[1]),0)    
            cociented=cocientef(a,b) #Crea la parte decimal
            for i in range(len(cocientee)-1):
                cociented.pop(0) #Quita dígitos enteros como haya en la parte entera
                if len(cociented)==0:
                    cociented=[0] #Si no hay más para quitar, pone un cero
            if dife>len(cocientee): #A medida que es muy grande, agrega ceros en la parte decimal
                for i in range(dife-lenc):
                    cociented.insert(0,0)
            while len(cociented)>cifrasd: #Al final asegura dcifras cifras decimales
                cociented.pop(len(cociented)-1)
            
    #Si el número a dividir tiene menos decimales
    elif dife<0:
        for i in range(abs(dife)):
            a[1].insert(len(a[1]),0)
        cocientee=cocientef(a,b) 
        while cocientee[0]==0:
            cocientee.pop(0)
            if len(cocientee)==0:
                cocientee=[0]
                break
        for i in range(cifrasd+len(cocientee)): #Aumenta a para dar más dígitos decimales
            a[1].insert(len(a[1]),0)
        cociented=cocientef(a,b) #Crea la parte decimal
        for i in range(len(cocientee)):
            cociented.pop(0) #Quita dígitos enteros como haya en la parte entera
        while len(cociented)>cifrasd: #Al final asegura dcifras cifras decimales
                cociented.pop(len(cociented)-1)
    #Si tienen los mismos decimales
    else:
        aint=str()
        bint=str()
        for i in range(len(a[1])):
            aint=aint+str(a[1][i])
        for i in range(len(b[1])):
            bint=bint+str(b[1][i])
        if int(aint)<int(bint):
            a[1].insert(len(a[1]),0)
            cocientee=cocientef(a,b)
            while cocientee[0]==0:
                cocientee.pop(0)
                if len(cocientee)==0:
                    break
            cocientee.pop(len(cocientee)-1)
            if len(cocientee)==0:
                cocientee=[0]
            for i in range(cifrasd+len(cocientee)): #Aumenta a para dar más dígitos decimales
                a[1].insert(len(a[1]),0)    
            cociented=cocientef(a,b) #Crea la parte decimal
            for i in range(ff):
                cociented.insert(0,0)
            for i in range(len(cocientee)):
                cociented.pop(0) #Quita dígitos enteros como haya en la parte entera
            while len(cociented)>cifrasd: #Al final asegura dcifras cifras decimales
                    cociented.pop(len(cociented)-1)
        
        else:
            cocientee=cocientef(a,b)
            while cocientee[0]==0:
                cocientee.pop(0)
                if len(cocientee)==0:
                    cocientee=[0]
                    break
            for i in range(cifrasd+len(cocientee)): #Aumenta a para dar más dígitos decimales
                a[1].insert(len(a[1]),0)    
            cociented=cocientef(a,b) #Crea la parte decimal
            for i in range(len(cocientee)):
                cociented.pop(0) #Quita dígitos enteros como haya en la parte entera
            while len(cociented)>cifrasd: #Al final asegura dcifras cifras decimales
                    cociented.pop(len(cociented)-1)
                 
    cociente=(cocientee,cociented)
    #Incluye el signo.
    if a[0][0]==b[0][0]:
        cociente[0].insert(0,"+")
    elif a[0][0]!=b[0][0]:
        cociente[0].insert(0,"-")
    
    return cociente
 
#========================================================================
#===========================Comparación==================================
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

def pi():
    aa=49
    cc=0
    sumar=(['+',0],[0])
    while cc<=aa:
        kk=(['+',cc],[0])
        pot=(['+',1],[0])
        for i in range(cc):
            pot=multiplicacion((['-',1],[0]),pot)
        denominador=suma(multiplicacion(kk,(['+',2],[0])),(['+',1],[0]))
        sumar=suma(sumar,division(pot,denominador,29))
        cc+=1
    return multiplicacion(sumar,(['+',4],[0]))


if __name__ == "__main__":
    print(imprimir(pi()))
