
class Electrodomesticos:
    def __init__(self,precio,color,consumo,peso):
        self.precio = precio
        self.color = color
        self.consumo = consumo
        self.peso = peso
        self.comprobarConsumo()
        self.comprobarColor()

    def comprobarConsumo(self):
        if self.consumo.upper() == "A":
            self.consumo = "A"
        elif self.consumo.upper() == "B":
            self.consumo = "B"
        elif self.consumo.upper() == "C":
            self.consumo = "C"
        elif self.consumo.upper() == "D":
            self.consumo = "D"
        elif self.consumo.upper() == "E":
            self.consumo = "E"
        else:
            self.consumo = "F"
        return self.consumo

    def comprobarColor(self):
        if self.color.upper() == "NEGRO":
            self.color="NEGRO"
        elif self.color.upper() == "ROJO":
            self.color = "ROJO"
        elif self.color.upper() == "AZUL":
            self.color="AZUL"
        elif self.color.upper()== "GRIS":
            self.color="GRIS"
        else:
            self.color="BLANCO"
        return  self.color

    def precioFinal(self):
        if self.consumo.upper() == "A":
            self.precio=self.precio + 100
        elif self.consumo.upper() == "B":
            self.precio=self.precio + 80
        elif self.consumo.upper() == "C":
            self.precio=self.precio + 60
        elif self.consumo.upper() == "D":
            self.precio=self.precio + 50
        elif self.consumo.upper() == "E":
            self.precio=self.precio + 30
        else:
            self.precio=self.precio + 10
        if self.peso >= 0 | self.peso <=19:
            self.precio = self.precio + 10
        elif self.peso >= 20 | self.peso <= 49:
            self.precio = self.precio + 50
        elif self.peso >= 50 | self.peso <= 79:
            self.precio = self.precio + 80
        else:
            self.precio = self.precio + 100
        return self.precio

class Lavadora(Electrodomesticos):

    def __init__(self,carga,precio,color,consumo,peso):
        super().__init__(precio,color,consumo,peso)
        self.carga=carga

    def precioFinal(self):
        super().precioFinal()
        if self.carga > 30:
            self.precio=self.precio + 50
        return self.precio

class television(Electrodomesticos):

    def __init__(self,resolucion,fourk,precio,color,consumo,peso):
        super().__init__(precio,color,consumo,peso)
        self.resolucion=resolucion
        self.fourk=fourk

    def precioFinal(self):
        super().precioFinal()
        if self.resolucion > 40:
            self.precio = self.precio * 1.30
        if self.fourk == True:
            self.precio = self.precio + 50
        return  self.precio



electro1 = Electrodomesticos(1000,"Verde","C",150)
print("Electrodomestico 1 -->")
print("Precio : " + str(electro1.precio))
print("Peso : " + str(electro1.peso))
print("Color : " + electro1.color)
print("Consumo de : " + electro1.consumo)
print("Total : " + str(electro1.precioFinal()))
print("")



lavadora2=Lavadora(20,1000,"azul","D",200)
print("Lavadora 2 -->")
print("Precio : " + str(lavadora2.precio))
print("Peso : " + str(lavadora2.peso))
print("Color : " + lavadora2.color)
print("Consumo de : " + lavadora2.consumo)
print("Total : " + str(lavadora2.precioFinal()))
print("")


televison3=television(4000,False,1500,"Negra","F",350)
print("Television 3 -->")
print("Precio : " + str(televison3.precio))
print("Peso : " + str(televison3.peso))
print("Color : " + televison3.color)
print("Consumo de : " + televison3.consumo)
print("Total : " + str(televison3.precioFinal()))
print("")