# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

def sum_uneven():
    num = 0
    sum = 0
    while num <= 10:
        if num % 2 != 0:
            sum += num
        num += 1    
    return sum
print(f"The sum of the odd numbers from 1 to 10 is {sum_uneven()}")