#ejercicio1Objeto.asignarVal3(int(len(str(input("Ingrese el 3er. texto: ")))))

#LLamar al archivo y luego a la clase
from Concatenar import Concatenar
from Promedio import Promedios
from Mayor import Mayor
from Caracter import Caracteres

texto1=str
texto2=str
texto3=str

texto1=str(input("Ingrese el 1er. texto: "))
texto2=str(input("Ingrese el 2do. texto: "))
texto3=str(input("Ingrese el 3er. texto: "))


#Instanciamos la clase Promedio
ejercicio1Objeto = Promedios()

ejercicio1Objeto.asignarVal1(len(texto1))
ejercicio1Objeto.asignarVal2(len(texto2))
ejercicio1Objeto.asignarVal3(len(texto3))
ejercicio1Objeto.calcularPromedio()

#Instanciamos la clase Concatenar
ejercicio1Objeto = Concatenar()

ejercicio1Objeto.asignarVal1(texto1)
ejercicio1Objeto.asignarVal2(texto2)
ejercicio1Objeto.asignarVal3(texto3)
ejercicio1Objeto.concatenarTexto()
ejercicio1Objeto.longitudTexto()

#Instanciamos la clase Mayor
ejercicio1Objeto = Mayor()

ejercicio1Objeto.asignarVal1(len(texto1))
ejercicio1Objeto.asignarVal2(len(texto2))
ejercicio1Objeto.asignarVal3(len(texto3))
ejercicio1Objeto.textoMayor()

#Instanciamos la clase Caracter
ejercicio1Objeto = Caracteres()

ejercicio1Objeto.asignarVal1(texto1)
ejercicio1Objeto.asignarVal2(texto2)
ejercicio1Objeto.asignarVal3(texto3)
ejercicio1Objeto.concatenarTexto2()
