class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # si la suma es igual no se puede dividir en dos partes iguales
        if sum(nums) % 2:
            return False
        
        #se guardan las sumas posibles siendo target la suma a alcanzar
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        #Se recorre el array al reves
        for i in range(len(nums) - 1, -1, -1):

            # Por cada suma que ya se tenga agregamos el numero actual o no lo agregamos
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP #actualziamos estado

        #retornamos el resultado    
        return True if target in dp else False
