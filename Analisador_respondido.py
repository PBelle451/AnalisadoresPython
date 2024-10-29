import re

# Função para o analisador léxico
def analisador_lexico(expressao):
    # Tabela de símbolos
    tabela_simbolos = []

    # Expressões regulares para identificar lexemas
    padrao_identificador = r'[a-zA-Z]+'
    padrao_numero = r'\d+'
    padrao_operador = r'[\+\-\*\/]'
    padrao_atribuicao = r'='
    padrao_delimitador = r';'

    # Expressão regular combinada
    padrao_completo = f'{padrao_identificador}|{padrao_numero}|{padrao_operador}|{padrao_atribuicao}|{padrao_delimitador}'

    # Identificação dos lexemas na expressão
    tokens = re.findall(padrao_completo, expressao)

    # Mapeamento dos tipos de token
    tipos_tokens = {
        padrao_identificador: 'Identificador',
        padrao_numero: 'Número',
        padrao_operador: 'Operador',
        padrao_atribuicao: 'Operador de atribuição',
        padrao_delimitador: 'Delimitador'
    }

    # Construção da tabela de símbolos
    for token in tokens:
        for padrao, tipo in tipos_tokens.items():
            if re.match(padrao, token):
                tabela_simbolos.append((token, tipo))
                break

    # Saída da tabela de símbolos
    print("Tabela de Símbolos")
    print("Lexema\tToken (tipos de token)")
    for lexema, token in tabela_simbolos:
        print(f"{lexema}\t{token}")

    return tabela_simbolos

# Função para o analisador sintático
def analisador_sintatico(tabela_simbolos):
    # Verificação de erros sintáticos
    erro_sintatico = False

    # Condição 1: Dois operandos seguidos por espaços em branco
    for i in range(len(tabela_simbolos) - 1):
        if tabela_simbolos[i][1] == 'Identificador' and tabela_simbolos[i+1][1] == 'Identificador':
            erro_sintatico = True
            print("Erro sintático: Dois operandos seguidos e separados por espaços em branco.")
            break

    # Condição 2: Dois operadores seguidos por espaços em branco
    for i in range(len(tabela_simbolos) - 1):
        if tabela_simbolos[i][1] == 'Operador' and tabela_simbolos[i+1][1] == 'Operador':
            erro_sintatico = True
            print("Erro sintático: Dois operadores seguidos e separados por espaços em branco.")
            break

    # Condição 3: Mais de três operandos ou operadores após o símbolo de atribuição
    atribuicao_encontrada = False
    operandos_apos_atribuicao = 0
    for lexema, token in tabela_simbolos:
        if token == 'Operador de atribuição':
            atribuicao_encontrada = True
        elif atribuicao_encontrada and token in ['Identificador', 'Número', 'Operador']:
            operandos_apos_atribuicao += 1

    if operandos_apos_atribuicao > 3:
        erro_sintatico = True
        print("Erro sintático: Foram encontrados mais de três operandos ou operadores após o símbolo de atribuição.")

    # Condição 4: Operandos e operadores antes do símbolo de atribuição
    if tabela_simbolos[0][1] != 'Identificador' and tabela_simbolos[0][1] != 'Número':
        erro_sintatico = True
        print("Erro sintático: Operandos ou operadores antes do símbolo de atribuição.")

    return erro_sintatico

# Função principal
def main():
    # Entrada do código fonte
    expressao = input("Digite a expressão: ")

    # Análise léxica
    tabela_simbolos = analisador_lexico(expressao)

    # Análise sintática
    erro_sintatico = analisador_sintatico(tabela_simbolos)

    if not erro_sintatico:
        print("Expressão sintaticamente correta.")

if __name__ == "__main__":
    main()
