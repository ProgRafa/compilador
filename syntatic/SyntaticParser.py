from .SyntaticRules import SYNTATIC_RULES
from .SymbolTable import SymbolTable, SymbleTableRow
from .MegaAutomato import MegaAutomato
import copy

class SyntaticParser:
    def __init__(self):
        self.judge = MegaAutomato(SYNTATIC_RULES)
        self.symble_table = SymbolTable()
        self.block = []
        self.current_scope = '#GLOBAL'
    
    def analyze(self, pattern, pattern_lex):
        if "#START" in pattern:  
            self.block.append("{")
            if len(pattern) < 2:
                return "#START"

        if "#END" in pattern:
            self.block.pop()
            return "#END"

        if len(pattern) > 1:
            syntatic_rule = self.judge.find_rule(pattern)
            self.semantic(pattern, pattern_lex, syntatic_rule)
            return syntatic_rule

    def semantic(self, pattern, pattern_lex, rule):
        self.updateScope(pattern, pattern_lex, rule)
        self.semantic_rules(copy.copy(pattern), copy.copy(pattern_lex), rule)
        self.add_in_table(pattern, pattern_lex, rule)

    def updateScope(self, pattern, pattern_lex, rule):
        if rule == '#CLASS_DECLARATION' or rule == '#METHOD_DECLARATION':
            scope = ''
            for t, lex in zip(pattern, pattern_lex):
                if t == "#IDENTIFIER":
                    scope = '#SCOPE_' + lex.upper()
                    break
            self.current_scope = scope

    def semantic_rules(self, pattern, pattern_lex, rule):
        if rule == '#VARIABLE_DECLARATION' or rule == '#SET_VARIABLE':
            last = pattern.pop()
            lex = pattern_lex.pop()
            while last != '#EQUALS':
                if not(last == '#NUMBER' or last == '#IDENTIFIER' or last == '#SUM' or last == '#STRUCTIONEND'):
                    print("Erro semântico, variavel com tipo inteiro não pode receber outro valor", \
                          "\nInstrução :", *pattern_lex)
                symbol = self.symble_table.findByLabel(lex)
                if last == '#IDENTIFIER' and symbol and symbol.data_type != '#INTEGER':
                   print("Erro semântico, a variavel ", symbol.label, "é do tipo", symbol.data_type,
                         " enquanto a instrução espera por um tipo inteiro",  \
                          "\nInstrução :", *pattern_lex, symbol.label) 
                if last == '#IDENTIFIER' and symbol is None:
                    print("Erro semântico, a variavel ", lex, "não foi declarada", \
                          "\nInstrução :", *pattern_lex, lex) 
                if last == '#IDENTIFIER' and symbol and symbol.scope != self.current_scope:
                    print("Erro semântico, a variavel ", lex, "está fora do escopo", \
                          "\nInstrução :", *pattern_lex, lex) 

                last = pattern.pop()
                lex = pattern_lex.pop()


    def add_in_table(self, pattern, pattern_lex, rule):
        if rule == '#VARIABLE_DECLARATION':
            row = SymbleTableRow(pattern_lex[1], pattern[1], self.current_scope, pattern[0])
            self.symble_table.add(row)
        elif rule == '#METHOD_DECLARATION':
            label = ''
            token = ''
            data = ''
            for t, lex in zip(pattern, pattern_lex):
                if t == "#IDENTIFIER":
                    token = t
                    label = lex if label == '' else label
                if t == '#INTEGER' or t == '#VOID':
                    data = t
            row = SymbleTableRow(label, token, self.current_scope, data)
            self.symble_table.add(row)
        

