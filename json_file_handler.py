import json
from turing_machine import TuringMachine

def load_turing_machine_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    
    states = data["states"]
    alphabet = data["alphabet"]
    transitions = {tuple(key.split("_")): value for key, value in data["transitions"].items()}
    initial_state = data["initial_state"]
    final_states = data["final_states"]
    
    return TuringMachine(states, alphabet, transitions, initial_state, final_states)
