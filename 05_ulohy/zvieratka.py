pets = ['had', 'andulka', 'pes' , 'kocka', 'kralik']

pet_split = []

for pet in pets:
    pet_list = pet[1].split()
    pet_split.append(pet_list)
    pet_list.append(pet)


print(sorted(pet_split))
pet_split.sort()

pet_sorted = []

for pet2 in pet_split:
    pet_list2 = pet2[1]
    pet_sorted.append(pet_list2)

print(pet_sorted)
