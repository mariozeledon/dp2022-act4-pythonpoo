class Mayor:
     #atributos
    val1=0
    val2=0
    val3=0
    

    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def asignarVal3(self,v3):
        self.val3=v3

    def textoMayor(self):
        if self.val1 > self.val2 & self.val1 > self.val3:
            print("El texto con más caracteres es 1")
        if self.val2 > self.val1 & self.val2 > self.val3:
            print("El texto con más caracteres es 2")
        if self.val3 > self.val2 & self.val3 > self.val1:
            print("El texto con más caracteres es 3")
        
        

   