from turtle import forward, left, right, exitonclick
from math import sqrt

def user_input(stena):
    """Vyziada si dlzku strany"""
    return int(input('Zadajte dlzku strany domceka: '))

def domcek(dlzka):
    """postup pre samotny dom"""
    for i in range(4):          
        forward(dlzka)
        left(90)
    left(45)
    forward(sqrt(2) * dlzka)
    for j in range(2):          
        left(90)
        forward(dlzka / (sqrt(2)))
    left(90)
    forward(sqrt(2) * dlzka)

def vytvor_domcek():
    """vlozi input do postupu na dom"""
    stena = user_input(int)
    domcek(stena)
    
vytvor_domcek()

exitonclick()