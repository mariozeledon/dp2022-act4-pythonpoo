class Caracteres:
     #atributos
    val1=0
    val2=0
    val3=0
    concatenar=0
    longitud=0

    #métodos
    def asignarVal1(self,v1):
        self.val1=v1

    def asignarVal2(self,v2):
        self.val2=v2

    def asignarVal3(self,v3):
        self.val3=v3

    def concatenarTexto2(self):
        self.concatenar= (self.val1+self.val2+self.val3)
        print("El texto concatenado es: ",self.concatenar)
        print("La cantidad de caracteres es: ",len(self.concatenar))

    

 