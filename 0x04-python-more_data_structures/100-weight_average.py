#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        sum_of_prod = 0
        weight_sum = 0
        for tpl in my_list:
            sum_of_prod += (tpl[0] * tpl[1])
            weight_sum += tpl[1]
        average = sum_of_prod/weight_sum
        return average
