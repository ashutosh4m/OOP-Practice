from Enemy import *
from Zombie import *
from Ogre import *
from Weapon import *
from Hero import *
#zombie = Zombie(10,1)

#ogre = Ogre(20,3)

#print(zombie.talk())
#print(zombie.spread_disease())
#print(zombie.get_type_of_enemy())
#zombie.spread_disease()

#print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do {zombie.attack_damage} damage')
#print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do {ogre.attack_damage} damage')

def battle(e1:Enemy,e2:Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('--------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}:{e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}:{e2.health_points} HP left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('----------------')

    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')


def Hero_battle(hero:Hero,enemy:Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('--------------')
        enemy.special_attack()
        print(f'Hero:{hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}:{enemy.health_points} HP left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('----------------')

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')





zombie = Zombie(10,1)
ogre = Ogre(15,2)
hero = Hero(10,1)
weapon = Weapon('Sword',5)
hero.weapon = weapon
hero.equip_weapon()

Hero_battle(hero,ogre)
