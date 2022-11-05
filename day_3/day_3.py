# Fundamentos
# Sintaxe
# Variaveis
# operadores
# loops
# condicionais
# functions

def tri_recursion(*args, **kargs):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
        kargs["argumento"]
        args[1]
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(3, argumento= 1)


def sum(a, b):
    return a + b

print("resultado da soma e: " + str(sum(1, 2)))

a = True #bool
print(type(a))
a = "aa" #str #String #string #Char
print(type(a))
a = 1 #int
print(type(a))
a = 1.1 #float
print(type(a))
a = [] #list
print(type(a))
a = {} #dict
print(type(a))
a = set() #set
print(type(a))

# and or not
# && || !


def test_args(*args, **kargs):
    print(args)
    print("\t a\n")
    print(kargs["argumento"])

test_args(2, k=1, argumento=9)
