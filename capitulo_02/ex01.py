#operador unário
# +, -

#operador ternário, avalia true ou false em uma linha
a, b = 10, 20
print( a if a > b else b)

#------------------------ operador binário
#........aritmético
a, b = 1, 4
print(a + b)    #addition

a, b = 10, 5
print(a - b)    #subtraction

print(a * b)    #multiplication

a, b = 10, 3
print(a / b)    #division

print(a % b)    #modulus

a, b = 10, 5
print(a**b)     #exponentiation

a, b = 10, 3
print(a // b)   #floor division
print(a / b)

a, b = 10, 3.0
print(a // b)

#........abreviados
a, b = 10, 5    # = assignment
a += b          # += add and
print(a)
a -= b          # -= subtract and
print(a)
a *= b          # *= multiply and
print(a)
a /= b          # divide and
print(a)
a %= b          # modulus and
print(a)
a //= b         # floor division and
print(a)
a **=b          # exponent and
print(a)
print(type(a), type(b))
a = int(a)
a &= b          # bitwise and
print(a)
a |= b          # bitwise or and
print(a)
a ^= b          # bitwise xor and
print(a)
a >>= b         # binary right sihift and
print(a)
a <<= b         # binary left shift and
print(a)

#........comparison
a, b = 10, 5
print(a == b)   #equal to
print(a != b)   #not equal to
print(a < b)    #less than
print(a <= b)   #less than equal to
print(a > b)    #greater than
print(a >= b)   #greater than equal to

#........lógicos
a, b = 10, 5
print(a and b)  #logical and -> result: 5
print(a or b)   #logical or -> result: 10
print(not a)    #logical not -> result: False
print(not b)    #result: False

#........identity
print(a is b)       #False
print(a is not b)   #True

#........Membership (filiação)
l = [10, 20]
print(10 in l)      #True
print(10 not in l)  #False

#........bitwise
a, b = 10, 5
print(a & b)    #0
print(a | b)    #15
print(~b)       #-6
print(a^b)      #15
print(a>>b)     #0
print(a<<b)     #320

#--------- String operators
# + concatenação
s = "test"
s1 ="ing"
print(s + s1)

# * replicação
print("test " * 3)
print(3 * "sample ")
print(3 *"1")

#--------- operator precedence
"""
()  (primeiro a ser avaliado)
**
+, -, ~ (unário, o que aparercer primeiro)
*, /, //, %
+, -    (addition, subtraction)
<<, >>, ?
&
^
|
==, !=, >, >=, <, <=, is, is not, in, not in
and, or
not
=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=
"""

#--------- expression evaluation
x = eval("123 + 123")
print(x)

x = eval("sum([10,10,10])",{})
print(x)

x=y=100
z = eval("x + y")
print(z)
#exemplos anteriores, x, y e z são variáveis globais
#exemplo com variável local
w = eval("x+50",{},{"x":51})
#x é  variável local por estar dentro do eval
print(w)

#--------- input
print("digite 2 números inteiros")
a = int(input())
b = int(input())
print("a =",a,", b =",b,", a + b =",a + b)

a = int(input("digite um número inteiro: "))
b = int(input("digite um número inteiro: "))
c = a + b
print("sum =", c)

a=input()
print(type(a))
#print(a+3) typeError
print(int(a) + 3)

a = float(input("Enter a float value: "))
b = float(input("Enter a float value: "))
c = a + b
print("sum of floats =", c)

n = int(input("Digite um número: "))
print(n * "1")

x = input("Enter character: ")
print("Ascii of", x, "is", ord(x))