import os

input = open(os.path.abspath("day-2/input.txt"), 'r')

def createIntcodeArray(arr):
    arr = arr.read().split(',')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr

# part 1
def getValue(arr, p1, p2):
    arr[1] = p1
    arr[2] = p2
    for i in range(0, len(arr), 4):
        if arr[i] == 1:
            arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
        if arr[i] == 2:
            arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
        if arr[i] == 99:
            return arr[0]

# part 2
def getSpecificOutput(arr, output):
    for noun in range(99):
        arr[1] = noun
        for verb in range(99):
            arr[2] = verb
            currentOutput = getValue(arr.copy(), noun, verb)
            if (output == currentOutput): return 100 * noun + verb


output = 19690720
intcode = createIntcodeArray(input)
result = getSpecificOutput(intcode, output)
print(result)