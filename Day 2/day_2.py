import pandas as pd

text = pd.read_csv("input.txt")
text = text.columns.tolist()
print(text)
tally = 0

for i in text:
    low = int(i.split('-')[0])
    high = int(i.split('-')[1])

    for num in range(low, high+1):
        number = str(num)
        len_num = int(len(number) / 2)
        if number[:len_num] == number[len_num:]:
            tally += num

print(tally)
