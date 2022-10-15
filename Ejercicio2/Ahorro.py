class Ahorros:
    #atributos
    val1=0
    val2=0
    ahorro=0
   
    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def ahorroAhorro(self):
        self.ahorro= (self.val1+self.val2)*0.07
        print("El ahorro es de: ",self.ahorro)