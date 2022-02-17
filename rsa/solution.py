
import rsa
import math
import hashlib

n = 988082649547634539735932714787069852964949779
e = 65537
q = 35742549198872617291353508656626642567

#(decimal to ASCII for resulting message)
c = 327097033161733906765917941890866428911800925


p = n//q
phi = ( p-1) * (q - 1)

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

d = getModInverse(e, phi)


m = pow(c,d,n)
##answer shoule be 104971151043239821111219910139, put into decimal to ascii tool
## result says hash 'Royce'
str_to_hash = 'Royce'
result = hashlib.sha256(str_to_hash.encode())


  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())