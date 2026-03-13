class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                    goal = i

        return True if goal == 0 else 

# Justificación: La solucion es Greedy hacia atras. Si una posición i puede alcanzar el goal, entonces i también puede llegar al final, por lo que se actualiza el goal = i
# Complejidad: Tiempo O(n) porque se recorre el arreglo una vez.Espacio O(1) ya que solo se usa una variable adicional goal
