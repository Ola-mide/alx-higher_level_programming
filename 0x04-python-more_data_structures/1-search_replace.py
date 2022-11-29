#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if search in my_list:
        for num in my_list:
            if search == num:
                idx = new_list.index(search)
                new_list[idx] = replace
    return new_list
