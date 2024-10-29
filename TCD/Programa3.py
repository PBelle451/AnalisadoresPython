# Pedro Belle Magalhães de Castro
# RA: 22103581
# Programa 3: Analisador léxico com tratamento de erros e tabela de símbolos

import re

# Criação do analisador léxico

class Lexer:
    def __init__(self):
        self.tabela_simbolos = {}  # Tabela de símbolos como propriedade
        self.palavras_chave = ["if", "else", "while", "return", "int", "float", "char"]  # Palavras chave
        for palavra in self.palavras_chave:
            self.tabela_simbolos[palavra] = "KEYWORD"  # Designa as palavras-chave que são inseridas dentro da tabela de símbolos

    # Função para criar e adicionar os tokens e seus tipos para a tabela de símbolos
    def adicionar(self, token, tipo_token):
        if token not in self.tabela_simbolos:
            self.tabela_simbolos[token] = tipo_token

    # Função para receber as palavras-chave inseridas
    def palavra_chave(self, token):
        return token in self.palavras_chave

    # Função para analisar os tokens recebidos e especificá-los
    def analise(self, code):
        tokens = []
        erros = []
        code = re.sub(r'\s+', ' ', code)
        code = re.sub(r'//.*|/\*.*?\*/', '', code, flags=re.DOTALL)

        # Fazendo a especificação dos tokens
        token_specification = [
            ('NUMBER', r'\d+(\.\d*)?'),  # Número integral ou decimal
            ('ASSIGN', r'='),  # Operador de atribuição
            ('END', r';'),  # Término de instrução
            ('ID', r'[A-Za-z_]\w*'),  # Identificadores
            ('OP', r'[+\-*/]'),  # Operadores aritméticos
            ('REL_OP', r'[<>]=?|==|!='),  # Operadores relacionais
            ('SKIP', r'[ \t]+'),  # Pular espaços e tabs
            ('MISMATCH', r'.'),  # Qualquer outro caractere
        ]

        # Irá separar os pares durante a especificação dos tokens
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        line_num = 1

        # Iteração dos tipos
        for mo in re.finditer(tok_regex, code):
            tipo = mo.lastgroup
            valor = mo.group()
            if tipo == 'NUMBER':
                tokens.append((tipo, valor))
                self.adicionar(valor, 'NUMBER')  # Irá adicionar para a lista de tokens caso for um tipo número
            elif tipo == 'ID':
                if self.palavra_chave(valor):
                    tipo = 'KEYWORD'
                tokens.append((tipo, valor))
                self.adicionar(valor, tipo)
            elif tipo in ('OP', 'REL_OP', 'ASSIGN', 'END'):
                tokens.append((tipo, valor))
            elif tipo == 'SKIP':
                continue
            elif tipo == 'MISMATCH':
                erros.append(f'Erro: caracter inesperado {valor!r} na linha {line_num}')
                # Insere uma mensagem de erro na linha caso não encontrar o tipo
            if valor == '\n':
                line_num += 1

        return tokens, erros

# Fim do código fonte

# Aplicação do código
if __name__ == "__main__":
    final_code = ''
    while True:
        code = input("Digite o código-fonte para análise léxica (digite fim para encerrar):\n")
        if code.lower() == "fim":
            break
        final_code += code + "\n"

    lexer = Lexer()
    tokens, erros = lexer.analise(final_code)

    print("\nTokens: ")
    for token in tokens:
        print(token)

    print("Erros: ")
    for erro in erros:
        print(erro)

    print("\nTabela de Símbolos: ")
    for simbolo, tipo in lexer.tabela_simbolos.items():
        print(f'{simbolo}: {tipo}')
