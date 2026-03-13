class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])

        return profit

# Justificación: Solucion tipo Greedy. Se suman todas las subidas consecutivas de precio, porque cada incremento representa una ganancia válida al comprar ayer y vender hoy.
# Complejidad: Tiempo O(n) ya que se recorre el arreglo una sola vez. Espacio O(1) porque solo usamos la variable acumuladora profit.
