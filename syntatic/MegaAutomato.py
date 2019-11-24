from .AFND import AFND
import copy

class MegaAutomato:
    # inicia todos os automatos a partir das regras
    def __init__(self, rules):
        self.afnd_list = []
        for sym in rules:
            p_type = list(sym.values())[0]
            self.afnd_list.append((p_type, AFND(sym["AFD"])))
    
    # Percorre os AFDs para validar uma entrada
    def find_rule(self, pattern):
        rule = None
        for afnd in self.afnd_list:
            # print(afnd[0], ' - ', afnd[1].testing2(copy.copy(pattern), None))
            if afnd[1].testing2(copy.copy(pattern), None):
                rule = afnd[0]
                break
        return rule