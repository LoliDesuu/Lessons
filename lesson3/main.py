my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
elem = 0

while elem < len(my_list)-1:
    elem += 1
    if my_list[elem] == 0:
        continue
    elif my_list[elem] > 0:
        print(my_list[elem])
        continue
    else:
        break