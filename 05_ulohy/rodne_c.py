rodne_cislo = input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')

den = int('{}{}'.format(rodne_cislo[4], rodne_cislo[5]))     
rok = int('{}{}'.format(rodne_cislo[0], rodne_cislo[1]))      
mesiac = int('{}{}'.format(rodne_cislo[2], rodne_cislo[3]))
month = bool
if rok == 0:
    tisicrocie = '2000{}'.format(rok)                #vynimky pre 2000 a 2001-2009 kedze int nespracuje 0 na zaciatku
elif rok < 10:
    tisicrocie = '200{}'.format(rok)                
elif rok < 21:
    tisicrocie = '20{}'.format(rok)                
else:
    tisicrocie = '19{}'.format(rok)

if mesiac in range(0, 13):                 
    mesiac = mesiac
elif mesiac in range(51, 63):
    mesiac = mesiac - 50           #u zien sa k mesiacu pripocitava 50
else:
    month = False

if (den in range(1, 32) and month != False):
    print('Datum narodenia je {}.{}.{}.'.format(den, mesiac, tisicrocie))
else:
    print('False')
