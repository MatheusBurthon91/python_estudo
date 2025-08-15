# from faker import Faker

#Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
import math

def get_biggest_number(num_1, num_2):
    if (num_1 > num_2):
        return num_1
    elif (num_1 < num_2):
        return num_2
    else:
        return 'Os numeros são iguais.'
    
# print(get_biggest_number(2, 1))
# print(get_biggest_number(1, 2))
# print(get_biggest_number(2, 2))

#Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def calculate_arithmetic_medium(numbers):
    sum = 0
    for number in numbers:
        sum += number
    
    arithmetic_medium = sum / len(numbers)
    return arithmetic_medium


# print(calculate_arithmetic_medium([5, 2, 5, 6, 7, 8, 10, 2, 1]))

#Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1, 
#imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:

# n = 5

# *****
# *****
# *****
# *****
# *****


#codigo em natura
def make_square_asteric(num):
    asterisc = '*'
    concat_string = ''
    numbers = range(num)
    for _ in numbers:
        concat_string += f"{num * asterisc}\n"
    
    return concat_string


# dica de codigos legiveis com o chatgpt

# 1️⃣ Nomes de variáveis mais claros

# asterisc pode ser só '*' direto na multiplicação.

# concat_string → resultado ou output.

# 2️⃣ Evitar concatenar string dentro de loop

# Em Python, concatenar com += dentro de um loop não é tão eficiente, 
# porque strings são imutáveis.

# Melhor: criar uma lista de linhas e depois juntar com '\n'.join(...).

# 3️⃣ O loop pode ser mais direto

# Você não está usando o índice, então pode fazer só for _ in range(num): ....

# 4️⃣ Remover variáveis desnecessárias

# Não precisa criar numbers = range(num) antes do loop.

# print(make_square_asteric(5))

#código limpo
def make_square_asterisc_clean(n):
    # resultado = []
    # for _ in range(n):
    #     resultado.append(f"{n * '*'}")

    # return "\n".join(resultado) # depois da mudança
    return "\n".join(['*' * n for _ in range(n)]) # compreensão de lista

# print(make_square_asterisc_clean(5))

#Exercício 4: Crie uma função que receba uma lista de nomes e 
#retorne o nome com a maior quantidade de caracteres. 
#Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"],
#o retorno deve ser "Fernanda".

names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

def get_biggest_name(names):
    biggest_name = names[0]
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
    
    return biggest_name

# print(get_biggest_name(names))


#Exercício 5: Conlre que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
#que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas
#de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).

# 1 litro para 3 metros²
# 18 litros de tinta custam R$80.00


def calculate_paint_and_price(n):
    """Calcula a quantidade de latas e o custo total para pintar uma área em m².""" 
    litros_por_lata = 18
    preco_litros_por_lata = 80
    cobertura_por_litro = n / 3
    
    quantidade_de_tinta_comprada = math.ceil(cobertura_por_litro / litros_por_lata)
    preco_total_de_tinta = preco_litros_por_lata * quantidade_de_tinta_comprada
    return (quantidade_de_tinta_comprada, preco_total_de_tinta)


# print(calculate_paint_and_price(27))


#Exercício 6: Crie uma função que receba os três lado de um triângulo e 
#informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.

#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.



# def define_is_an_triangle(l1, l2, l3):
#     is_triangle = (
#             l1 + l2 > l3 and
#             l2 + l3 > l1 and
#             l1 + l3 > l2
#     )
#     if is_triangle:
#         "aqui veremos os tipos de triangulo"
#         if l1 == l2 == l3:
#             return "Triângulo Equilátero"
#         elif l1 == l2 or l2 == l3 or l1 == l3:
#             return "Triângulo Isósceles"
#         else:
#             return "Triângulo Escaleno"
#     else:
#         return "Não é triangulo"

def define_triangle(l1, l2, l3): # versão clean
    if not (l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2):
        return "Não é triângulo"

    if l1 == l2 == l3:
        return "Triângulo Equilátero"
    elif l1 == l2 or l2 == l3 or l1 == l3:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


    
# print(define_triangle(60, 20, 100)) # Não é triângulo
# print(define_triangle(60, 60, 60)) # Triângulo Equilátero
# print(define_triangle(60, 80, 60)) # Triângulo Isósceles
# print(define_triangle(90, 80, 60)) # Triângulo Escaleno


#Gere uma lista com os quadrados dos números de 1 a 10.
def set_list_with_square_numbers(n):
    # square_numbers_list = []
    # for number in range(1, n + 1):
    #     square_numbers_list.append(number ** 2)
    # return square_numbers_list
    return [number ** 2 for number in range(1, n + 1)]

# print(set_list_with_square_numbers(10))

#Gere uma lista apenas com os números pares de 0 a 20.
def set_list_with_pair_numbers(num):
    # pair_numbers = []
    # for number in range(0, num + 1):
    #     if number % 2 == 0:
    #         pair_numbers.append(number)
    
    # return pair_numbers
    return [number for number in range(0, num + 1) if number % 2 == 0]

# print(set_list_with_pair_numbers(20))

#A partir de uma lista de nomes, gere outra lista com todos em maiúsculas.
def set_list_names_with_upper_case_letters(array):
    # upper_case_list = []
    # for names in array:
    #     upper_case_list.append(names.upper())
        
    # return upper_case_list
    return [names.upper() for names in array]

# print(set_list_names_with_upper_case_letters(names))


#Dada uma lista, descubra o menor elemento. Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.
def find_smallest_number(array):
    result = array[0]
    for item in array:
        if item < result:
            result = item
    
    return result

# print(find_smallest_number([5, 9, 3, 19, 70, 8, 100, 2, 35, 1, 27]))


# Exercício 2: Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um triângulo retângulo com n asteriscos de base. 
# Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:

# n = 5

# *
# **
# ***
# ****
# *****


def make_stairs_asterisc(n):
    return ('\n').join([index * '*' for index in range(1, n + 1)])
        
# print(make_stairs_asterisc(5))

#Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N. Por exemplo, para N = 5, o valor esperado será 15
def make_summation_of_gauss(n):
    result = 0
    for number in range(1, n + 1):
        result += number
    
    return result

print(make_summation_of_gauss(5))

#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#   Álcool:
#     - Até 20 litros, desconto de 3% por litro;
#     - Acima de 20 litros, desconto de 5% por litro.
#   Gasolina:
#     - Até 20 litros, desconto de 4% por litro;
#     - Acima de 20 litros, desconto de 6% por litro.

# Escreva uma função que receba o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A - álcool, G - gasolina), 
# e retorne o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço do litro do álcool é R$ 1,90.
def pay_fuel_liter(n):
    a = 'álcool'
    g = 'gasolina'
    preco_alcool = 0
    preco_gasolina = 0
    
    if n <= 20:
        preco_alcool = n * 1.90 * (1 - 0.03)
        preco_gasolina = n * 2.50 * (1 - 0.04)
    else:
        preco_alcool = n * 1.90 * (1 - 0.05)
        preco_gasolina = n * 2.50 * (1 - 0.06)
    
    return f"o preço do {a} é R${preco_alcool} e o da {g} é R${preco_gasolina}"
       
       
# print(pay_fuel_liter(25), 'minha função')

# compreensão de lista com condição
#Gere uma lista com os múltiplos de 3 entre 1 e 30.
def generate_list_with_multiply_by_three(num):
    return [number for number in range(1, num + 1) if number % 3 == 0]


# print(generate_list_with_multiply_by_three(30))

# Pegue apenas palavras com mais de 5 letras de uma lista.

# fake = Faker()
# palavras_aleatorias = [fake.word() for _ in range(10)]


def get_five_words_in_list(words):
    return [word for word in words if len(word) > 5]

# print(get_five_words_in_list(palavras_aleatorias))

#Gere uma lista com "par" ou "ímpar" para cada número de 0 a 10.
def generate_list_with_pair(number):
    return [index for index in range(number + 1) if index % 2 == 0]

# print(generate_list_with_pair(10))

def generate_list_with_odd(number):
    return [index for index in range(number + 1) if index % 2 != 0]

# print(generate_list_with_odd(10))

#De uma lista ["a", "b", "c"], crie:
alfa = ["a", "b", "c"]

def create_list_tupple(commom_list):
    return [item for item in enumerate(commom_list)]

# print(create_list_tupple(alfa))

#Gere todas as combinações possíveis entre [1, 2] e ["x", "y"].
#resultado - [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')]
def generate_combinations(list_1, list_2):
    # result = []
    # for item in list_1:
    #     for el in list_2:
    #         result.append((item, el))
    
    # return result
    return [(item, el) for item in list_1 for el in list_2]

# print(generate_combinations([1, 2], ["x", "y"]))

#Gere todos os trios (i, j, k) de números 0 a 2, sem repetir índices.
#Vai gerar 6 combinações.
num_list = [0, 1, 2]

#dicas
# Pense em 3 variáveis (i, j, k) que vão assumir valores de 0 a 2.

# Use três loops for aninhados para testar todas as combinações possíveis.

# Como o enunciado fala “sem repetir índices”, você precisa ignorar casos onde algum valor se repete (ex.: (0, 0, 1) não pode).

# Para filtrar, pode usar uma condição do tipo:

#if i != j and j != k and i != k:

def generate_trio(num):
    # result = []
    # for i in range(0, num + 1):
    #     for j in range(0, num + 1):
    #         for k in range(0, num + 1):
    #             if i != j and j != k and i != k:
    #                 result.append((i, j, k))
    
    # return result
    return [(i, k, j) for i in range(0, num + 1) for k in range(0, num + 1) for j in range(0, num + 1) if i != j and j != k and i != k]


# print(generate_trio(2))

#Gere todas as combinações (x, y) de números 0 a 4, mas só quando x < y.
def generate_number_combinations(num):
    # result = []
    # for x in range(0, num + 1):
    #     for y in range(0, num + 1):
    #         if x < y:
    #             result.append((x, y))
                
    # return result
    return [(x, y) for x in range(0, num + 1) for y in range(0, num + 1) if x < y]


# print(generate_number_combinations(4))

#Objetivo: olhar um código pronto e entender passo a passo.

def explain_the_code():
    return [(i, j, k) for i in range(3) for j in range(3) for k in range(3) if i != j != k != i]


# o codigo tem um objeto de gerar uma lista e essa lista vai ter itens em formato de tuplas, para isso pegamos cada variavel e desempacotamos para dizer de onde vem eles
# para cada loop, cada loop vai interagir com o intervalo de 0 a 2 e o resultado final vai ser uma tupla que vai conter diversas combinações de 0 - 2, mas sem repetições 
# dentro de cada item

#Que valores (i, j, k) aparecem? valores de 0 a 2 por cada tupla sem repetição nas tuplas

# Quantos no total? 6 items

#Por que essa condição i != j != k != i funciona?
# essa condição faz uma verificação antes de adicionar um item no item a ser inserido na lista final

# “Escada invertida” (alinhada à direita)

# Checagem mental: o comprimento da linha é sempre n.

def make_inverted_stairs(n):
    return '\n'.join([' ' * (n - i) + '*' * i for i in range(1, n + 1)])

# print(make_inverted_stairs(5))

# algoritmo da pirâmide

# Checagem mental: se somar espaços+asteriscos, dá sempre 2*n - 1.
def make_pyramid(n):
    # result = []
    # for i in range(1, n + 1):
    #     result.append(' ' * (n - i) + '*' * (2*i - 1))
    return '\n'.join(' ' * (n - i) + '*' * (2*i - 1) for i in range(1, n + 1))


# print(make_pyramid(5))
