__author__ = 'jc437345'

from random import randint

num_of_picks = int(input("how many quick picks?: "))

num = 0
for i in range(0, num_of_picks):
    pick_of_6_num = []
    num = randint(1, 45)
    for j in range(0, 6):
       while num in pick_of_6_num:
                num = randint(1, 45)
       pick_of_6_num.append(num)

    print(sorted(pick_of_6_num))
    pick_of_6_num = []
