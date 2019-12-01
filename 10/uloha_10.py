import time
import random

class Priest:
    HEALTH_POOL = 50
    DAMAGE = 10
    def __init__(self, name):
        self.name = name
        self.dmg = self.DAMAGE
        self.health = self.HEALTH_POOL
    
    def heal(self):
        #recovers portion of health pool, cast time made through time.sleep and print
        print('{} begins to cast heal.'.format(self.name))
        if self.is_alive() == False:
            print('You are dead. You can only heal living targets.')
        elif self.is_alive():
            for casttime in range(3):
                time.sleep(1)
                self.health += 5
                print('{} has healed himself for 5 hp and has {} health now.'.format(self.name, self.health))
        else:
            print('You are already at full health!')

    def basic_attack(self, enemy):
        #dealing dmg to enemies health pool
        if enemy.health > 0:
            damage = self.dmg
            print('{} deals {} points of damage to {}.'.format(self.name, damage, enemy.name))
            if damage > enemy.health:
                enemy.health = enemy.health - damage
                enemy.health = 0
                print('{} recieves damage. His health is lowered to {}'.format(enemy.name, enemy.health))
            else:
                enemy.health = enemy.health - damage
                print('{} recieves damage. His health is lowered to {}'.format(enemy.name, enemy.health))
            print('')
        else:
            print('Your oponent is already dead, you cannot really make him any more dead.')
    
    def is_alive(self):
        #checks whether target is still alive
        return self.health > 0

class ShadowPriest(Priest):
    #heals same but with shadow and different amount of health, boosted damage
    DAMAGE = Priest.DAMAGE + 2
    def heal(self):
        #same as priest heal but also makes damage to caster
        super().heal()
        time.sleep(1)
        self.health -= random.randrange(2, 6)
        print('As you heal yourself with shadow forces some of your health is drawn back to void realm.')

    def basic_attack(self, enemy):
        #self is dealing dmg to enemy, basic dmg + random number(10)
        if enemy.health > 0:
            damage = self.dmg + random.randrange(0,8)
            print('{} deals {} points of shadow damage to {}.'.format(self.name, damage, enemy.name))
            if damage > enemy.health:
                enemy.health = enemy.health - damage
                enemy.health = 0
                print('{} recieves damage. His health is lowered to {}'.format(enemy.name, enemy.health))
            else:
                enemy.health = enemy.health - damage
                print('{} recieves damage. His health is lowered to {}'.format(enemy.name, enemy.health))
            print('')
        else:
            print('Your oponent is already dead, you cannot really make him any more dead.')

class HolyPriest(Priest):
    #has heal with no casttime, can also heal others, if target is dead - ressurects
    def heal(self, target):
        #recovers portion of health pool
        print('{} begins to cast greater heal.'.format(self.name))
        if target.is_alive() == False:
            target.health += target.HEALTH_POOL     #returns full health
            print('{} has been ressurected!'.format(target.name))
        elif target.health < target.HEALTH_POOL:
            target.health += 15
            print('{} has been healed for 15 hp and has {} health now.'.format(target.name, target.health))
        else:
            print('You are already at full health!')
