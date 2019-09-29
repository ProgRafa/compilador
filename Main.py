from Reader import *
from AFD import *
from SymbolTable import *
from Token import *

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
        for sym in TABLE:
            lex = list(sym.keys())[0]
            p_type = list(sym.values())[0]
            self.lexers.append((Token(p_type, lex, 0, 0), AFD(sym["AFD"])))

    # Percorre os AFDs para validar uma entrada
    def find_token(self, p_word):
        token = Token('#ERROR', p_word, self.row, self.col)
        for lex in self.lexers:
            if lex[1].testing(list(p_word)):
                token = lex[0]
                token.lex = p_word
                token.row = self.row
                token.colunm = self.col
                break
        return token

    def parse(self):
        while self.reader.end_of_archive():
            #pede um caracter do buffer
            char = self.reader.pull_buffer()
            #remove espaços em branco mas conta como coluna
            if char == ' ':
                self.col += 1
                continue
            if char == '\t':
                self.col += 4
                continue
            #identifica quebra de linha, acrescenta a linha e zera a coluna
            if char == '\n':
                self.row += 1
                self.col = 0
                continue
            # testa os tokens usando o carcter char que veio do buffer
            test_char = self.find_token(char)

            #caso não seja um erro ou um identificador grave o Token
            if test_char.type != '#ERROR' and test_char.type != '#IDENTIFIER' and test_char.type != '#NUMBER':
                if self.word != '':
                    self.tokens.append(self.find_token(self.word))
                    self.find_token(word).to_string()
                    self.col += len(self.word)
                    self.word = ''
                    test_char.colunm = self.col
                    test_char.to_string()
                    self.tokens.append(test_char)
                else:
                    self.tokens.append(test_char)
                    test_char.to_string()
                self.col += 1
                continue
            self.word += char
            test_word = self.find_token(self.word)
            
            if test_word.type != '#ERROR' and test_word.type != '#IDENTIFIER':
                self.tokens.append(test_word)
                test_word.to_string()
                self.col += len(self.word)
                self.word = ''
        

compile = Compiler('./archives/Factorial.java')
compile.init_afds()
compile.parse()

for token in compile.tokens:
    print('###################################################')
    token.to_string()
    print('\n\n')