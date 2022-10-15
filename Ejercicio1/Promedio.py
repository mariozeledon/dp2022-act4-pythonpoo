class Promedios:
    #atributos
    val1=0
    val2=0
    val3=0
    promedio=0

    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def asignarVal3(self,v3):
        self.val3=v3

    def calcularPromedio(self):
        self.promedio= (self.val1+self.val2+self.val3)/3
        print("El promedio es ",self.promedio)