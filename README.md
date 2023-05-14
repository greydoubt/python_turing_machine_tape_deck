# python_turing_machine_tape_deck
python / json mechanism to run turing machines

input:
a json file describing a turing machine
one or more binary sequences (separated by an operator if not passing a singleton)

example:
for the zero TM, any input (0, 1, 10, 11, 110,...) will return output 0
for the addition TM, the sequence will be added mechanically by the TM and outputs their sum as a new sequence
