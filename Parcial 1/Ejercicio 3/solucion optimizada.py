class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #si no hay precios o solo hay uno, no hay ganancia posible
        if not prices or len(prices) < 2:
            return 0


        #se inicializa el precio minimo con el primer elemento
        #y la ganancia maxima es 0
        min_price = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
           
            if prices[i] < min_price:
                min_price = prices[i]
            
            
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
