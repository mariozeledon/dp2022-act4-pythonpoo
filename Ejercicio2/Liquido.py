class liquido:
     #atributos
    val1=0
    val2=0
    comision=0
    totalGanado=0
    ahorro=0
    igss=0
    totalDescuentos=0
    total=0

    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def totalLiquido(self):
        self.comision= (self.val2*1.10)
        self.totalGanado=(self.val1+self.comision)
        
        self.ahorro= (self.val1+self.val2)*0.07
        self.igss= (self.val1*0.0483)
        self.totalDescuentos=(self.ahorro+self.igss)

        self.total=(self.totalGanado-self.totalDescuentos)
        print("El total Líquido es de: ",self.total)