def get_combined_dict(dicta, dictb):
    newdict={}
    for value in dicta:
        if value in dictb:
            newdict[value] = dicta[value] + dictb[value]
    return newdict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)