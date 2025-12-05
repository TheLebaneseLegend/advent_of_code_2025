import pandas as pd

moves = pd.read_csv('input.txt', names=['moves'])
moves = moves['moves'].tolist()

total = 50
count = 0
for i in moves:
    if i[0] == "R":
        i_new = int(i.replace("R", ""))
        total = total + i_new
        count = count + int(total / 100)
        total = total % 100
    else:
        i_new = int(i.replace("L", ""))
        old = total
        total = total - i_new
        if total == 0:
            count = count + 1
        if total < 0:
            if old != 0:
                count = count + 1
            count = count + int((i_new - old) / 100)
            total = total % 100

print("total_end=", total)
print("count_end=", count)
