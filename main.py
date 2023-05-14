from json_file_handler import load_turing_machine_from_json

def print_tape(tape):
    print("Tape:", "".join(tape))

def main():
    file_path = "0_zero_function.json"  # Replace with your JSON file path
    turing_machine = load_turing_machine_from_json(file_path)

    tape = list(input("Enter input tape: "))  # Provide the initial tape input
    steps = turing_machine.run(tape)

    for i, step in enumerate(steps, start=1):
        current_state, symbol, new_state, new_symbol, move = step
        print(f"Step {i}:")
        print("Current State:", current_state)
        print("Symbol:", symbol)
        print("New State:", new_state)
        print("New Symbol:", new_symbol)
        print("Move:", move)
        print_tape(tape)
        print()

    print("Halted.")
    print_tape(tape)

if __name__ == "__main__":
    main()
