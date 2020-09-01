# This func generates the kth power of complex number a + bi modulo m

import math

def solve(a, b, k, m):

    upper = math.ceil(math.log(k,2))
    zeros = [0]*(upper+1)
    zeros[1] = [a%m, b%m]

    for i in range(2, upper +1):
        last = zeros[i-1]
        x = last[0]
        y = last[1]

        a = x**2 - y**2
        b = 2*x*y

        zeros[i] = [a%m, b%m]
    
    
    binary = bin(k)[2:]
    length = len(binary)

    working = [0,0]
    first1 = str(binary).find('1')

    working = zeros[length-first1]

    for j in range(first1+2, length+1):

        if str(binary)[j-1] == '1':
            index = length-j+1

            pick = zeros[index]

            a = (working[0]*pick[0])-(working[1]*pick[1])
            b = working[0]*pick[1] + working[1]*pick[0]
            
            working = [a%m,b%m]

    return working
