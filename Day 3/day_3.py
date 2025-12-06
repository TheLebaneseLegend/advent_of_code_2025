import pandas as pd
import random

text = pd.read_csv("input.txt", names=['joltage'])
text = text['joltage'].tolist()
print(text)

total_joltage = 0

for entry in text:
    joltage = [0, 0]
    num_index = []
    for number in range(0, len(entry)):
        for number2 in range(0, len(entry)):
            if number >= number2:
                continue
            else:
                joltage[1] = entry[number] + entry[number2]
                if int(joltage[1]) > int(joltage[0]):
                    num_index = [number, number2]
                    joltage[0] = joltage[1]
                else:
                    continue
    total_joltage += int(joltage[0])
    print(entry, joltage[0], num_index, entry[num_index[0]], entry[num_index[1]])

print(total_joltage)
