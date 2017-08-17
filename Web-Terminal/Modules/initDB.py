#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Init database
Create tables
Insert data
Query data
"""

from sqlalchemy import *
from sqlalchemy.orm import *


#define egine
engine = create_engine('sqlite:///../DB/raspberrypirobot.db')
#bind metadata
metadata = MetaData(engine)

#create tables, init database
pilot = Table('pilot', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String(255)),
    Column('fullname', String(255)),
    Column('email', String(255)),
    Column('password', String(255))
)

air = Table('air', metadata, 
    Column('id', Integer, primary_key = True),
    Column('date', DateTime, nullable=False),
    Column('temperature', Float),
    Column('humidity', Float),
    Column('infaredetector', Boolean)
)

joystick = Table('joystick', metadata,
    Column('id', Integer, primary_key = True),
    Column('gpio', Integer),
    Column('function', String(255)),
    Column('device', String(255))
)

#create tables, if tables exist, pass
metadata.create_all(engine)
#get db connected
conn = engine.connect()


def insert_data(table, data):
    i = table.insert()
    r1 = conn.execute(i, data)
    # print r1.inserted_primary_key
#func usage
# data = dict(name='jailman', fullname='jailman lobo', email='jailman@sina.com', password='damnyou')
# insert_data(pilot, data)



def query(flag, table, *columns):
    if flag:
        s1 = select([table])
        r1 = conn.execute(s1)
        return r1.fetchall()
    else:
        qry = ''
        for i in columns:
            qry = qry + 'table.c.' + i + ','
        qry = 'select([' + qry + '])'
        s2 = eval(qry)
        r2 = conn.execute(s2)
        return r2.fetchall()

#func usage
# print query(True, pilot, "name", "fullname")