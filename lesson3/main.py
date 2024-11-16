my_list =  [42, 69, 322, 13, 0, 99, 9, 8, 7, 5]
number = 0

while my_list[number] > -1  :
    if my_list[number] == 0:
        my_list.remove(0)
    if (my_list[number]) >= len(my_list) :
        print(my_list[number])
        number += 1
        continue
    else:
        break