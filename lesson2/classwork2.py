# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

# n = int(input())
# sum = 1

# while n > 0:
#     sum = n * sum
#     n = n - 1

# print(sum)


 # Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# 1  2  3  4  5  6  7   8   9  10  11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

# num = int(input())
# count = 2
# f_1 = 0
# f_2 = 1

# while f_2 <= num:
#     if num == f_2:
#         print(count)
#         break
#     f_1, f_2 = f_2, f_1 + f_2
#     count = count + 1 # count += 1
# else:
#     print(-1)



# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно
# превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50


# import os
# os.system('cls') # clear

# n = int(input())
# maximum_row = current_row = 0
# for i in range(n):
#     temp = int(input())
#     if temp > 0:
#         current_row += 1
#     else:
#         if current_row > maximum_row:
#             maximum_row = current_row
#     current_row = 0
# print(maximum_row)


# Иван Васильевич пришел на рынок и решил купить
# два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# import os
# os.system('cls') # clear

# n = int(input())
# max, min = int(input())

# for _ in range(total - 1): # _ безымянная переменная
#     count = int(input())
#     if count > max:
#         max = count
#     if count < min:
#         min = count
# print(min, max)