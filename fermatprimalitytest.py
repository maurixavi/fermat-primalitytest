from random import randrange
import math
#INPUT: N: value to test for primality
def isPossiblyPrime(N):
    cont=0
    while cont<=10:
        a = randrange(1, N-1)  #Choose a random "a" value in the given range

        g = math.gcd(a, N)
        if g != 1:  
            return False #N is composite

        if pow(a, N-1, N) != 1: #pow(a, N-1) % N != 1:
            print(f'{a:,}', "is a Fermat witness for N =",f'{N:,}')   
            return False #N is composite
        else:
            cont+=1
            #print(cont, ":: a value for the Possibly Prime:", f'{a:,}')
            if cont>=10:
                return True


print("Number of prime numbers you want to find:")
primesToGet = int(input())

print("Let [I1, I2] the range:")
i1 = int(input("Enter a I1 value: "))
i2 = int(input("Enter a I2 value: "))
print("\n")

examinated = 1
primesList = []
primesCount=0

for N in range(i1, i2):
    #Filtering multiples of first prime numbers up to 199:
    if (N % 2 != 0) and (N % 3 != 0) and (N % 5 != 0) and (N % 7 != 0) and (N % 11 != 0) and (N % 13 != 0) and \
        (N % 17 != 0) and (N % 19 != 0) and (N % 23 != 0) and (N % 29 != 0) and (N % 31 != 0) and \
        (N % 37 != 0) and (N % 41 != 0) and (N % 43 != 0) and (N % 53 != 0) and (N % 59 != 0) and \
        (N % 61 != 0) and (N % 67 != 0) and (N % 71 != 0) and (N % 73 != 0) and (N % 83 != 0) and \
        (N % 89 != 0) and (N % 97 != 0) and (N % 101 != 0) and (N % 103 != 0) and (N % 107 != 0) and \
        (N % 113 != 0) and (N % 127 != 0) and (N % 131 != 0) and (N % 137 != 0) and (N % 149 != 0) and \
        (N % 151 != 0) and (N % 157 != 0) and (N % 163 != 0) and (N % 167 != 0) and (N % 173 != 0) and \
        (N % 179 != 0) and (N % 181 != 0) and (N % 191 != 0) and (N % 193 != 0) and (N % 197 != 0) and (N % 199 != 0):
        if  isPossiblyPrime(N):
            print(f'{N:,}', "IS POSSIBLY PRIME")
            print("Number of tests done ", f'{examinated:,}')
            primesList.append(N)
            primesCount+=1
            if (primesCount == primesToGet):
                print("\nFirst", primesCount, "possible prime numbers found in the [", i1, "-", i2,"] interval:")
                for elem in primesList:
                    print(elem)
                #print("i1, i2, "interval")
                break
        examinated+=1