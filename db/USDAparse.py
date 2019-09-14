import re
from operator import itemgetter
import sqlite3

connection = sqlite3.connect("test.db")

crsr = connection.cursor()

sql_command = """CREATE TABLE lang (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100)
);"""

crsr.execute(sql_command)

with open('./LANGDESC.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # m = re.match('~[A-Z][0-9]+~\^~[A-Z\s()0-9.-/,><]+~', line)
        m = re.findall('[A-Z\s()0-9.\'\-/,><]+', line)
        assert len(m) == 2
        id, name = m
        crsr.execute("INSERT INTO lang VALUES (?, ?)", (id, name))
    connection.commit()

sql_command = """CREATE TABLE food (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100)
);"""

crsr.execute(sql_command)

with open('./FOOD_DES.txt', encoding='iso-8859-1') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # m = re.match('~[A-Z][0-9]+~\^~[A-Z\s()0-9.-/,><]+~', line)
        m = re.findall('[a-zA-Z\s()0-9.\'\-/,><]+', line)
        id = m[0]
        name = m[2]
        crsr.execute("INSERT INTO food VALUES (?, ?)", (id, name))
    connection.commit()

sql_command = """CREATE TABLE link (
    lang_id VARCHAR(10),
    food_id VARCHAR(10),
    FOREIGN KEY(lang_id) REFERENCES lang(id),
    FOREIGN KEY(food_id) REFERENCES food(id)
);"""

crsr.execute(sql_command)

with open('./LANGUAL.txt', encoding='ascii') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # m = re.match('~[A-Z][0-9]+~\^~[A-Z\s()0-9.-/,><]+~', line)
        m = re.findall('[A-Z\s()0-9.\'\-/,><]+', line)
        assert len(m) == 2
        food_id, lang_id = m
        crsr.execute("INSERT INTO link VALUES (?, ?)", (lang_id, food_id))
    connection.commit()
    connection.close()
