# -*- coding: utf-8 -*-
import random

from Obj import Animal

Animal.delete(all=True)
animals = []

a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
a = Animal.add('animal_1', 'm', 0, 50, 50)
print(Animal.count())

f = (0, 0)
for line in range(25):
    animals = Animal.all()
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
        
        animal.x += del_x
        animal.y += del_y
        animal.save()
    print 
    Animal().all()
