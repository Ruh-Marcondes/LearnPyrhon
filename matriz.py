import math
import os

# Comando que mostra um guia de comandos da matrix
def matrix_help():
    print('Adicione numeros digitando abaixo.\nCaso queira usar um comando coloque "/" e em seguida um dos comandos abaixo')
    print(' - "quit": Finaliza o codigo.')
    print(' - "help": Mostra novamente esse guia de comandos.')
    print(' - "show": Mostra a matrix atual.')
    print(' - "reset": Reseta a matrix atual.')
    print(' - "clear": Limpa o console.')
    print(' - "--": Remove o ultimo numero adicionado.')
    print(' - "det": Acha o determinante da matrix atual.')
    print(' - "cofactor": Mostra o cofactor da matrix atual na coluna e linha 1.')

# Comando para conseguir o tamanho da matrix.
def matrix_size(matrix):
    try:
        size = int(math.sqrt(len(matrix)))
        if size==1:
            return "Tamanho da matrix invalida"
    except:
        return "Tamanho da matrix invalida"
    return size

# Comando para mostrar a matrix.
def show_matrix(matrix):
    size = matrix_size(matrix)
    if(len(matrix) == 1):
        print("[ {} ]".format(matrix[0]))
    else:
        if type(size).__name__ == "str":
            return size

        for i in range(0, size): # Linha
            text = ""
            for j in range(0, size): # Numero em coluna baseado na linha
                if j == size-1:
                    text += " {} ".format(matrix[j + (size * i)])
                else:
                    text += " {},".format(matrix[j + (size * i)])
            print("[{}]".format(text))

# Comando para mostrar um numero na matrix.
def matrix_number(i, j):
    size = matrix_size(matrix)
    
    if type(size).__name__ == "str":
        return size

    if i >= size:
        return "Linha acima do limite"
    if j >= size:
        return "Coluna acima do maximo"
    if i < 0:
        return "Linha abaixo do minimo"
    if j < 0:
        return "Coluna abaixo do minimo"

    return matrix[j + (size * i)]

# Comando para achar a determinante da matrix.
def matrix_det(matrix):
    size = matrix_size(matrix)
    det = 0
    if(len(matrix) == 1): # Matrix de Ordem 1
        det = matrix[0]
    else:
        if size == 2: # Matrix de Ordem 2
            det = o2_det(matrix)
        elif size == 3: # Matrix de Ordem 3
            det = o3_det(matrix)
        else: # Matrix de Ordem 4 ou maior
            a = 0
            for i in range(0, size): # Linha
                a = matrix[size * i] * (math.pow(-1, i + 2))
                d = o3_det(matrix_cofactor(matrix, 0, 0))
                print(i)
                print(a)
                print(d)
                det += a * d 
                print(det)
                print("-----------------------")
    print("det = {}".format(det))

def matrix_cofactor(matrix, ci, cj):
    nMatrix = []
    size = matrix_size(matrix)
    for i in range(0, size): # Linha
        if(i != ci):
            for j in range(0, size): # Coluna
                if(j != cj):
                    n = j + i * size
                    nMatrix.append(matrix[n])
    if(matrix_size(matrix) != 4):
        nMatrix = matrix_cofactor(nMatrix, 0, 0)
    return nMatrix
                
# Comando para achar a determinante da matrix de ordem 2.
def o2_det(matrix):
    dP = matrix[0] * matrix[3]
    dS = matrix[1] * matrix[2]
    return dP - dS

# Comando para achar a determinante da matrix de ordem 3.
def o3_det(matrix):
    dP = (matrix[0] * matrix[4] * matrix[8]) + (matrix[1] * matrix[5] * matrix[6]) + (matrix[2] * matrix[3] * matrix[7])
    dS = (matrix[2] * matrix[4] * matrix[6]) + (matrix[0] * matrix[5] * matrix[7]) + (matrix[1] * matrix[3] * matrix[8])
    return dP - dS

# Variaveis
matrix = []

# Input do usuario para configurações da matrix.
print('[!] Recomendado usar "/help" para conseguir mais informações [!]')
while True:
    str_input = input("# ")
    if str_input[0] == "/":
        if str_input[1:] == "quit":
            break
        elif str_input[1:] == "help":
            matrix_help()
        elif str_input[1:] == "show":
            show_matrix(matrix)
        elif str_input[1:] == "reset":
            matrix = []
        elif str_input[1:] == "--":
            matrix = matrix[:-1]
        elif str_input[1:] == "clear":
            os.system('cls')
        elif str_input[1:] == "det":
            matrix_det(matrix)
        elif str_input[1:] == "cofactor":
            show_matrix(matrix_cofactor(matrix, 0, 0))
        else:
            print("Comando não encontrado!")
    else:
        try:
            number = float(str_input)
            matrix.append(number)
        except:
            print("Um erro ocorreu ao inserir esse numero.")