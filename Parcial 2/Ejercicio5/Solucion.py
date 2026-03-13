#El algoritmo primero ordena los intervalos por su punto de inicio. Luego recorre la lista una sola vez y 
#fusiona inmediatamente los intervalos que se solapan extendiendo el final al valor máximo. 
#Esta decisión voraz es correcta porque, después de ordenar, un intervalo solo puede solaparse con el último intervalo procesado,
#por lo que fusionarlo en ese momento no afecta decisiones futuras
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #orden de los intervalo por el inicio
        intervals.sort(key=lambda x: x[0])

        merged = []
        #recorrerlos una sola vez   
        for interval in intervals:

            #si no hay solapamiento
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                #fusionar intervalos
                merged[-1][1] = max(merged[-1][1], interval [1])
        
         #si el intervalo actual se solapa con el ultimo intervalo agregado,
         #se fusionan extendiendo su final al maximo
        return merged

# Complejidad:
# Tiempo: O(n log n) debido al ordenamiento de los intervalos.
# Espacio: O(n) para almacenar los intervalos fusionados.
