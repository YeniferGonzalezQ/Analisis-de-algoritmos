class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Verifica si una lista contiene duplicados usando un diccionario.

        Recorre cada número en la lista y lo agrega a un diccionario.
        Si un número ya está en el diccionario, retorna True inmediatamente.
        Si termina de recorrer la lista sin encontrar duplicados, retorna False.

        Retorna:
        bool: True si hay duplicados, False si todos los elementos son únicos.
        """
        conteo = {}

        for num in nums:
            if num in conteo:
                return True
            conteo[num] = 1

        return False