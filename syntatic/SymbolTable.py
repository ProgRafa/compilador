import random
import copy

class SymbolTable():
    def __init__(self,):
        self.table = {}
        
    def add(self, row):
        if row.id in self.table:
            self.table[row.id] = row
        else:
            self.table[row.id] = row

    def delete(self, id):
        if id in self.table:
            removed = copy.copy(self.table[id])
            self.table[id] = None
            del self.table[id]
            return removed

    def find(self, id):
        if id in self.table:
            return self.table[id]
        else:
            return None

    def findByLabel(self, label):
        for id in self.table:
            if self.table[id].label == label:
                return self.table[id]
        
        return None
    
    def set_attribute(self, attr_name, attr_value, id):
        if id in self.table:
            row = self.table[id]
            row.__dict__[attr_name] = attr_value
            return self.table[id]
    
    def get_attribute(self, attr_name, id):
        if id in self.table:
            row = self.table[id]
            return row[attr_name]
    
    def toString(self):
        for id in self.table:
            print('key : ', id, 'value : ', self.table[id].to_string())


class SymbleTableRow:
    def __init__(self, label, token_type, scope, data_type):
        self.id = str("%032x" % random.getrandbits(128))
        self.label = label
        self.token_typen = token_type
        self.scope = scope
        self.data_type = data_type
        self.value = None
    
    def to_string(self):
        return self.label + ' - ' + self.token_typen + ' - ' + self.scope + ' - ' + self.data_type