rodne_cislo =  input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')
cislo_list = list(rodne_cislo)     

def forma(rodne_cislo):
    """Ci je rodne cislo zadane v spravnej forme. Vracia T/F."""
    if (rodne_cislo[6] == '/' and rodne_cislo[0:6].isdigit() and rodne_cislo[7:11].isdigit() and len(rodne_cislo) == 11):
        return True
    else:
        return False 

def delitelnost(rodne_cislo):
    """Ci je cislo delitelne 11 bez zvysku. Vracia T/F."""
    cislo = rodne_cislo.split('/')
    cislo_spolu = ''.join([cislo[0], cislo[1]])
    cislo_int = int(cislo_spolu)      
    if cislo_int % 11 == 0:    
        return True
    else:
        return False

def datum(rodne_cislo):
    """Podla cisla vyhodnoti datum narodenia. Vrati T/F a datum."""  
    den = int('{}{}'.format(rodne_cislo[4], rodne_cislo[5]))     
    rok = int('{}{}'.format(rodne_cislo[0], rodne_cislo[1]))      
    mesiac = int('{}{}'.format(rodne_cislo[2], rodne_cislo[3]))
    if rok == 0:
        tisicrocie = '2000{}'.format(rok)              
    elif rok < 10:
        tisicrocie = '200{}'.format(rok)                
    elif rok < 21:
        tisicrocie = '20{}'.format(rok)                
    else:
        tisicrocie = '19{}'.format(rok)

    if mesiac in range(0, 13):                 
        mesiac = mesiac
    elif mesiac in range(51, 63):
        mesiac = mesiac - 50           
    else:
        return False
    return ('{}. {}. {}'.format(den, mesiac, tisicrocie))

def pohlavie(cislo_list):  
    if cislo_list[2] == '0' or cislo_list[2] == '1':               
        return 'muz'
    elif cislo_list[2] == '5' or cislo_list[2] == '6':
        return 'zena'
    else:
        return False

if (forma(rodne_cislo) == True and delitelnost(rodne_cislo) == True and datum(rodne_cislo) != False and pohlavie(cislo_list) != False):
    print('Zadane rodne cislo ', rodne_cislo, 'je v spravnom formate. Pouzivatel je {}, narodena/y {}.'.format(pohlavie(cislo_list), datum(rodne_cislo)))
else:
    print('Zadane rodne cislo nie je v spravnom formate.')
