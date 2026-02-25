class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Verifica si dos cadenas son anagramas usando conteo de caracteres.

        Cuenta las letras de la primera cadena y las resta con la segunda.
        Si falta una letra o el conteo es negativo, no son anagramas.

        Retorna:
            bool: True si son anagramas, False en caso contrario.
        """
        if len(s) != len(t):
            return False

        cuenta = {}

        for c in s:
            cuenta[c] = cuenta.get(c, 0) + 1

        for c in t:
            if c not in cuenta:
                return False
            cuenta[c] -= 1
            if cuenta[c] < 0:
                return False

        return True