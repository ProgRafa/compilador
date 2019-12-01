from lex import *
from Reader import Reader
from syntatic import SyntaticParser

import sys
import copy

class Compiler:
    def __init__(self, archive):
        self.reader = Reader(32, archive)
        self.row = 1
        self.col = 1
        self.tokens = []     
        self.word = ''

    # Monta os AFDs a partir da tabela de símbolos da linguagem
    def init_afds(self):
        self.lexers = []
        for sym in LEX_RULES:
            lex = list(sym.keys())[0]
            p_type = list(sym.values())[0]
            self.lexers.append((Token(p_type, lex, 0, 0), Lex(sym["AFD"])))

    # Percorre os AFDs para validar uma entrada
    def find_token(self, p_word):
        c_row = copy.copy(self.row)
        c_col = copy.copy(self.col)
        token = Token('#ERROR', p_word, c_row, c_col)
        for lex in self.lexers:
            if lex[1].testing(list(p_word)):
                token = lex[0]
                token.lex = p_word
                token.row = c_row
                token.colunm = c_col
                break
        return token

    def parse_lex(self):
        while self.reader.end_of_archive():
            # pede um caracter do buffer
            char = self.reader.pull_buffer()
            # remove espaços em branco mas conta como coluna
            if char == ' ':
                if self.word != '':
                    self.tokens.append(copy.copy(self.find_token(self.word)))
                    self.col += len(self.word)
                    self.word = ''
                self.col += 1
                continue
            # identifica o tab e conta como 4 colunas
            if char == '\t':
                self.col += 4
                continue
            # identifica quebra de linha, acrescenta a linha e zera a coluna
            if char == '\n':
                if self.word != '':
                    self.tokens.append(copy.copy(self.find_token(self.word)))
                    self.col += len(self.word)
                    self.word = ''
                self.row += 1
                self.col = 1
                continue
            # testa os tokens usando o carcter char que veio do buffer
            test_char = self.find_token(char)

            if test_char.type == '#ERROR':
                print("Erro LÉXICO na linha", test_char.row, \
                          "coluna", test_char.colunm, \
                          "\nInstrução :", *test_char.lex)
                return None

            # identifica que o char é um token, grava a word anterior ao char como identificador
            if test_char.type != '#ERROR' and test_char.type != '#IDENTIFIER':
                if self.word != '':
                    self.tokens.append(copy.copy(self.find_token(self.word)))
                    self.col += len(self.word)
                    self.word = ''
            self.word += char
            test_word = self.find_token(self.word)
            
            if test_word.type != '#ERROR' and test_word.type != '#IDENTIFIER':
                self.tokens.append(copy.copy(test_word))
                self.col += len(self.word)
                self.word = ''

    def parse_syntatic(self):
        self.instructions = []
        syntatic = SyntaticParser()
        token = copy.copy(self.tokens.pop(0))
        sentence = []
        sentence_lex = []
        
        while self.tokens:
            initial_token = token
            sentence_lex.append(token.lex)
            sentence.append(token.type)
            new_token = copy.copy(self.tokens.pop(0))
            if (token.row != new_token.row) or not self.tokens:
                instruction = syntatic.analyze(sentence, sentence_lex)

                if instruction:
                    self.instructions.append(instruction)
                else:
                    print("Erro sintático na linha", initial_token.row, \
                          "coluna", initial_token.colunm, \
                          "\nInstrução :", *sentence_lex)
                    return None

                sentence.clear()
                sentence_lex.clear()
                token = new_token
            else:
                token = new_token
            
            
# remover o nome do arquivo dos argumentos        
sys.argv.pop(0)
arguments = sys.argv
archive = './archives/'
if len(arguments) > 0:
    archive += arguments[0]
else:
    archive += 'BinarySearch.java'

print("Analisando o programa", archive)
compile = Compiler(archive)
compile.init_afds()
compile.parse_lex()
compile.parse_syntatic()

# for token in compile.tokens:
#     print('###################################################')
#     token.to_string()
#     print('\n\n')

for instruction in compile.instructions:
    print(instruction)
