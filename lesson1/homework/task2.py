# 2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# in
# 6
# out
# 1 4 1

# in
# 24
# out
# 4 16 4

# in
# 60
# out
# 10 40 10

s = int(input("Введите количество журавликов: "))

if s % 2 or (s // 2) % 2:
    print("введите число кратное четырем")
else:
    a = s // 6
    print (f"{a} {4*a} {a}")
