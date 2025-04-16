from itertools import chain

list_1 = input()
list_2 = input()
list_3 = input()

all_list = set(chain(list_1.split(", "), list_2.split(", "), list_3.split(", ")))

for index, value in enumerate(sorted(list(all_list)), 1):
    print(f"{index}. {value}")