# TASK1
def name_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}. Your age is: {age}")
    return name + age

# TASK2
def swap_integers(num1, num2):
    print("X=" + str(num1))
    print("Y=" + str(num2))
    temporary = num1
    num1 = num2
    num2 = temporary
    print("After swap: ")
    print("X=" + str(num1))
    print("Y=" + str(num2))
    return str(num1) + str(num2)

# TASK3
def check_numbers(num1, num2):
    dividable_by6 = (num1 % 6 == 0) or (num2 % 6 == 0)
    dividable_by10 = (num1 % 10 == 0) and (num2 % 10 == 0)

    if dividable_by6 and dividable_by10:
        print("One number is divisible by 6 or both numbers are divisible by 10")
        return True
    else:
        if dividable_by6:
            print("one number is divisible by 6")
        if dividable_by10:
            print("Both numbers are divisible by 10")
        return False

# TASK4
def sum_up(num1, num2):
    if num2 <= num1 or num1 <= 0 or num2 <= 0:
        return 0
    else:
        result = 0
        for i in range(num1, num2 + 1):
            result += i
        return result

# TASK5
def circle_area(r1, r2, r3):
    pi = 3.14
    area1 = pi * (r1 ** 2)
    area2 = pi * (r2 ** 2)
    area3 = pi * (r3 ** 2)
    total_area = area1 + area2 + area3
    return round(total_area, 2)

# TASK6
def check_string(text):
    if text.startswith("a") or text.endswith("a") or text.startswith("A") or text.endswith("A"):
        return True
    else:
        return False

# TASK7
def triangle(rows):
    for i in range(1, rows+1):
        print("*" * i)