class Automaton:

    def __init__(self, final, initial=0):
        self.initial_state = self.state = initial
        self.final_states = final

    def reset(self):
        self.state = self.initial_state

    def accept(self):
        return self.state in self.final_states

    def get_state(self):
        return self.state

    def process_atom(self, item):
        raise NotImplementedError
