from Comision import Comisiones
from Igss import Igss
from Ahorro import Ahorros
from Ganado import Ganado
from Descuento import Descuentos
from Liquido import liquido

base=0
ventas=0

base=int(input("Ingrese el sueldo base: "))
ventas=int(input("Ingrese el monto de las ventas realizadas: "))

#Instanciamos la clase Comisiones
ejercicio2Objeto = Comisiones()

ejercicio2Objeto.asignarVal2(ventas)
ejercicio2Objeto.comisionVentas()

#Instanciamos la clase IGSS
ejercicio2Objeto = Igss()

ejercicio2Objeto.asignarVal1(base)
ejercicio2Objeto.descuentoSeguro()

#Instanciamos la clase Ahorro
ejercicio2Objeto = Ahorros()

ejercicio2Objeto.asignarVal1(base)
ejercicio2Objeto.asignarVal2(ventas)
ejercicio2Objeto.ahorroAhorro()

#Instanciamos la clase Ganado
ejercicio2Objeto = Ganado()

ejercicio2Objeto.asignarVal1(base)
ejercicio2Objeto.asignarVal2(ventas)
ejercicio2Objeto.totalGanado()

#Instanciamos la clase Descuentos
ejercicio2Objeto = Descuentos()

ejercicio2Objeto.asignarVal1(base)
ejercicio2Objeto.asignarVal2(ventas)
ejercicio2Objeto.totalDescuento()

#Instanciamos la clase Líquido
ejercicio2Objeto = liquido()

ejercicio2Objeto.asignarVal1(base)
ejercicio2Objeto.asignarVal2(ventas)
ejercicio2Objeto.totalLiquido()