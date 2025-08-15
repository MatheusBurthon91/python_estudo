PI = 3.14

#Funções de area do circulo, retângulo e quadrado

#quadrado
def calculate_square(side):
    '''calcular a area do quadrado'''
    return side ** 2


#retângulo
def calculate_retangle(width, length):
    '''calcular a area do retangulo'''
    return width * length;


#circulo
def calculate_circle(ray):
    '''calcular a area do circulo'''
    return PI * (ray ** 2)

if __name__ == "__main":
    print(calculate_square(8))
    print(calculate_retangle(2, 3))
    print(calculate_circle(5))