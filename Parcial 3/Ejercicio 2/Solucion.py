class Solution:
    def wordBreak(self, s, wordDict):
        """
        Determina si la cadena s puede segmentarse en palabras del diccionario.

        Usa programación dinámica donde dp[i] indica si el prefijo s[0:i]
        puede formarse usando palabras de wordDict.

        Complejidad:
        - Tiempo: O(n^2)
        - Espacio: O(n)
        """
        word_set = set(wordDict)  # búsqueda O(1)
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # optimización importante

        return dp[n]