class TuringMachine:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.final_states = final_states
        self.tape = []
        self.head_position = 0
        self.steps = []

    def load_tape(self, input_string):
        self.tape = list(input_string)

    def step(self):
        current_symbol = self.tape[self.head_position]
        if (self.current_state, current_symbol) not in self.transitions:
            return False  # Invalid transition, halt execution

        next_state, new_symbol, move_direction = self.transitions[(self.current_state, current_symbol)]
        self.tape[self.head_position] = new_symbol
        self.current_state = next_state
        self.steps.append((self.current_state, ''.join(self.tape)))

        if move_direction == 'L':
            self.head_position -= 1
            if self.head_position < 0:
                self.tape.insert(0, '_')
                self.head_position = 0
        elif move_direction == 'R':
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append('_')

        return True

    def run(self):
        self.steps.append((self.current_state, ''.join(self.tape)))
        while self.current_state not in self.final_states:
            if not self.step():
                break
