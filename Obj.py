# -*- coding: utf-8 -*-
import sqlite3
from copy import copy


class DeleteException(Exception): pass


CON = sqlite3.connect('heirdom.db')
CUR = CON.cursor()


def add_obj(self, name, sex, age, x, y):
    self.name = name
    self.sex = sex if sex in ('m', 'f') else 'm'
    self.age = age if age > 0 else 0
    self.x = x
    self.y = y
    CUR.execute('''
    insert into animals (name, sex, age, x, y) 
    values (?, ?, ?, ?, ?)
    ''' , (self.name, self.sex, self.age, self.x, self.y))
    CON.commit()
    self.__id = CUR.lastrowid
    return self


def add_for_init(*args):
    add_obj(*args)


class Animal(object):
    __init__ = add_for_init
    
    def __repr__(self):
        return '%s_%s[%s] (%s,%s)' % (self.name, self.sex, self.age, 
            self.x, self.y)
    
    add = classmethod(add_obj)
##    add = __init__
    
    def create(self, id, name, sex, age, x, y):
        self.__id = id
        self.sex = sex
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        return self
        
    def save(self):
        CUR.execute('''
        update animals 
        set name=?, sex=?, age=?, x=?, y=?
        where id=?
        ''', (self.name, self.sex, self.age, self.x, self.y, self.__id))
        CON.commit()
    
    @classmethod
    def delete(self, id=0, all=False):
        try:
            if all:
                raise DeleteException()
            id = id if id else self.__id
            CUR.execute('delete from animals where id=?', (id,))
        except DeleteException:
            CUR.execute('delete from animals')
        CON.commit()
    
    @classmethod
    def count(self):
##        CUR.execute('select * from animals')
##        count = 0
##        for row in CUR:
##            count += 1
##        return count
        CUR.execute('select count(*) from animals')
        for row in CUR:
            return row
        
    @classmethod
    def all(self, rtrn=False):
        CUR.execute('select * from animals')
        if rtrn:
            all = []
            for row in CUR:
                all.append(self.create(*row))
            return all
        else:
            for row in CUR:
                print(self.create(*row))
            if self.count() == 0:
                print('No objects "Animal"')
