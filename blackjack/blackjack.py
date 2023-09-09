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

    def mano_inicial(self, cartas: list[Carta, Carta]):
        pass


class Casa:
    pass


class Blackjack:

    def __init__(self):
        self.jugador: Jugador = None
        self.cupier: Casa = None
        self.baraja: Baraja = None
