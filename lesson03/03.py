import random

my_student_id = 83

for _ in range(10000):
    result = random.randint(0, 100)

    try:
        print(my_student_id / result)
    except ZeroDivisionError as e:
        print(e)