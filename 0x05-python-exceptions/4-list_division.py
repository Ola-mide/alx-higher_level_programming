#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = [0] * list_length
    i = 0
    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
            div_list[i] = div
            i += 1
        except TypeError:
            print("wrong type")
            div_list[i] = 0
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            div_list[i] = 0
            i += 1
        except IndexError:
            print("out of range")
            div_list[i] = 0
            i += 1
        finally:
            pass
    return div_list
