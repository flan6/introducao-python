# data structures

# pilha, lista, fila
# stack, list, queue

# Python: list, dict, set, tuple

a = ["flander", 1, "domingo"]
b = ["pitagoras", "computer science"]
c = [1, 1.1, 2, 3, 4]


a.append("academia")
#print(a)

a.insert(int(len(a)/2), "eleicao dois")
#print(a)

# a[len(a):] = b
a.extend(b)
a.extend(c)
#print(a)

item = a.pop()
a.remove(1)
#print(a)

# a.sort(reverse=True)
##print(a)

from collections import deque

deque = deque(a)
deque.append("eleicao")
#print(deque)

# for _ in deque:
#     print(deque.popleft())

#print(deque)
lista_nova_2 = []
for x in deque:
    if type(x) == int:
        lista_nova_2.append(x*2)

#print(lista_nova_2)

lista_nova = [x for x in [x*2 for x in deque if type(x) == int]]
#print(lista_nova)

tuple_vazia = ()
a = 1, 2, lista_nova

z, x, y = a
# print(f"valor de z {z},", f"valor de x {x},", "valor de y {0},".format(y))
# print(a)

set_a = {"abelha", "abobora"}
set_b = {"abobora", "batata"}

set_c = {x for x in deque if type(x) == str}

# print(set_c)
# print(set_a - set_b)
# print(set_a | set_b)
# print(set_a & set_b)
# print(set_a | set_c)

dict_a = {"chave": "valor", "chave2": "valor2"}
print(dict_a["chave"])

dict_a["chave"] = "novo_valor"
dict_a["chave2"] = a

print(sorted(set_a))


for chave, valor in dict_a.items():
    if chave == "chave2":
        print(valor)
