import pandas as pd

text = pd.read_csv("input.txt")
text = text.columns.tolist()
print(text)


tally = set()

for i in text:
    low = int(i.split('-')[0])
    high = int(i.split('-')[1])

    # print(low, high)

    for num in range(low, high+1):
        number = str(num)
        len_num = int(len(number))
        # print(low, high, len_num, number)

        for i in range(1, len_num+1):
            # print(len_num, i)
            x = list((number[0+b:i+b] for b in range(0, len(number), i)))
            if len(x) > 1 and len(set(x)) == 1:
                tally.add(num)
                # print(num, i, x, len(x), set(x), len(set(x)), tally)

print(sum(tally))
