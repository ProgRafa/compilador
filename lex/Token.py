class Token:
    def __init__(self, p_type, lex, colunm, row):
        self.type = p_type
        self.lex = lex
        self.colunm = colunm
        self.row = row

    def to_string(self):
        print("Type - ", self.type)
        print("Lex - ", self.lex)
        print("Colunm - ", self.colunm)
        print("Row - ", self.row)