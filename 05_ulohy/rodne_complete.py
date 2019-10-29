rodne_cislo =  input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')

cislo_list = list(rodne_cislo)     

#poduloha a
lomitko = cislo_list[6]        
if cislo_list[6] == '/':
    lomitko = True

sest = cislo_list[0:6]          
for num in sest:
    if num.isdigit():
        sest = True

styri = cislo_list[7:]      
for num in styri:
    if num.isdigit():
        styri = True

rodne_cislo_format = bool
if (lomitko == True and sest == True and styri == True and len(cislo_list) == 11):
    rodne_cislo_format = True        

#poduloha b
cislo = rodne_cislo.split('/')
cislo_spolu = ''.join([cislo[0], cislo[1]])

print(cislo_spolu)
cislo_int = int(cislo_spolu)        

rodne_cislo_delitelne = bool
if cislo_int % 11 == 0:
    rodne_cislo_delitelne = True     
else:
    print('False')

#poduloha c
rc_pre_datum = list(rodne_cislo)           

den = '{}{}'.format(rc_pre_datum[4], rc_pre_datum[5])      

rok = int('{}{}'.format(rc_pre_datum[0], rc_pre_datum[1]))     

if rok == 0:
    tisicrocie = '2000{}'.format(rok)                
elif rok < 10:
    tisicrocie = '200{}'.format(rok)                
elif rok < 21:
    tisicrocie = '20{}'.format(rok)                
else:
    tisicrocie = '19{}'.format(rok)

mesiac = int('{}{}'.format(rc_pre_datum[2], rc_pre_datum[3]))

rodne_cislo_datum = bool
if mesiac in range(0, 13):                 
    mesiac = mesiac
    rodne_cislo_datum = True
elif mesiac in range(51, 63):
    mesiac = mesiac - 50           
    rodne_cislo_datum = True
else:
    print('Rodne cislo nema spravny format.')


#poduloha d

sex = cislo_list[2]            

rodne_cislo_pohlavie = ''
if sex == '0' or sex == '1':               
    rodne_cislo_pohlavie = 'muz'
elif sex == '5' or sex == '6':
    rodne_cislo_pohlavie = 'zena'
else:
    print('Rodne cislo nie je zadane v spravnom formate.')


#zhrnutie vsetkych poduloh do podmienky 
if (rodne_cislo_format == True and rodne_cislo_delitelne == True and rodne_cislo_datum == True):
    print('Zadane rodne cislo ', rodne_cislo, 'je v spravnom formate. Pouzivatel je {}, narodena/y {}.{}.{}.'.format(rodne_cislo_pohlavie, den, mesiac, tisicrocie))
else:
    print('Zadane rodne cislo nie je v spravnom formate.')

