# -*- coding: utf-8 -*-
import random

from Obj import Animal

print("anim")
Animal.delete(-1)
animals = []

Animal.add('animal_1', 'm', 0, 50, 50)
Animal('animal_1', 'f', 0, 50, 50)

f = (0, 0)
for line in range(25):
    animals = Animal().all(True)
    for animal in animals:
        if animal.sex == 'f': 
            f = (animal.x, animal.y)
        if animal.sex == 'm':
            x_del_x = animal.x - f[0]
            if 0 < x_del_x:
                del_x = -x_del_x if 0 <= x_del_x <= 2 else -2
            else:
                del_x = x_del_x if 0 <= x_del_x <= 2 else 2
                
            y_del_y = animal.y - f[1]
            if 0 < x_del_x:
                del_y = -y_del_y if 0 <= y_del_y <= 2 else -2
            else:
                del_y = y_del_y if 0 <= y_del_y <= 2 else 2
        else:
            del_x = random.randint(-2, 2)
            del_y = random.randint(-2, 2)
        animal.age += 0.5
##        if animal.age >= 5:
##            animal.delete()
            
##        if animal.age == 3:
##            Animal().add(animal.name, random.choice('mf'), 0, animal.x, animal.y)
        
        animal.x += del_x
        animal.y += del_y
        animal.save()
    print 
    Animal().all()