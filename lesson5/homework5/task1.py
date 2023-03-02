# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def pow_num(a, b):
    if b == 0:
        return 1
    
    if b < 0:
        return pow_num(a, b + 1) * 1 / a
    
    return pow_num(a, b - 1) * a

print(pow_num(int(input()), int(input())))