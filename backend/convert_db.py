import sqlite3
import json
import re

conn = sqlite3.connect("dataset.sqlite")
cursor = conn.cursor()
fixture = [] 

cursor.execute("""
    select * from actors
""")
fixture = []
for item in cursor.fetchall():
    tmp = {}
    tmp['model'] = "cinema.actor"
    tmp['pk'] = item[0]
    tmp['fields'] = {
        "name": item[1] if item[1] != "N/A" else ""
    }
    fixture.append(tmp)


cursor.execute("""
    select * from writers;
""")
for item in cursor.fetchall():
    tmp = {}
    tmp['model'] = "cinema.writer"
    tmp['pk'] = item[0]
    tmp['fields'] = {
        "name": item[1] if item[1] != "N/A" else ""
    }
    fixture.append(tmp)

cursor.execute("""
    select * from movie_actors;
""")
movie_actors_list = cursor.fetchall()



cursor.execute("""
    select * from movies;
""")
for item in cursor.fetchall():
    tmp = {}
    tmp['model'] = "cinema.movie"
    tmp['pk'] = item[0]
    tmp['fields'] = {
        "title": item[4],
        "imdb_rating": item[7] if item[7] != "N/A" else 0,
        "genre": item[1],
        "description": item[5] if item[5] != "N/A" else "",
        "director": item[2] if item[2] != "N/A" else "",
        "writers": re.findall('0b[a-zA-Z0-9]{7,40}', item[3]) if item[3] else re.findall('0b[a-zA-Z0-9]{7,40}', item[8]),
        "actors": [int(x[1]) for x in movie_actors_list if x[0]==item[0]]
    }
    fixture.append(tmp)


with open('dump.json', 'w') as outfile:
    json.dump(fixture, outfile)