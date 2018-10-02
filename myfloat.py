class MyFloat:

    def __init__(self, tupla):
        self.enter=tupla[0]
        self.deci=tupla[1]
        self.sa=(self.enter,self.deci)
        self.a=MyFloat.safe(self.sa)
       
    #Función adicional para solucionar el problema en el punto de las funciones.
    def safe(a): #Genera una copia de la tupla a, evita modificar la tupla.
        ent=a[0][:]
        dec=a[1][:]
        b=(ent,dec)
        return b
    
    ############################Nuevamente las funciones adicionales:
    #Esta no es la función suma que el profesor pide
    def suma1(self,other):
        self.a=MyFloat.safe(self.sa)
        #Define la longitud de cada parte de las tuplas.
        all0=len(self.a[0])
        all1=len(self.a[1])
        bll0=len(other.a[0])
        bll1=len(other.a[1])
        
        #--------------------Completa con 0 casillas-----------------
        
        if all0>bll0:
            ss=all0-bll0    
            for i in range(ss):
                other.a[0].insert(1,0)    
        elif all0<bll0:
            ss=bll0-all0    
            for i in range(ss):
                self.a[0].insert(1,0)    
        if all1>bll1:
            ss=all1-bll1    
            for i in range(ss):
                other.a[1].insert(bll1,0)    
        elif all1<bll1:
            ss=bll1-all1    
            for i in range(ss):
                self.a[1].insert(all1,0)    
        
        alle=len(self.a[0])
        alld=len(self.a[1])
        esum=list(range(alle))
        dsum=list(range(alld))
                    
        #-----------------------------Suma-----------------------------
        for i in range(alld-1,-1,-1):
                suma=self.a[1][i]+other.a[1][i]
                #Por si el número de arriba es más grande.
                if suma>9:
                    #Por si está en el dígito de la coma.
                    if i==0:
                        #Toma la suma cono str.
                        suma=str(self.a[1][i]+other.a[1][i])
                        #suma se vuelve el segundo dígito.
                        suma=int(suma[1])
                        #Suma uno al siguiente dígito.
                        self.a[0][alle-1]=self.a[0][alle-1]+1
                    #Para los demás.
                    else:
                        suma=str(self.a[1][i]+other.a[1][i])
                        suma=int(suma[1])
                        self.a[1][i-1]=self.a[1][i-1]+1
                #Ingresa el valor al vector resultado.
                dsum[i]=suma
                
        for i in range(alle-1,-1,-1):
            if i==0:
                break
            suma=self.a[0][i]+other.a[0][i]
            #Por si el número de arriba es más grande.
            if suma>9:
                if i==1:
                    suma=str(self.a[0][i]+other.a[0][i])
                    suma=int(suma[1])
                    esum[i]=suma
                    esum.insert(1,1)
                    break
                suma=str(self.a[0][i]+other.a[0][i])
                suma=int(suma[1])
                self.a[0][i-1]=self.a[0][i-1]+1
            #Ingresa el valor al vector resultado.
            esum[i]=suma
            
        m=(esum,dsum)
        return m
    
#=======================================================================#
#==============================Resta 1==================================#
#=======================================================================#
    #Esta no es la función resta que pide el profesor.
    def resta1(self,other):    
        self.a=MyFloat.safe(self.sa)
        #Define la longitud de cada parte de las tuplas.
        all0=len(self.a[0])
        all1=len(self.a[1])
        bll0=len(other.a[0])
        bll1=len(other.a[1])
        
        #--------------------Completa con 0 casillas-----------------
        
        if all0>bll0:
            ss=all0-bll0    
            for i in range(ss):
                other.a[0].insert(1,0)    
        elif all0<bll0:
            ss=bll0-all0    
            for i in range(ss):
                self.a[0].insert(1,0)    
        if all1>bll1:
            ss=all1-bll1    
            for i in range(ss):
                other.a[1].insert(bll1,0)    
        elif all1<bll1:
            ss=bll1-all1    
            for i in range(ss):
                self.a[1].insert(all1,0)    
        
        alle=len(self.a[0])
        alld=len(self.a[1])
        eres=list(range(alle))
        dres=list(range(alld))
        #---------------------------Funciones-------------------------
        o=10**(alle-2)
        cuenta=0
        for i in range(alle):
            if i>0:
                compa=(self.a[0][i]-other.a[0][i])*o
                cuenta=cuenta+compa
                o-=9*10**(alle-i-2)
        if cuenta<0:
            for i in range(alle):
                self.a[0][i],other.a[0][i]=other.a[0][i],self.a[0][i]
            for i in range(alld):
                self.a[1][i],other.a[1][i]=other.a[1][i],self.a[1][i]
                    
        for i in range(alld-1,-1,-1):
                resta=self.a[1][i]-other.a[1][i]
                #Por si el número de arriba es más grande.
                if resta<0:
                    #Por si está en el dígito de la coma.
                    if i==0:
                        #Le agrega 10 al número de ''arriba'' y resta.
                        resta=self.a[1][i]+10-other.a[1][i]
                        #Quita uno al siguiente dígito.
                        self.a[0][alle-1]=self.a[0][alle-1]-1
                    #Para los demás.
                    else:
                        #Le agrega 10 al número de ''arriba'' y resta.
                        resta=self.a[1][i]+10-other.a[1][i]
                        #Quita uno al siguiente dígito.
                        self.a[1][i-1]=self.a[1][i-1]-1
                #Ingresa el valor al vector resultado.
                dres[i]=resta
                
        for i in range(alle-1,-1,-1):
            if i==0:
                break
            resta=self.a[0][i]-other.a[0][i]
            #Por si el número de arriba es más grande.
            if resta<0:
                #Le agrega 10 al número de ''arriba'' y resta.
                resta=self.a[0][i]+10-other.a[0][i]
                #Quita uno al siguiente dígito.
                self.a[0][i-1]=self.a[0][i-1]-1
            #Ingresa el valor al vector resultado.
            eres[i]=resta
        
        signa=self.a[0][0]
        m=(eres,dres)
        return m,signa
    ######################################### HASTA ACÁ LAS ADICIONALES #######################
    
    def __add__(self, other):
        self.a=MyFloat.safe(self.sa)
        signa=self.a[0][0]
        signb=other.a[0][0]
        if signa==signb: #Si los signos son iguales suma y si no, resta.
            ss=MyFloat.suma1(self,other)
            ss[0][0]=signa 
            return ss
        elif signa!=signb:
            rr,rr[0][0]=MyFloat.resta1(self,other)
            return rr

    def __sub__(self, other):
        self.a=MyFloat.safe(self.sa)
        signa=self.a[0][0]
        signb=other.a[0][0]
        if signa!=signb: #Si los signos son iguales resta y si no, suma.
            ss=MyFloat.suma1(self,other)
            ss[0][0]=signa
            return ss
        elif signa==signb:
            rr,rr[0][0]=MyFloat.resta1(self,other)
            return rr
       
    def __mul__(self, other):
        self.a=MyFloat.safe(self.sa)
        #Defino los tamaños que requiero. Se asume a arriba y b abajo.
        all0=len(self.a[0])
        all1=len(self.a[1])
        bll0=len(other.a[0])
        bll1=len(other.a[1])
        allt=all0+all1-1
        bllt=bll0+bll1-1
        
        #Crea una lista que va a albergar las listas de mult.parcial.
        c=list(range(bllt))
        
        #Crear un vector resultado con la longitud total, tal que
        #es una lista decimal con las posiciones ya definidas.
        resmulti=list(range(1))
        resmulti=[list(range(allt+bllt))]
        for p in range(allt+bllt):
            resmulti[0][p]=resmulti[0][p]*0
        
        #"Translada los números decimales a la parte entera de las listas
        for i in range(all1):
            self.a[0].insert(all0+i,self.a[1].pop(0))
        for j in range(bll1):
            other.a[0].insert(bll0+j,other.a[1].pop(0))
        
        #Crea los espacios completos
        for k in range(bllt): #Para cada lista creada
            c[k]=[] #Hace una con la cantidad de elementos de a
            for q in range(allt):
                c[k].insert(0,0)
            
        #Multiplica
        for l in range(bllt):#Toma los valores de b
            for m in range(allt):#Toma los valores de a
                #c se toma desde la izquierda. b crece lento con l y a rápido con m.
                c[l][allt-m-1]=self.a[0][allt-m]*other.a[0][bllt-l]+c[l][allt-m-1]
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
            resmulti[0][0]=""
        
        #Vuelve la lista decimal.
        resmulti.insert(1,list()) #Crea la parte decimal
        for i in range(all1+bll1):
            resmulti[1].insert(0,resmulti[0].pop(clli-i-1))
        
        #Incluye el signo.
        if self.a[0][0]==other.a[0][0]:
            resmulti[0].insert(0,"+")
        elif self.a[0][0]!=other.a[0][0]:
            resmulti[0].insert(0,"-")
    
        #Convierte la lista en tupla para que la lea imprimir.
        mm=(resmulti[0],resmulti[1])
    
        return mm    

    def __div__(self):
        pass

    def __radd__(self):
        pass

    def __rsub__(self):
        pass

    def __rmul__(self):
        pass

    def __rdiv__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        self.a=MyFloat.safe(self.sa)
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

    def __eq__(self):
        pass

    def __ne__(self):
        pass

if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    pass
