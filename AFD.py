class AFD:
    def __init__(self, afd): 
        self.states = afd['states']
        self.rules = afd['rules']

    def testing(self, word):
        self.current_state = self.states[0]
        stop = False
        while word and not stop:
            char = str(word.pop(0))
            for key, value in self.rules[self.current_state].items():
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