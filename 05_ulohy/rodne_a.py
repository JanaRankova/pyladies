rodne_cislo =  input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')

cislo_list = []         #vytvorenie prazdneho listu pomocou cyklu alebo list()

for char in rodne_cislo:
    cislo_list.append(char)
print(cislo_list)


lomitko = cislo_list[6]         #ci je pritomne lomitko v spravnej pozicii

if cislo_list[6] == '/':
    lomitko = True

sest = cislo_list[0:6]          #ci prvych 6 je cislica

for num in sest:
    if num.isdigit():
        sest = True

styri = cislo_list[7:]      #ci poslene 4 su cisla

for num in styri:
    if num.isdigit():
        styri = True

if (lomitko == True and sest == True and styri == True and len(cislo_list) == 11):        #ak su splnene vsetky podmienky, cislo je zadane spravne a ci ma spravnu dlzku
    print('True')