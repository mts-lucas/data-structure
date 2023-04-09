# Desenvolva um algoritmo capaz de verificar um dado numero n eh primo.
# Verifique sua complexidade com
# o calculo de T(n).

def isPrime(n):

    if n < 2:

        return False

    # na lang escrita usar n-1
    for i in range(2, n):

        if n % i == 0:
            return False

    return True


print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(10))
