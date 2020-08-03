nums = [1, 2, 3, 4]

# new_nums = [n for n in nums]
# print(new_nums)

# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)

# # new_nums = map(lambda n: n * n, nums)
# # print(new_nums)

# my_list = [(letter, number) for letter in 'abcd' for number in nums]
# print(my_list)


# sets and dictionaries comprehensions
names = ['Betty', 'Jason', 'Ian', 'Elaine', 'Dory']
heros = ['Superwoman', 'Superman', 'Batman', 'Batwoman', 'Spiderman']

# # the zip object got exausted after changing it to a list
# identities = zip(names, heros)
# print(list(identities))

# if do it from the beginning then do not exausted after changing it to a list
identities = list(zip(names, heros))
print(identities)

for identity in identities:
    print(f'{identity[0]} is actually {identity[1]}!')

my_dict = {names: heros for (names, heros) in zip(names, heros)}
print(my_dict)
