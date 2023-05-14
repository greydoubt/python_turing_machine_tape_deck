# python_turing_machine_tape_deck
python / json mechanism to run turing machines

## offering a bounty if you can create a linter for this file format that can tell before running whether any arbitrary file in this format will halt on a valid answer or go on forever

input:
a json file describing a turing machine
one or more binary sequences (separated by an operator if not passing a singleton)

example:
for the zero TM, any input (0, 1, 10, 11, 110,...) will return output 0
for the addition TM, the sequence will be added mechanically by the TM and outputs their sum as a new sequence
