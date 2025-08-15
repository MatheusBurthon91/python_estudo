import random
from collections import Counter

random_list = random.sample(range(0, 100000), 1000)

# listas, dicionarios e conjuntos

pessoas = [
    "Lucas", "Mariana", "Thiago", "Fernanda", "Bruno",
    "Camila", "Rafael", "Patrícia", "Gustavo", "Juliana",
    "André", "Larissa", "Felipe", "Natália", "Diego"
]

frase = "CS é bom demais, as dicas pythonicas fazem ficar melhor ainda"

vogais = "aeiou"
consoante = "bcdfghjklmnpqrstvwxyz"

# colocar em uma lista quantas vogais, consoantes o outros caracteres tem na frase

lista_vogais = []
lista_consoantes = []
lista_outras_letras = []
for letra in frase:
    if letra in vogais:
        lista_vogais.append(letra)
    elif letra in consoante:
        lista_consoantes.append(letra)
    else:
        lista_outras_letras.append(letra)

# print(lista_vogais)
# print(lista_consoantes)
# print(lista_outras_letras)

# faça um conjunto de vogais tem na mesma frase acima

conjunto_vogais = set()
conjunto_consoantes = set()
conjunto_outros_caracteres = set()

for letra in frase:
    # quero adicionar as vogais em um conjunto
    if letra in vogais:
        conjunto_vogais.add(letra)
    elif letra in consoante:
        conjunto_consoantes.add(letra)
    else:
        conjunto_outros_caracteres.add(letra)


# print(conjunto_vogais)
# print(conjunto_consoantes)
# print(conjunto_outros_caracteres)

#enumerate, any, all

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [0, 6, 7, 8, 9]

#all serve para identificar se em determinada lista todas as condições são verdadeiras(raciocinio similar ao 'every do javascript')
all1 = all(lista_1)
# print(all1)
all2 = all(lista_2)
# print(all2)

# any serve para identificar se em determinada lista alguma condição é verdadeira(racionio similar ao some do javascript)
any1 = any(lista_1)
# print(any1)
any2 = any(lista_2)
# print(any2)

# enumerate - serve para criar um contador e ainda ser percorrer esse dado
# for index, pessoa in enumerate(pessoas):
#     print(f"id: {index + 1} nome: {pessoa}")
    
#max, min, len

#max - serve para pegar o elemento que aparece mais vezes
num_max = max(random_list)
# print(num_max)
#min - serve para pegar o elemento que aparece menos vezes
num_min = min(random_list)
# print(num_min)
#len - serve para medir o comprimento de uma lista
num_len = len(random_list)
# print(num_len)

# Counter
import random
from collections import Counter

lista_de_numeros = []
for x in range(10000):
    lista_de_numeros.append(random.randint(0, 1000))

# print(lista_de_numeros)
counter = Counter(lista_de_numeros)

# print(counter)
# print(counter[0])

mais_comuns = counter.most_common()
# print(mais_comuns)

numero, vezes_que_repete = mais_comuns[0]
print(
    f"O número mais comum é {numero} e ele se repete {vezes_que_repete} vezes"
)