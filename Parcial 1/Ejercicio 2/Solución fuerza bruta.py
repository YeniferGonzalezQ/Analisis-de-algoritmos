class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        """
        Verifica si una lista contiene elementos duplicados utilizando un conjunto (set).

        Convierte la lista en un set, el cual elimina automáticamente los valores
        repetidos. Si el tamaño del set es menor que el de la lista original,
        significa que existían elementos duplicados.

        Retorna:
            bool: True si hay duplicados, False si todos los elementos son únicos.
        """
        return len({*a}) < len(a))
