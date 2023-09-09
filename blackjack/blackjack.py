from random import shuffle
class Carta:

    def __init__(self):
        self.valores: dict[str, int] = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 10,
                                        "10": 10, "J": 10, "Q": 10, "K": 10}
        self.pinta: list[str] = ["Corazon", "Trebol", "Diamante", "Espada"]
        self.tapada: bool = False
        self.valor: str = ''
        self.valor_num : int = 0

    def valor_as(self, as_igual_11: bool = True):
        if as_igual_11:
            self.valores["A"] = 11
        else:
            self.valores["A"] = 1

    def definir_valor(self):
        if self.valor == "A":
            self.valor_num = self.valores["A"]
        elif self.valor in ['J','Q','K']:
            self.valor_num = 10
        else:
            self.valor_num = int(self.valor)

class Mano:

    def __int__(self, cartas: tuple[Carta, Carta]):
        self.mano: list[Carta] = []
        self.mano.extend(cartas)

    def blackjack(self) -> bool:
        if self.mano[0].valor_num + self.mano[1].valor_num == 21:
            return True
        else:
            return False

    def añadir_carta(self, carta: Carta):
        self.mano.append(carta)

    def valor_mano(self) -> int:
        valor_mano = 0
        for carta in self.mano:
            valor_mano += carta.valor_num
        return valor_mano

    def destapar(self):
        for carta in self.mano:
            carta.tapada = False



class Baraja:

    def __init__(self):
        self.baraja: list[Carta] = [Carta(valor,pinta) for valor in Carta.valores.keys() for pinta in Carta.pinta]

    def revolver_cartas(self):
        shuffle(self.baraja)


    def repartir_cartas(self, tapada = False):
        if len(self.baraja) > 0:
            carta = self.baraja.pop()
            carta.tapada = tapada
            return carta
        else:
            return None


class Jugador:

    def __init__(self, fichas: int, nombre: str):
        self.fichas = fichas
        self.nombre = nombre
        self.mano: Mano

    def mano_inicial(self, cartas: tuple[Carta, Carta]):
        self.mano = Mano(cartas)

    def recibir_carta(self, carta : Carta ):
        self.mano.añadir_carta(carta)
    def añadir_fichas(self, fichas : int):
        self.fichas += fichas
    def hay_fichas(self) -> bool:
        return self.fichas > 0

class Casa:


    def __init__(self):
        self.mano : Mano

    def  mano_inicial(self, cartas: tuple[Carta, Carta]):
        self.mano = Mano(cartas)
    def destapa_carta(self):
        if  self.mano[0].tapada == True or self.mano[1].tapada == True:
            self.mano[0].destapar()
            self.mano[1].destapar()


    def recibir_carta(self, carta : Carta):
        self.mano.añadir_carta(carta)



class Blackjack:

    def __init__(self):
        self.apuesta : int = 0
        self.jugador: Jugador = None
        self.cupier: Casa = Casa()
        self.baraja: Baraja = Baraja()

    def registrar_jugador(self,nombre:str):
        self.jugador = Jugador(100,nombre)
    def iniciar_juego(self, apuesta : int):
        self.apuesta = apuesta
        self.baraja.revolver_cartas()

        carta_1_jugador = self.baraja.repartir_cartas()
        carta_2_jugador = self.baraja.repartir_cartas()
        self.jugador.mano_inicial((carta_1_jugador,carta_2_jugador))

        carta_1_casa = self.baraja.repartir_cartas()
        carta_2_casa = self.baraja.repartir_cartas(tapada=True)
        self.cupier.mano_inicial((carta_1_casa, carta_2_casa))

    def repartir_carta_jugador(self):
        self.jugador.recibir_carta(self.baraja.repartir_cartas())

    def destapar_mano_casa(self):
        self.cupier.mano.destapar()

    def pedir_carta_casa(self):
        valor_mano_casa = self.cupier.mano.valor_mano()
        return valor_mano_casa <= self.jugador.mano.valor_mano() and valor_mano_casa <= 16

    def repartir_carta_casa(self):
        self.cupier.recibir_carta(self.baraja.repartir_cartas())

    def jugador_gano(self) -> bool:
        valor_mano_jugador = self.jugador.mano.valor_mano()
        valor_mano_casa = self.cupier.mano.valor_mano()
        return self.jugador.mano.blackjack() or valor_mano_jugador > valor_mano_casa or valor_mano_casa > 21

    def casa_gano(self) -> bool:
        valor_mano_jugador = self.jugador.mano.valor_mano()
        valor_mano_casa = self.cupier.mano.valor_mano()
        return self.cupier.mano.blackjack() or valor_mano_jugador < valor_mano_casa or valor_mano_jugador > 21

    def empate(self) -> bool:
        valor_mano_jugador = self.jugador.mano.valor_mano()
        valor_mano_casa = self.cupier.mano.valor_mano()
        return valor_mano_casa == valor_mano_jugador
