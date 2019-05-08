"""Crear un modulo con una función que permita saber si una palabra es palindroma. Ejemplo:
Input: 'reconocer'
Output: TRUE 'reconocer'"""

def validar_palindroma(text):
    """Funcion que retorna si una palara es palindroma"""
    igual, aux = 0, 0
    for i in reversed(range(0, len(text))):
        if text[i].lower() == text[aux].lower():
            igual += 1
            aux += 1

    if len(text) == igual:
        return "TRUE " + text
    return "FALSE " + text

TEXTO = input("Input: ")
print(validar_palindroma(TEXTO))
