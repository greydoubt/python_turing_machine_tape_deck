class TuringMachine:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def run(self, tape):
        current_state = self.initial_state
        position = 0
        steps = []

        while current_state not in self.final_states:
            symbol = tape[position]
            if (current_state, symbol) not in self.transitions:
                break

            new_state, new_symbol, move = self.transitions[(current_state, symbol)]
            tape[position] = new_symbol

            steps.append((current_state, symbol, new_state, new_symbol, move))

            if move == "R":
                position += 1
                if position == len(tape):
                    tape.extend("_")
            elif move == "L":
                position -= 1
                if position < 0:
                    tape.insert(0, "_")

            current_state = new_state

        return steps
