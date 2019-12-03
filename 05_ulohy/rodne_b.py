rodne_cislo =  input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')
cislo = rodne_cislo.split('/')
cislo_spolu = ''.join([cislo[0], cislo[1]])
cislo_int = int(cislo_spolu)        #prevod z str na int

if cislo_int % 11 == 0:     #je cislo delitelne 11 bez zvysku?
    print('True')
else:
    print('False')
    