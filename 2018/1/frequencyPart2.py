with open('input.txt') as input:
    freqChanges = input.read().splitlines()

# i = 0
# while i < len(freqChanges):
#     freqChanges[i] = int(freqChanges[i])
#     i += 1

freqChanges = list(map(int, freqChanges))

def step(arr):
    i = 0
    sum = 0
    frequencies = []
    done = False

    while not done:
        sum += arr[i]
        i += 1
        frequencies.append(sum)
        print(len(frequencies))

        # if we find it, return it
        if frequencies[-1] in frequencies[0:-1]:
            return frequencies[-1]

        # if we get to the end of the fchange list, restart from the beginning
        if i >= len(arr):
            i = 0



print(freqChanges)
print(step(freqChanges))
