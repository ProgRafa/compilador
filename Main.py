from Reader import *
from AFD import *
from AFDPatterns import *
from Token import *
from SymbolTable import SymbleTableRow, SymbolTable

import sys
import copy

row = SymbleTableRow('identifier', 'SIDENTIFIER', 'GLOBAL', 'INTEGER')
table = SymbolTable()

table.add(row)
table.toString()
table.set_attribute('label', 'class', row.id)
table.toString()


# class Compiler:
#     def __init__(self, archive):
#         self.reader = Reader(32, archive)
#         self.row = 1
#         self.col = 1
#         self.tokens = []     
#         self.word = ''

#     # Monta os AFDs a partir da tabela de símbolos da linguagem
#     def init_afds(self):
#         self.lexers = []
#         for sym in TABLE:
#             lex = list(sym.keys())[0]
#             p_type = list(sym.values())[0]
#             self.lexers.append((Token(p_type, lex, 0, 0), AFD(sym["AFD"])))

#     # Percorre os AFDs para validar uma entrada
#     def find_token(self, p_word):
#         c_row = copy.copy(self.row)
#         c_col = copy.copy(self.col)
#         token = Token('#ERROR', p_word, c_row, c_col)
#         for lex in self.lexers:
#             if lex[1].testing(list(p_word)):
#                 token = lex[0]
#                 token.lex = p_word
#                 token.row = c_row
#                 token.colunm = c_col
#                 break
#         return token

#     def parse(self):
#         while self.reader.end_of_archive():
#             # pede um caracter do buffer
#             char = self.reader.pull_buffer()
#             # remove espaços em branco mas conta como coluna
#             if char == ' ':
#                 self.col += 1
#                 continue
#             # identifica o tab e conta como 4 colunas
#             if char == '\t':
#                 self.col += 4
#                 continue
#             # identifica quebra de linha, acrescenta a linha e zera a coluna
#             if char == '\n':
#                 self.row += 1
#                 self.col = 1
#                 continue
#             # testa os tokens usando o carcter char que veio do buffer
#             test_char = self.find_token(char)

#             # identifica que o char é um token, grava a word anterior ao char como identificador
#             if test_char.type != '#ERROR' and test_char.type != '#IDENTIFIER':
#                 if self.word != '':
#                     self.tokens.append(copy.copy(self.find_token(self.word)))
#                     self.col += len(self.word)
#                     self.word = ''
#             self.word += char
#             test_word = self.find_token(self.word)
            
#             if test_word.type != '#ERROR' and test_word.type != '#IDENTIFIER':
#                 self.tokens.append(copy.copy(test_word))
#                 self.col += len(self.word)
#                 self.word = ''
            
# # remover o nome do arquivo dos argumentos        
# sys.argv.pop(0)
# arguments = sys.argv
# archive = './archives/'
# if len(arguments) > 0:
#     archive += arguments[0]
# else:
#     archive += 'BinarySearch.java'

# print("Analisando o programa", archive)
# compile = Compiler(archive)
# compile.init_afds()
# compile.parse()

# for token in compile.tokens:
#     print('###################################################')
#     token.to_string()
#     print('\n\n')