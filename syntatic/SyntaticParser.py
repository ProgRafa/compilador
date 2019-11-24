from .SyntaticRules import SYNTATIC_RULES
from .SymbolTable import SymbolTable, SymbleTableRow
from .MegaAutomato import MegaAutomato

class SyntaticParser:
    def __init__(self):
        self.judge = MegaAutomato(SYNTATIC_RULES)
        self.symble_table = SymbolTable()
        self.block = []
    
    def analyze(self, pattern):
        if "#START" in pattern:  
            self.block.append("{")
            if len(pattern) < 2:
                return "#START"

        if "#END" in pattern:
            self.block.pop()
            return "#END"

        if len(pattern) > 1:
            return self.judge.find_rule(pattern)