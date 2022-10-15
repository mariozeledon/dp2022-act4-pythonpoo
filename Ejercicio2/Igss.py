class Igss:
    #atributos
    val1=0
    seguro=0
   
    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def descuentoSeguro(self):
        self.seguro= (self.val1*0.0483)
        print("El monto del IGSS es de: ",self.seguro)
        