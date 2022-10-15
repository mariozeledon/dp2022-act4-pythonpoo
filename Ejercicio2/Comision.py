class Comisiones:
     #atributos
    val2=0
    comision=0
   
    #métodos
    def asignarVal2(self,v2):
        self.val2=v2
    
    def comisionVentas(self):
        self.comision= (self.val2*0.10)
        print("La comisión de ventas es de: ",self.comision)
        