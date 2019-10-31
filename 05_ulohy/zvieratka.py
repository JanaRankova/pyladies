pets = ['had', 'andulka', 'pes' , 'kocka', 'kralik']

pet_split =[]

for pet in pets:
    pet_split.append(pet[1])
pet_dict = dict(zip(pet_split, pets))

presorted_pets = sorted(pet_dict.items())
sorted_pets = []
for values in presorted_pets:
    sorted_pets.append(values[1])
print(sorted_pets)
