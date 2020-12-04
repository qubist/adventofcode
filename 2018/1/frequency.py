with open('input.txt') as input:
    freqChanges = input.read().splitlines()

# i = 0
# while i < len(freqChanges):
#     freqChanges[i] = int(freqChanges[i])
#     i += 1

freqChanges = list(map(int, freqChanges))

currentFrequency = 0

def sum(arr):
    i = 0
    output = 0
    while i < len(arr):
        output += arr[i]
        i += 1
    return output

testArr = [1,2,8,12]
print(f"should be 23: {sum(testArr)}")

print(freqChanges)
print(sum(freqChanges))
