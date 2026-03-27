class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        #dp[i] almacena el numero de formas de decodificar s[:i]
        dp = [0] * (n + 1)

        #caso base: una cadena vacia tiene 1 forma de decodificacion
        dp[0] = 1
        #el primer caracter no es '0' por el check inicial
        dp[1] = 1

        for i in range(2, n +1):
            #opcion 1: decodificar el digito actual por separado(1-9)
            one_digit = int(s[i-1:i])
            if one_digit >= 1:
                dp[i] += dp[i-1]

            #opcion 2: decodificar los dos ultimos digitos juntos (18-26)
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n]
