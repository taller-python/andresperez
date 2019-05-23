"""Ejercicio 3 Clases y Herencia"""
class Compuerta:
    """Clase Compueta"""
    def __init__(self, valor_a, valor_b):
        """Metodo de la clase Compuerta"""
        self.valor_a = valor_a
        self.valor_b = valor_b

class CompuertaOR(Compuerta):
    """Clase Compuerta OR"""
    def orr(self, valor_a, valor_b):
        """Metodo de la clase CompuertaOR"""
        return "Resultado Compuerta OR: " + str(bool(valor_a or valor_b))

class CompuertaAND(Compuerta):
    """Clase Compuerta AND"""
    def andd(self, valor_a, valor_b):
        """Metodo de la clase CompuertaAND"""
        return "Resultado Compuerta AND: " + str(bool(valor_a and valor_b))

print("Taller 3: Tener en cuenta que:\
    0 = False\
        1 = True")

VALOR_A = input("Ingrese el valor de a:")
VALOR_B = input("Ingrese el valor de b:")

if (VALOR_A in ('0', '1')) and (VALOR_B in ('0', '1')):
    COMPUERTA_OR = CompuertaOR(int(VALOR_A), int(VALOR_B))
    print(COMPUERTA_OR.orr(int(VALOR_A), int(VALOR_B)))
    COMPUERTA_AND = CompuertaAND(int(VALOR_A), int(VALOR_B))
    print(COMPUERTA_AND.andd(int(VALOR_A), int(VALOR_B)))
else:
    print("Valor ingreso no valido 0: False, 1: True")
