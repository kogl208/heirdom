# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect('heirdom.db')
c = con.cursor()
c.execute('''
    create table if not exists animals
    (id integer primary key autoincrement,
    name text,
    sex text,
    age real,
    x integer,
    y integer)
    ''')
c.close()
con.close()
