from turtle import forward, left, right, exitonclick
from math import sqrt

def user_input(side):
    """Ask for a side lenght."""
    return int(input('Zadajte dlzku strany housea: '))

def house(dlzka):
    """House blueprint :)"""
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

def build_house():
    """Puts user_input into blueprint."""
    side = user_input(int)
    house(side)
    
build_house()

exitonclick()