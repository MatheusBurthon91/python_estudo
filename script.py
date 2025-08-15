# 1. Resumo do python
#declarando variaveis
nome = "Matheus";
idade = 34;
profissao = "Programador";

# Tipos de dados
#int
# print(type((20)));
# #float
# print(type(20.5))
# #string
# print(type("Matheus"))
# #boolean
# print(type(True))
# #list
# print(type([1,2,3]))
# #tuple
# print(type(("Matheus", "Burthon", 34)));
# #dict
# print(type({"nome": "Matheus", "idade": 34}));

# 2. Operadores
a = 2;
b = 3;

# soma
# print(a + b);
# # subtração
# print(a - b);
# # multiplicação
# print(a * b);
# # divisão
# print(a / b);
# # resto da divisão
# print(a % b);
# # potencia
# print(a ** b);
# # divisão inteira
# print(a // b);
# # igualdade
# print(a == b);
# # diferente
# print(a != b);
# # maior
# print(a > b);
# menor

# 3. Estruturas de controle
# if
# if a > b:
#     print("a é maior que b");
# else:
#     print("a é menor que b");
    
# não existe switch case no python

# 4. Estruturas de repetição

# podemos percorrer uma lista, para isso existe o loop for ou while

restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

# pegue os restaurantes que tiveram notas maiores que 4.0 e mostre eles em uma nova lista
topRestaurants = [];

for restaurant in restaurants:
    if restaurant["nota"] > 4.0:
        topRestaurants.append(restaurant);

# print(topRestaurants);

# esse loop pode ser escrito de outra forma
topRestaurants = [restaurant for restaurant in restaurants if restaurant["nota"] > 4.0];
# print(topRestaurants);

# podemos percorrer uma lista e pegar apenas os nomes dos restaurantes
restaurantNames = [restaurant["name"] for restaurant in restaurants];
# print(restaurantNames);

# percorrer uma estrutura númerica e para isso podemos utilizar o range(5)
intervalo = [index for index in range(5)]
# print(intervalo)

phrase = "No meu WSL, o comando code . está abrindo o Cursor AI, mas eu quero que ele abra a IDE oficial do Visual Studio Code."

# na frase acima retorne o numero de vezes que a letra "o" aparece.
times = 0
for letter in phrase:
    if letter == "o" or letter == "O":
        times += 1
        
# print(times);
# outras formas de fazer
vogals = len([letter for letter in phrase if letter == "o" or letter == "O"]);
# print(vogals)


# print(soma(1, 2));

# declarando duas variaveis seguidas
# c, d = 3, 4

# print(c, "variavel c")
# print(d, "variavel d")

# sequencia de fibonnaci no python
n = 10
last, next = 0, 1
while last < n:
    # print(last, "antes do acrescimo")
    last, next = next, last + next
    # print(last, "last", next, "next")

# enumerate
languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
# print(list(enumerate_prime))

# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


for index, language in enumerate(languages):
    print(f'{index} - {language}')
# Saída:
# 0 - Python
# 1 - Java

# O Fatorial de um número inteiro é representado pela multiplicação de todos os 
# números predecessores maiores que 0. Por exemplo, 
# o fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5. 
# Escreva um código que calcule o fatorial de um número inteiro.

factorial = 1
list = [number for number in range(1, 6)]
for number in list:
    factorial *= number

# print(factorial);

# outra forma de escrever
factorial = 1
for number in range(1, 6):
    factorial *= number

# print(factorial)

# spoiler faça uma função com fatorial
def calculate_factorial(n):
    factorial = 1
    for number in range(1, n + 1):
        factorial *= number;
    
    return factorial


# print(calculate_factorial(4))

#Um sistema de avaliações registra valores de 0 a 10 para cada avaliação. 
# Após algumas mudanças estes valores precisam ser ajustados para avaliações de 0 a 100. 
# Dado uma sequência de avaliações ratings = [6, 8, 5, 9, 10]. 
# Escreva um código capaz de gerar as avaliações após a mudança. 
# Neste caso o resultado deveria ser [60, 80, 50, 90, 100].

ratings = [6, 8, 5, 9, 10]

new_ratings = []
for rating in ratings:
    new_ratings.append(rating * 10)

# print(new_ratings)

#  outro jeito
new_ratings = [rating * 10 for rating in ratings]
# print(new_ratings)

#Percorra a lista do exercício 13 e 
#imprima “Múltiplo de 3” se o elemento for divisível por 3.
# for rating in new_ratings:
#     if rating % 3 == 0:
#         print(f"{rating} é múltiplo de 3");
#     else:
#         print(f"{rating} não é múltiplo de 3");


# 5. Funções

def soma(a, b):
    return a + b;


# soma(2, 2)  # os parâmetros aqui são posicionais

# soma(a=2, b=2)  # aqui estamos nomeando os parâmetros

# Os parâmetros também podem ser variádicos, ou seja, variam em sua quantidade.

# Parâmetros posicionais variádicos são acessados como uma tupla no interior de uma função, 
# e parâmetros nomeados variádicos como um dicionário.
def concat_like_tuple(*args):
    final_string = ""
    for index, name in enumerate(args, 1):
        final_string += f"O nome da pessoa {index} é {name}.\n"
    return final_string


def concat_like_dict(**kwargs):
    final_string = (
        f'{kwargs["nome"]} {kwargs["sobrenome"]} tem {kwargs["idade"]} anos.\n'
    )
    return final_string


# print(concat_like_tuple("Cris", "Wallace", "Carol"))
# saída:
# O nome da pessoa 1 é Cris.
# O nome da pessoa 2 é Wallace.
# O nome da pessoa 3 é Carol.

# print(concat_like_dict(nome="Felipe", sobrenome="Silva", idade=25))
# saída:
# Felipe Silva tem 25 anos.