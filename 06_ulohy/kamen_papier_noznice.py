from random import randrange                  

pocet_kol = 0
tahcloveka = ''
tahpocitace = ''

def tah_cloveka():
    """zoberie tah od hraca"""
    odpoved = input('Vyber si: kamen, papier alebo noznice?')
    odpoved_cislo = int
    if odpoved == 'kamen':
        odpoved_cislo = 0
        return odpoved_cislo
    elif odpoved == 'noznice':
        odpoved_cislo = 1
        return odpoved_cislo
    elif odpoved == 'papier':
        odpoved_cislo = 2
        return odpoved_cislo
    else:
        print('Nerozumiem!')
    

def tah_pocitace():
    """generuje nahodny tah PC"""
    nahoda = randrange(3)
    if nahoda == 0:                           
        print('Pocitac si nahodne vybral kamen.')
    elif nahoda == 1:
        print('Pocitac si nahodne vybral noznice.')
    elif nahoda == 2:
        print('Pocitac si nahodne vybral papier.')
    return nahoda
    
def vysledky(tahcloveka, tahpocitace):
    """vyhodnoti vysledky hry"""
    if tahcloveka == tahpocitace:
        print('Plichta.')
    elif ((tahcloveka == 0 and tahpocitace == 1) or (tahcloveka == 1 and tahpocitace == 2) or (tahcloveka == 2 and tahpocitace == 0)):
        print('Vyhral(a) si!')
    else:
        print('Prehral(a) si!')
    return 

while True:
    pocet_kol += 1
    tahcloveka = tah_cloveka()
    if tahcloveka == None:
        break

    tahpocitace = tah_pocitace()
    vysledky(tahcloveka, tahpocitace)
    print('Chces si zahrat este jedno kolo? (ak nie napis "koniec")')
    este_jedno = input()
    if este_jedno == 'koniec':
        break