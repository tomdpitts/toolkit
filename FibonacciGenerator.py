# Generates nth Fibonacci number (up to 10e9) given any f0 and f1, modulo (1e9 +7)

# firstly, initialise the 1,1,1,0 matrix to the power of 2^n for n up to 30, outside of the solve function

# this means we have the components needed to quickly (O(logn)) generate powers of the 1,1,1,0 matrix on the fly and don't have to repeat any unnecessary calculations

matrix = [[1,1],[1,0]]
zeros = [0]*(31)
zeros[1] = matrix

# adjust modulo here
m = int(1e9 + 7)

a1 = matrix[0][0]
a2 = matrix[0][1]
b1 = matrix[1][0]
b2 = matrix[1][1]

for i in range(2, 31):

    matrix = [[(a1*a1%m + a2*b1%m)%m,(a1*a2%m + a2*b2%m)%m], [(b1*a1%m + b2*b1%m)%m, (b1*a2%m + b2*b2%m)%m]]

    a1 = matrix[0][0]
    a2 = matrix[0][1]
    b1 = matrix[1][0]
    b2 = matrix[1][1]

    zeros[i] = matrix

    print(matrix)


# here's the top-level solve func, which generates the canonical matrix exponentiation form of fibonacci for any given f(0) and f(1)

def solve(a, b, n):

    matrix = [[1,1],[1,0]]
    initial = [b, a]

    target = matmult(leftHandPower(n),initial)%m

    return int(target)

# this func is needed to take the 1,1,1,0 matrix to the power of n-1
# it's fast, because it only multiplies combinations of matrices already calulated in step 1 e.g. 53 = 32 + 16 + 4 + 1, so M^53 = M^32 * M^16 * M^4 * M^1

# a trick to neatly break down n-1 into these components is to convert n-1 to binary and then use which ever matrices correspond to a '1' in the number e.g. binary(53) = 110101

def leftHandPower(n):

    binary = bin(n-1)[2:]
    
    length = len(binary)

    # just the Identity matrix, as a starting point for the for loop
    I = [[1,0], [0,1]]
    working = I

    for j in range(1, length+1):

        if str(binary)[j-1] == '1':

            index = length-j+1

            a1 = zeros[index][0][0]
            a2 = zeros[index][0][1]
            b1 = zeros[index][1][0]
            b2 = zeros[index][1][1]

            x1 = working[0][0]%m
            x2 = working[0][1]%m
            y1 = working[1][0]%m
            y2 = working[1][1]%m

            working = [[(x1*a1%m + x2*b1%m)%m, (x1*a2%m + x2*b2%m)%m], [(y1*a1%m + y2*b1%m)%m, (y1*a2%m + y2*b2%m)%m]]

    return working

# this function is tailored to only return the 'top' value of a 2x2 matrix multiplied by a 1x2 vector, which is all that's needed in solve() to get f(n). Doing proper multiplication would give us f(n-1) as well but we're not interested in that here.

def matmult(m, v):

    a1 = int(m[0][0])
    a2 = int(m[0][1])

    x = v[0]
    y = v[1]

    answer = (a1*x + a2*y)
 
    return answer
