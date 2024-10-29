# Pedro Belle Magalhães de Castro
# RA: 22103581

# Essa função separa as operações de soma, subtração, multiplicação e divisão
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


# Define quais são os operadores
def is_operator(c):
    return c in ('+', '-', '*', '/')


# Função Principal de Conversão
# Infixo para Pós-Fixo
def infix_to_postfix(expression):
    stack = []  # Cria a pilha de itens que serão removidos da saída
    output = [] # Lista de saída
    i = 0
    while i < len(expression):
        char = expression[i]    # Adiciona as expressões inseridas para dentro da lista

        if char == ' ':     # Lê os espaços caso tiver e adiciona a lista
            i += 1
            continue

        if char.isdigit():
            num = ''    # Variável que recebera os números
            while i < len(expression) and expression[i].isdigit(): # Caso o dígito inserido for um número
                num += expression[i]    # Variável num recebe o valor do digito inserido
                i += 1
            output.append(num)      # Adiciona os números inseridos para dentro da lista de saída
            continue

        elif char == '(':
            stack.append(char)  # É adicionado a pilha de itens que serão removidos da saída

        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())  # A lista de saída adiciona os dígitos que foram removidos da pilha
            stack.pop()  # Remover '('

        elif is_operator(char): # Caso os digitos forem operadores
            while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(char): # Lê os operadores definidos na função de precedência e compara com os inseridos durante a leitura
                output.append(stack.pop())  # Adiciona para saída os itens removidos
            stack.append(char)  # Operadores são adicionados ao final da lista

        i += 1

    while stack:
        output.append(stack.pop())

    # Reordenar a saída para garantir que os números venham primeiro e os operadores depois
    numbers = [token for token in output if token.isdigit()]
    operators = [token for token in output if is_operator(token)]
    return ' '.join(numbers + operators)    # Coloca os números a esquerda e os operadores a direita

# Fim do código fonte

# Exemplo de aplicação
if __name__ == "__main__":
    expression = input("Digite a expressão infixa: ")
    postfix_expression = infix_to_postfix(expression)
    print("Expressão pós-fixa:", postfix_expression)
