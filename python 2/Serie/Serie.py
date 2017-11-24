class Serie:

    def __init__(self,titulo,creador,numTemp,genero):
        self.titulo = titulo
        self.numTemp = numTemp
        self.entregado = False
        self.genero = genero
        self.creador = creador

    def entregar(self):
        self.entregado = True

class Videojuego:

    def __init__(self,titulo,horas,genero,comp):
        self.titulo = titulo
        self.horas = horas
        self.entregado = False
        self.genero = genero
        self.compania = comp

    def entregar(self):
        self.entregado = True

series = []
serie1 = Serie("Lo que el viento se llevo","Yo",12,"Accion")
serie1.entregar()

serie2 = Serie("GOT","Timburto",3,"No se")
serie2.entregar()

serie3 = Serie("Pepito el travieso","Pepito",1,"Aventura")
serie4 = Serie("Nosferatu","Yo",9,"Terror")

serie5 = Serie("Los simpsons","Boleo",70,"Comedia")
serie5.entregar()

series.append(serie1)
series.append(serie2)
series.append(serie3)
series.append(serie4)
series.append(serie5)

videojuegos = []
videojuego1 = Videojuego("TWBH",400,"Accion/Estrategia","Jeje")
videojuego1.entregar()

videojuego2 = Videojuego("WoW",150,"Accion","Blizzard")
videojuego2.entregar()

videojuego3 = Videojuego("GTA",200,"Accion","2k")

videojuego4 = Videojuego("CR",900,"Estrategia","Supercell")
videojuego4.entregar()

videojuego5 = Videojuego("Crash bandicoot",20,"Accion/Estrategia","Naughty Dog")


videojuegos.append(videojuego1)
videojuegos.append(videojuego2)
videojuegos.append(videojuego3)
videojuegos.append(videojuego4)
videojuegos.append(videojuego5)

contSeries = 0
for i in range(0,5):
    if(series[i].entregado == True):
        contSeries += 1

print("Hay " + str(contSeries) + " series entregadas")

contVideojuego = 0
for i in range(0,5):
    if(videojuegos[i].entregado == True):
        contVideojuego += 1


print("Hay " + str(contVideojuego) + " juegos entregados")

conMasTemp = 0
serie = ""
for i in range(0,5):
    if(series[i].numTemp >= conMasTemp):
        conMasTemp = series[i].numTemp
        serie = series[i].titulo

print("La serie ganadora es \"" + serie + "\" con " + str(conMasTemp) + " temporadas")

conMasHoras = 0
videojuego = ""
for i in range(0,5):
    if(videojuegos[i].horas >= conMasHoras):
        conMasHoras = videojuegos[i].horas
        videojuego = videojuegos[i].titulo

print("El juego ganador es \"" + videojuego + "\" con " + str(conMasHoras) + " horas")
