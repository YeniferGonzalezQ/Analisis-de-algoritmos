class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Devuelve el número máximo de niños que pueden ser satisfechos con las galletas disponibles.

        Cada niño i requiere una galleta de tamaño al menos g[i], y cada galleta j tiene tamaño s[j].
        Se asigna la galleta más pequeña que pueda satisfacer al niño. 

        Retorna:
        int: Número máximo de niños contentos.
        """
        g.sort()
        s.sort()
        i = j = count = 0
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1  
        return count