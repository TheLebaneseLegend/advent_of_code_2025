import pandas as pd
import math

moves = pd.read_csv('input.txt', names=['moves'])
moves = moves['moves'].tolist()
# print(moves)

current_number = 50
ending_nums = []

for move in moves:
    if move[0] == 'R':
        current_number += (int(move[1:]) % 100)
        if current_number > 99:
            current_number -= 100
            if current_number != 0 and int(math.floor((int(move[1:]) / 100))) != 0:
                ending_nums += [0] * math.floor((int(move[1:]) / 100))


    if move[0] == 'L':
        current_number -= (int(move[1:]) % 100)
        if current_number < 0:
            current_number += 100
            if current_number != 0 and int(math.floor((int(move[1:]) / 100))) != 0:
                ending_nums += [0] * math.floor((int(move[1:]) / 100))

    ending_nums.append(current_number)
    print(move, current_number, math.floor((int(move[1:]) / 100)))

code = ending_nums.count(0)

print(code)

