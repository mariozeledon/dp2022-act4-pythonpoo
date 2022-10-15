class Ganado:
    #atributos
    val1=0
    val2=0
    comision=0
    total=0

    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def totalGanado(self):
        self.comision= (self.val2*1.10)
        self.total=(self.val1+self.comision)
        print("El total ganado es de: ",self.total)