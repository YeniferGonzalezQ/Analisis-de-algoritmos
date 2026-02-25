class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #inicializa el precio minimo con el primer valor
        #y la ganancia maxima es 0
        min_price = float('inf')
        max_profit=0

        for price in prices:
            #Si encuentra un precio mas bajo que el actual,
            #lo marcara como un nuevo punto de compra potencial
            if price < min_price:
                min_price = price
            
            #si el precio actual menos el minimo
            #es mayor que la ganancia actual, se actualiza max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
