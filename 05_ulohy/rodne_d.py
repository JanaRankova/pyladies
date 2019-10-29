rodne_cislo = input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')

rc_list = []                    #bud naplnime list cyklom alebo cez funkciu list()
for char in rodne_cislo:
    rc_list.append(char)

sex = rc_list[2]            

if sex == '0' or sex == '1':                #[2],[3] = mesiac u zien + 50
    print('muz')
elif sex == '5' or sex == '6':
    print('zena')
else:
    print('Rodne cislo nie je zadane v spravnom formate.')