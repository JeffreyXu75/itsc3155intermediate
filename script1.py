def get_unique_list(list):
    unique_list = []
    for val in list:
        if val not in unique_list:
            unique_list.append(val)
    return unique_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)