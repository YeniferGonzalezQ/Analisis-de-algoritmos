class Solution:
    def lengthOfLIS(self, nums):
        """
        Calcula la longitud de la subsecuencia estrictamente creciente más larga (LIS).

        Se utiliza programación dinámica donde dp[i] representa la longitud de la
        subsecuencia creciente más larga que termina en el índice i. Para cada
        posición i, se revisan todos los índices anteriores j < i, y si nums[i] > nums[j],
        se actualiza dp[i] como dp[j] + 1.

        La respuesta final es el valor máximo en el arreglo dp.

        Complejidad:
        - Tiempo: O(n^2)
        - Espacio: O(n)
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)