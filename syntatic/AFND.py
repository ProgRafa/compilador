import copy

class AFND:
    def __init__(self, afd): 
        self.states = afd['states']
        self.rules = afd['rules']

    def testing2(self, word, current_state):
        if current_state is None:
            current_state = self.states[0]
        if word:
            sym = str(word.pop(0))
            flag = False
            for symbols, states in self.rules[current_state].items():
                if symbols.find(sym) >= 0:
                    for state in states:
                        flag = flag or self.testing2(copy.copy(word), state)
                    break
                else:
                    return False
            return flag
        else:
            if current_state == self.states[-1]:
                return True
            else:
                return False

    def testing(self, word):
        self.current_state = self.states[0]
        stop = False
        while word and not stop:
            char = str(word.pop(0))
            
            for key, value in self.rules[self.current_state].items():
                print(key, ' - ', value)
                print(char)
                if key.find(char) >= 0:
                    self.current_state = value
                    stop = False
                    break
                else:
                    stop = True
        if self.current_state == self.states[-1]:
            return True
        else:
            return False
    
    def to_string(self):
        print("States - ", self.states)
        print("Initial State - ", self.states[0])
        print("Final State - ", self.states[-1])
        print("Rules - ", self.rules)