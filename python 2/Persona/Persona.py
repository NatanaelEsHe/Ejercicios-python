import random
from tkinter import Pack


class Persona:
    def __init__(self,sexo,nombre,edad,peso,altura):
        self.dni=""
        self.sexo = sexo
        self.introducirSexo()
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.generarDNI()

    def calcularIMC(self):
        imc = "{0:.0f}".format((self.peso/(self.altura*self.altura)))
        if int(imc) < 14:
            print("Tu IMC es de: "+ imc + ", estas por debajo de tu peso ideal")
            self.esMayorEdad()
        elif int(imc) >= 14 & int(imc) <16:
            print("Tu IMC es de: " + imc + ", bastante bien en comparación a tu peso")
            self.esMayorEdad()
        else:
            print("Tu IMC es de: " + imc + ", necesitas adelgazar")
            self.esMayorEdad()

    def esMayorEdad(self):
        if self.edad < 18:
            print("Es menor de edad")
        else:
            print("Es mayor de edad")

    def introducirSexo(self):
        if  self.sexo.upper() == "H":
            self.sexo = "H"
        elif self.sexo.upper() == "M":
            self.sexo = "M"
        else:
            self.sexo = "Sexo no especifico"
        return  self.sexo

    def generarDNI(self):
        letras = ["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        numero = random.randint(10000000,99999999)
        moduloNumero = numero%23
        self.dni = str(numero) + letras[moduloNumero]



    def setSexo(self,sex):
        self.sexo = sex

    def setNombre(self,nom):
        self.nombre = nom

    def setEdad(self,edad):
        self.edad = edad

    def setPeso(self,peso):
        self.peso = peso

    def setAltura(self,altura):
        self.altura = altura

print("Introduzca datos --->")
nombre = input("Nombre: ")
sexo= input("Sexo : ")
edad = int(input("Edad: "))
altura= float(input("Altura: "))
peso = float(input("Peso: "))
print("")


p= Persona(sexo,nombre,edad,peso,altura)
print("Nombre: "+p.nombre)
print("Sexo: "+ p.sexo)
print("Edad: "+ str(p.edad))
print("Peso: "+ str(p.peso))
print("Altura: "+ str(p.altura))
print("Dni: " + p.dni)
p.calcularIMC()
p.esMayorEdad()