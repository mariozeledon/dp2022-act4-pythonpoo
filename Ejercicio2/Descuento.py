class Descuentos:
    #atributos
    val1=0
    val2=0
    ahorro=0
    igss=0

    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def totalDescuento(self):
        self.ahorro= (self.val1+self.val2)*0.07
        self.igss= (self.val1*0.0483)
        self.total=(self.ahorro+self.igss)
        print("El total de descuentos es de: ",self.total)