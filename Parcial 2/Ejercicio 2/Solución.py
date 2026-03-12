from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Devuelve el mínimo número de intervalos a eliminar para que
        los intervalos restantes no se solapen.
        Estrategia voraz: mantener siempre el intervalo con el fin más temprano.
        """
        intervals.sort(key=lambda x: x[1])
        count = 0
        pre = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < pre:
                count += 1
            else:
                pre = intervals[i][1]

        return count