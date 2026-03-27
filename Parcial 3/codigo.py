class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        #creacion de una matriz de (m+1) x (n+1) llena de ceros
        # dp[i][j] sera la LCS de text1[:i] y text2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m +1):
            for j in range(1, n + 1):
                #si los caracteres actuales son iguales
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        #resultado final esta en la ultima celda de la matriz
        return dp[m][n]
