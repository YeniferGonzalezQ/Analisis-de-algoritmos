class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Comprueba si dos palabras son anagramas usando un método de fuerza bruta
        basado en el conteo de letras.

        Recorre la primera palabra letra por letra y compara cuántas veces aparece
        cada carácter en ambas cadenas utilizando count(). Si alguna letra tiene
        una frecuencia diferente, significa que no contienen las mismas letras.

        Retorna:
            bool: True si son anagramas, False si no lo son.
        """
        if len(s) != len(t):
            return False

        for c in s:
            if s.count(c) != t.count(c):
                return False

        return True