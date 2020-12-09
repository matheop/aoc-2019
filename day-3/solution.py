import os

input = open(os.path.abspath("day-3/input.txt"), 'r')

def createWires(arr):
    wires = arr.read().split('\n')
    wire_1 = wires[0].split(',')
    wire_2 = wires[1].split(',')
    print(wire_1)
    return wire_1, wire_2

wire_1, wire_2 = createWires(input)