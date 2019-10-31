rodne_cislo =  input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')
cislo_list = list(rodne_cislo)     

#poduloha a
if (rodne_cislo[6] == '/' and rodne_cislo[0:6].isdigit() and rodne_cislo[7:11].isdigit() and len(rodne_cislo) == 11):
    rc_format = True
else:
    rc_format = False    

#poduloha b
cislo = rodne_cislo.split('/')
cislo_spolu = ''.join([cislo[0], cislo[1]])
cislo_int = int(cislo_spolu)      
rodne_cislo_delitelne = bool

if cislo_int % 11 == 0:    
    rodne_cislo_delitelne = True
else:
    rodne_cislo_delitelne = False

#poduloha c          
den = int('{}{}'.format(rodne_cislo[4], rodne_cislo[5]))     
rok = int('{}{}'.format(rodne_cislo[0], rodne_cislo[1]))      
mesiac = int('{}{}'.format(rodne_cislo[2], rodne_cislo[3]))
if rok == 0:
    tisicrocie = '2000{}'.format(rok)                #vynimky pre 2000 a 2001-2009 kedze int nespracuje 0 na zaciatku
elif rok < 10:
    tisicrocie = '200{}'.format(rok)                
elif rok < 21:
    tisicrocie = '20{}'.format(rok)                
else:
    tisicrocie = '19{}'.format(rok)

rodne_cislo_datum = bool
if mesiac in range(0, 13):                 
    mesiac = mesiac
elif mesiac in range(51, 63):
    mesiac = mesiac - 50           
else:
    rodne_cislo_datum = False

#poduloha d      
rodne_cislo_pohlavie = ''
if cislo_list[2] == '0' or cislo_list[2] == '1':               
    rodne_cislo_pohlavie = 'muz'
elif cislo_list[2] == '5' or cislo_list[2] == '6':
    rodne_cislo_pohlavie = 'zena'
else:
    print('Rodne cislo nie je zadane v spravnom formate.')

#zhrnutie vsetkych poduloh do podmienky 
if (rc_format == True and rodne_cislo_delitelne == True and rodne_cislo_datum !=  False):
    print('Zadane rodne cislo ', rodne_cislo, 'je v spravnom formate. Pouzivatel je {}, narodena/y {}.{}.{}.'.format(rodne_cislo_pohlavie, den, mesiac, tisicrocie))
else:
    print('Zadane rodne cislo nie je v spravnom formate.')
