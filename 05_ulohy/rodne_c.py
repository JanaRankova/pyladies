rodne_cislo = input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')

rc_pre_datum = list(rodne_cislo)            #rodne cislo do listu

den = '{}{}'.format(rc_pre_datum[4], rc_pre_datum[5])       #den vybratim poloziek z listu a prevedenim na string

rok = int('{}{}'.format(rc_pre_datum[0], rc_pre_datum[1]))      #aby som mohla pouzit podmienku musim previest do int

if rok == 0:
    tisicrocie = '2000{}'.format(rok)                #vynimky pre 2000 a 2001-2009 kedze int nespracuje 0 na zaciatku
elif rok < 10:
    tisicrocie = '200{}'.format(rok)                
elif rok < 21:
    tisicrocie = '20{}'.format(rok)                
else:
    tisicrocie = '19{}'.format(rok)

mesiac = int('{}{}'.format(rc_pre_datum[2], rc_pre_datum[3]))

if mesiac in range(0, 13):                 
    mesiac = mesiac
elif mesiac in range(51, 63):
    mesiac = mesiac - 50           #u zien sa k mesiacu pripocitava 50
    
else:
    print('Rodne cislo nema spravny format.')

print('Datum narodenia je {}.{}.{}.'.format(den, mesiac, tisicrocie))