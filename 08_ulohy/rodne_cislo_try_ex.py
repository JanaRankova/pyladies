while True:
    rodne_cislo =  input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')
    cislo_list = list(rodne_cislo)
    cislo_spolu = int(''.join([rodne_cislo[0:6], rodne_cislo[7:]]))   
    try:    
        prva_cast = int(rodne_cislo[0:6])
        druha_cast = int(rodne_cislo[7:11])
        len(rodne_cislo) == 11
        assert rodne_cislo[6] == '/'
        assert cislo_spolu % 11 == 0  
    except ValueError:
        print('Rodne cislo je zadane v zlom formate.')
        continue
    except AssertionError:
        print('Rodne cislo je zadane v zlom formate.')
        continue
    else:
        break

def datum(rodne_cislo):
    """Podla cisla vyhodnoti datum narodenia. Vrati T/F a datum."""  
    den = int(rodne_cislo[4:6])     
    rok = int(rodne_cislo[0:2])    
    mesiac = int(rodne_cislo[2:4])
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
    else:
        mesiac = mesiac - 50           
    return ('{}. {}. {}'.format(den, mesiac, tisicrocie))

def pohlavie(rodne_cislo):
    """Z cisla zisti pohlavie a vrati ho.""" 
    if int(rodne_cislo[2:4]) < 13:               
        return 'muz'
    else:
        return 'zena'

print('Zadane rodne cislo ', rodne_cislo, 'je v spravnom formate. Pouzivatel je {}, narodena/y {}.'.format(pohlavie(rodne_cislo), datum(rodne_cislo)))