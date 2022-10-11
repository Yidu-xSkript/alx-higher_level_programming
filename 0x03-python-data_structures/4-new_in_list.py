#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    for i in range(0, len(my_list)):
        newlist.append(my_list[i])
    if idx < 0 or idx >= len(newlist):
        return newlist
    newlist[idx-1] = element
    return newlist
