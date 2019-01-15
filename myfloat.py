class MyFloat:

    class MyFloat:
#=======================================================================#
#================================Init===================================#
#=======================================================================#
    def __init__(self,tupla):
        self.aa=tupla
        
#=======================================================================#
#================================Safe===================================#
#=======================================================================#
    def safe(a): #Genera una copia de la tupla a, evita modificar la tupla.
        ent=a[0][:]
        dec=a[1][:]
        b=(ent,dec)
        return b
#=======================================================================#
#=============================== Add ===================================#  
#=======================================================================#
    def __add__(self,other,sincero=1):
        #Se guardan
        self.a=MyFloat.safe(self.aa)
        other.a=MyFloat.safe(other.aa)
        #Quito y guardo el signo
        signa=self.a[0].pop(0)
        signb=other.a[0].pop(0)
        #Guardo cuántos decimales hay
        deca=len(self.a[1])
        decb=len(other.a[1])
        #Igualo la parte decimal
        if deca>decb: #a mayor
            for i in range(deca-decb):
                other.a[1].append(0) 
        if decb>deca: #b mayor
            for i in range(decb-deca):
                self.a[1].append(0)
        deca=len(self.a[1])
        #Igualo la parte entera
        if len(self.a[0])>len(other.a[0]):
            for i in range(len(self.a[0])-len(other.a[0])):
                other.a[0].insert(0,0)    
        if len(other.a[0])>len(self.a[0]):
            for i in range(len(other.a[0])-len(self.a[0])):
                self.a[0].insert(0,0)
        #Paso la parte decimal a la misma lista del entero
        for i in range(len(self.a[1])):
            self.a[0].insert(len(self.a[0]),self.a[1].pop(0))
        for i in range(len(other.a[1])):
            other.a[0].insert(len(other.a[0]),other.a[1].pop(0))
        #Busco el más grande
        for i in range(len(self.a[0])):
            comp=self.a[0][i]-other.a[0][i]
            if comp<0:
                signa,signb=signb,signa
                for k in range(len(self.a[0])):
                    self.a[0][k],other.a[0][k]=other.a[0][k],self.a[0][k] #En caso de que b sea más grande lo ubica en a
                break
            elif comp>0:
                break
        #Crea la lista resultado
        resul=[]
        for i in range(len(self.a[0])):
            resul.insert(0,0)
        #Opera
        if signa==signb: #Signos iguales suma
            for i in range(len(self.a[0])-1,-1,-1): #Toma valores de mayor a menor para la longitud
                aux=self.a[0][i]+other.a[0][i] #Suma el valor que haya en cada lista
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
            for i in range(len(self.a[0])-1,-1,-1):
                aux=self.a[0][i]-other.a[0][i] #Resta los valores de cada lista
                if aux<0:
                    resul[i]+=10
                    self.a[0][i-1]-=1
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
    def __sub__(self,other):
        #Se guardan
        self.a=MyFloat.safe(self.aa)
        other.a=MyFloat.safe(other.aa)
        signa=self.a[0][0]
        signb=other.a[0][0]
        if signa!=signb:
            other.a[0][0]=self.a[0][0]
        elif signa==signb:
            if signa=='+':
                other.a[0][0]='-'
            elif signa=='-':
                other.a[0][0]='+'
        return MyFloat(self.a)+MyFloat(other.a)

    #=======================================================================
    #===========================Multiplicación==============================
    #=======================================================================
    def __mul__(self,other):
        #Se guardan
        self.a=MyFloat.safe(self.aa)
        other.a=MyFloat.safe(other.aa)
        #Quito y guardo el signo
        signa=self.a[0].pop(0)
        signb=other.a[0].pop(0)
        #Guardo cuántos decimales hay
        deca=len(self.a[1])
        decb=len(other.a[1])
        #Paso la parte decimal a la misma lista del entero
        for i in range(len(self.a[1])):
            self.a[0].insert(len(self.a[0]),self.a[1].pop(0))
        for i in range(len(other.a[1])):
            other.a[0].insert(len(other.a[0]),other.a[1].pop(0))
        #Creo una lista que contendrá el resultado de cada multiplicación como una lista
        resul=[]
        for i in range(len(other.a[0])):
            resul.append([0]*(len(self.a[0])+1+i)) #Creo los ceros a la derecha que permitirán sumar estas listas
            for j in range(len(self.a[0])):
                #Multiplica y acomoda a la izquierda (len(resul)-i-1) de los ceros
                mul=self.a[0][len(self.a[0])-j-1]*other.a[0][len(other.a[0])-i-1]
                if mul>9: #Soluciona el que en una casilla la multiplicación de dos dígitos
                    mul=str(mul)
                    lleva,mul=int(mul[0]),int(mul[1])
                    resul[i][len(self.a[0])-j]+=mul
                    resul[i][len(self.a[0])-j-1]+=lleva
                else: #Otro caso
                    resul[i][len(self.a[0])-j]+=mul
                parcial=resul[i][len(self.a[0])-j]
                if parcial>9: #Soluciona el que al sumar lo que se llevaba, nuevamente de dos dígitos
                    parcial=str(parcial)
                    lleva1,parcial1=parcial[0],parcial[1]
                    lleva1,parcial1=int(lleva1),int(parcial1)
                    resul[i][len(self.a[0])-j]=parcial1
                    resul[i][len(self.a[0])-j-1]+=lleva1
            resul[i].insert(0,'+') #Agrega el signo a la lista
            resul[i]=(resul[i],[]) #Vuelve esa lista una tupla
        cuenta=(['+',0],[]) #Crea la lista que llevará la suma
        for i in range(len(resul)):
            cuenta=MyFloat.__add__(MyFloat(cuenta),MyFloat(resul[i]),0) #suma todas las listas de resul (los escalones)
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
    def __div__(self,other,cifras=100):  
        #Se guardan
        self.a=MyFloat.safe(self.aa)
        other.a=MyFloat.safe(other.aa)
        #Guardo los signos y los vuelvo positivos (para asegurar restar efectivamente)
        signa=self.a[0][0]
        signb=other.a[0][0]
        self.a[0][0]='+'
        other.a[0][0]='+'
        #Paso la parte decimal a la misma lista del entero
        diva=0 #Los contadores de las veces que se 'dividió' por 10
        divb=0
        for i in range(len(self.a[1])):
            self.a[0].insert(len(self.a[0]),self.a[1].pop(0))
            diva+=1
        for i in range(len(other.a[1])):
            other.a[0].insert(len(other.a[0]),other.a[1].pop(0))
            divb+=1   
        #En caso de que a sea menor que b:
        cuentadiez=0 #Cuántas veces se multiplicó por diez
        diez=(['+',1,0],[])
        for i in range(len(other.a[0])-len(self.a[0])):
            self.a=MyFloat(self.a)*MyFloat(diez)
            cuentadiez+=1
        #Divide
        seccion=(['+'],[]) #La sección de 'a' a usar
        for i in range(len(other.a[0])-1): #quita uno por el signo
            seccion[0].insert(len(seccion[0]),self.a[0][i+1])
        cociente=(['+'],[])
        for j in range(len(self.a[0])-len(other.a[0])+1): #Mediante este hallo toda la parte entera
            for i in range(11): #Ciclo for destinado a hallar el siguiente dígito de cociente
                candidato=(['+',i],[]) #El número por el que va a multiplicar (en tupla)
                busca=MyFloat(other.a)*MyFloat(candidato) 
                resto=MyFloat(seccion)-MyFloat(busca)
                if resto[0][0]=='-':
                    candidato=(['+',i-1],[]) #Estas tres lineas que siguen es para hacer lo mismo...
                    busca=MyFloat(other.a)*MyFloat(candidato) #... pero con el número anterior, pues candidato...
                    resto=MyFloat(seccion)-MyFloat(busca) #... se pasa para lograr el negativo
                    seccion=resto #los primeros digitos de seccion son resto
                    cociente[0].insert(len(cociente[0]),candidato[0][1]) #Guarda el candidato en insert
                    #print(busca,resto,candidato)
                    if j==len(self.a[0])-len(other.a[0]): #Range llega hasta un número antes, por eso aquí no hay +1
                        break #Se rompe pues no hay más números para 'bajar'
                    seccion[0].insert(len(seccion[0]),self.a[0][len(other.a[0])+j]) #'Baja' el siguiente número
                    #print(busca,resto,candidato)
                    break
        if seccion[0][1]!=0: #Si la división no es exacta
            seccion[0].insert(len(seccion[0]),0) #Se anexa un cero por haber llegado a la coma
            for j in range(cifras):
                for i in range(11): 
                    candidato=(['+',i],[]) 
                    busca=MyFloat(other.a)*MyFloat(candidato) 
                    resto=MyFloat(seccion)-MyFloat(busca)
                    if resto[0][0]=='-':
                        candidato=(['+',i-1],[])
                        busca=MyFloat(other.a)*MyFloat(candidato) 
                        resto=MyFloat(seccion)-MyFloat(busca)
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
                    cociente=MyFloat(cociente)*MyFloat(diez)
            elif potencia<0:
                for i in range(-potencia):
                    cociente=MyFloat(cociente)*MyFloat(cerouno)
        #Para correr las cifras decimales que se corrieron al multiplicar por diez en valores pequeños.
        if cuentadiez>0:
            for i in range(cuentadiez):
                cociente=MyFloat(cociente)*MyFloat(cerouno)
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
 
#=======================================================================#
#================================= R's =================================#  
#=======================================================================#
    def __radd__(self,other):
        MyFloat.__add__(other,self)

    def __rsub__(self,other):
        MyFloat.__sub__(other,self)

    def __rmul__(self):
        MyFloat.__mul__(other,self)

    def __rdiv__(self):
        MyFloat.__div__(other,self)
        
#=======================================================================#
#=================================Str===================================#  
#=======================================================================#
    def __str__(self):
        inte=str()
        intd=str()
        for i in range(len(self.a[0])):
            inte=inte+str(self.a[0][i])
        for i in range(len(self.a[1])):
            intd=intd+str(self.a[1][i])
        intt=inte+","+intd
        return intt
    
#=======================================================================#
#================================Repr===================================#  
#=======================================================================#
    def __repr__(self):
        self.a=MyFloat.safe(self.aa)
        pc=len(self.a[0])
        sc=len(self.a[1])
        temp=0
        entero=""
        decimal=""
    
        for i in range (pc):
            temp=str(self.a[0][i])
            entero=str(entero)+temp
        for j in range (sc):
            temp=str(self.a[1][j])
            decimal=str(decimal)+temp
        return ("{},{}".format(entero,decimal))
    
#=======================================================================#
#================================ Eq ===================================#  
#=======================================================================#
    def __eq__(self,other):
        con=2
        lona=len(self.a)
        lonb=len(other.a)
        if lona!=lonb:
          print("Son tuplas diferentes")
          con=0
        elif lona==lonb:
          for i in range(lona):
            ver1=lona-1
            loninta=len(self.a[i])
            lonintb=len(other.a[i])
            if loninta!=lonintb:
              print("Son tuplas diferentes")
              con=0
              break
            elif loninta==lonintb:
              for j in range(loninta):
                ver2=loninta-1
                x=self.a[i][j]
                y=other.a[i][j]
                if x!=y:
                  print("Son tuplas diferentes")
                  con=0
                  break
                elif i==ver1:
                  if j==ver2:
                    print("Son tuplas iguales")
                    con=1
            if x!=y:
              con=0
              break
            if con==1:
                return True
            elif con==0:
                return False
            
#=======================================================================#
#================================ Ne ===================================#  
#=======================================================================#
    def __ne__(self,other):
        if MyFloat.__eq__(other,self)==True:
            return False
        elif MyFloat.__eq__(other,self)==False:
            return True
            
if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    cuatro=MyFloat((['+',4],[]))
    dos=MyFloat((['+',2],[]))
    uno=MyFloat((['+',1],[]))
    menosuno=MyFloat((['-',1],[]))
    dividendo=MyFloat((['-',1],[]))
    cuenta=MyFloat((['+',0],[]))
    kha=MyFloat((['-',1],[]))
    for k in range(1000000):
        kha=MyFloat(uno+kha)
        dosk=MyFloat(dos*kha)
        divisor=MyFloat(dosk+uno)
        dividendo=MyFloat(menosuno*dividendo)
        total=MyFloat(MyFloat.__div__(dividendo,divisor,30))
        cuenta=MyFloat(cuenta+total)
    pi=MyFloat(cuatro*cuenta)
    print(pi)
