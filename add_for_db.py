# -*- coding: utf-8 -*-
import sqlite3

from Obj import Animal


def add_for_objects(name, age, pos_x, pos_y):
    conn = sqlite3.connect('heirdom.db')
    c = conn.cursor()
    c.execute("INSERT INTO animal (name, age, pos_x, pos_y)\
              VALUES (?, ?, ?, ?)", (name, age, pos_x, pos_y)) 
    conn.commit()
    conn.close()


def print_all_objects():
    conn = sqlite3.connect('heirdom.db')
    c = conn.cursor()
    c.execute("SELECT * FROM animal")
    for row in c.fetchall():
        print('%s: %s(%s)[%s,%s]' % (row[0], row[1], row[2], row[3], row[4]))
    conn.close()


def remove_old_from_objects():
    conn = sqlite3.connect('heirdom.db')
    c = conn.cursor()
    c.execute("DELETE FROM animal WHERE age>10")
    conn.commit()
    conn.close()


def add_for_animal(name, age, pos_x, pos_y):
    animal = Animal(name, age, pos_x, pos_y)
    conn = sqlite3.connect('heirdom.db')
    c = conn.cursor()
    c.execute("INSERT INTO animal (animal) VALUES (?)", animal) 
    conn.commit()
    conn.close()
