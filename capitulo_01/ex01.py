print("This is to test") #im
print() #imprime uma linha em branco
print("this is the second line in python program")

print("this","is","to","test",end="@")
print()
print("this is", " to test", sep="---",end="#")
print("this is an experiment")
print()
print("this","is","to","test",sep=";",end="@")
print()
print("this","is","to","test",end="\n\n")
print("this is an experiment")

#bloco de códigos são criados com indentação
#não há {}, deve-se utilizar espaços

def test():
    a = 1   #pertence à função

a = 0   #não pertence à função
print(a)

test_one = 1
test_two = 2
test_three = 3
#quando a linha for muito longa, pode-se utilizar o caracter
#de continuação de linha
a = test_one + \
test_two + \
test_three
print(a)

#declarações com: [], {}, () não precisam de caracter de continuação de linha
a = {1, 2, 3, 4,
     5, 6, 7}

#criar string é possível usar: ' ', " ", """ """
s = "teste"
s = 'teste'
s = """isto é um teste de 
criação de string
com múltiplas
linhas"""
s = '''isto é um teste de 
criação de string
com múltiplas
linhas'''

#triplo ''' ou """, podem ser utilizados para comentar várias linhas de execução

#mais de uma instrução por linha, separar com: ;
x = 'test'; print(x)

#para criar variáveis, basta atribuir um valor
c = 100
#cria automaticamente a variável 'c' que aponta para o valor 100

i = 100
i = 50 + 500
print(i)    #valor que tinha em i (100) foi substituído

a = '5'
b = "5"
print(a + b)    #ocorreu a concatenação

a = 5.0
b = 3.0
c = (a**2 + b**2) ** 0.5
print("c =", c)

#atribuir valores para várias variáveis em uma linha
c=e=f=g=1

#múltipla atribuição
c,e,f,g = 'c1', 'e1', 'f1', 'g1'

print(c, e, f, g)

#None : significa ausência de valor
test = None
if (test == None):
    print("None: ", test)

if test is None:
    print("Nada: ", test)

#conversão de tipo implicita
x = 123
y = 12.34
print(x + y)

x = 10 + 1j
y = 10.0
print(x + y)

x = 'test'
y = 10
# print(x + y) TypeError: não pode concatenar string com inteiro

print(chr(14))

x = "1010"
print("string=", x)
print("conversion to int=", int(x,2))
print("conversion to float=", float(x))
print("conversion to complex=", complex(x))
x = 10
print("conversion to hexadecimal=", hex(x))
print("conversion to octal=", oct(x))
print("conversion to ascii=", chr(x+2))
x = 'test'
print("conversion to tuple=", tuple(x))
print("conversion to set=", set(x))

print(1.0)
print(chr(213), hex(213), oct(213))