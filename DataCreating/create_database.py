import csv
import random
from collections import defaultdict
from random import choices
import pandas as pd
import pymysql


def generate_director():
    director = {}
    index = 0
    with open("movies.csv",encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        for line in reader:
            if line[3] not in director:
                if line[3] == "director":
                    continue
                director[line[3]] = index 
                index += 1
    return director



## movies  
def generate_movies_sql():
    director = generate_director()
    index = 0
    with open("movies.sql","w") as f: 
        with open("movies.csv",encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.reader(csvfile,delimiter=",")
            for line in reader:
                if index == 0:
                    pass
                else:
                    f.write("INSERT INTO movies (title,company,budget,genre,gross,rating,release_time,runtime,year,director_id) VALUES (\"{}\",\"{}\",{},\"{}\",{},\"{}\",\"{}\",{},\"{}\",{});\n".format(" ".join(line[6].split("\""))," ".join(line[1].split("\"")),line[0],line[4],line[5]," ".join(line[7].split("\"")),line[8],line[9],line[14],director[line[3]]))
                index += 1


## director
def generate_director_sql():
    index = 0
    genders = ["male","female"]
    birth ="19{}-{}-{}"
    with open("director.sql","w") as f: 
        for name,id_ in director.items():
            f.write("INSERT INTO director (id,name,gender,birth) VALUES ({},\"{}\",\"{}\",\"{}\");\n".format(id_,name,random.choice(genders),birth.format(random.randint(20,99),random.randint(1,12),random.randint(1,29))))



## actors
def generate_movie_sql():
    index = 0
    birth ="19{}-{}-{}"
    with open("actor.sql","w") as f:
        with open("actor.csv",encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.reader(csvfile,delimiter=",")
            for line in reader:
                if line[2] == "Name":
                    continue
                f.write("INSERT INTO actor (id,name,gender,birth) VALUES ({},\"{}\",\"{}\",\"{}\");\n".format(index," ".join(line[2].split("\"")),line[3],birth.format(random.randint(20,99),random.randint(1,12),random.randint(1,29))))
                index += 1



import random
from collections import defaultdict


def generate_rala():
    relation = defaultdict(set)
    
    movies = list(range(2,6824))
    actors = list(range(1,419))

    for movie in movies:
        for j in range(random.randint(2,5)):
            relation[movie].add(random.choice(actors))

    return relation




def generate_m_a_rela(relation):
    with open("rel_movie_actor.sql","w") as f: 
        for movie,actors in relation.items():
            for actor in actors:
                f.write("INSERT INTO rel_movie_actor (movie_id,actor_id) VALUES ({},{})\n".format(movie,actor))

relation = generate_rala()
generate_m_a_rela(relation)





# user
def generate_user():
    index = 0
    genders = ["male", "female"]
    birth = "19{}-{}-{}"
    account = "abcdefghijklmnopqrstuvwxyz123456789"
    a1=['Steven ','Chris ','Jackie ','Jay ','James ','Suki ','Kartik ','Johnson ','Michael ','Kevin ']
    a2=['','','','Bosh ','Lame ','Rick ','Noah ']
    a3=['Curry','Paul','Chen','Chou','Harden','George','Jordon','Durant','Nash']
    with open("user.sql", "w") as f:
        with open("ratings.csv", encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for line in reader:
                if index == 0:
                    pass
                if index == 1000:
                    break
                else:
                    f.write(
                        "INSERT INTO user (name,gender,password,birth) VALUES (\"{}\",\"{}\",\"{}\",\"{}\");\n".format(
                            random.choice(a1) + random.choice(a2) + random.choice(a3), random.choice(genders), "123456",  birth.format(random.randint(20,99),random.randint(1, 12),random.randint(1,29))))
                index += 1


    visited = set()
    with open("update_user.sql", "w") as f:
        while index > 0:
            email = "".join(choices(account,k = 5)) + "@pitt.edu"
            if email in visited:
                continue
            else:
                f.write("UPDATE user SET account = \"{}\", district = {} WHERE id = {};\n".format(email, random.randint(0,10),index))
                visited.add(email)
                index -= 1



## theater
def generator_theater():
    theater_names = set()
    first_name = ["Colorful","Beautiful","Amazing","Splendid","Happy","Fantasy","Gold","Blue"]
    last_name = ["City","House","Theater","Box","Movie","Memory","Cinema","Studio","Hall","Room"]
    for first in first_name:
        for last in last_name:
            theater_names.add(first + " " + last)

    with open("theater.sql","w") as f:
        for district in range(0,10):
            for i in range(random.randint(5,8)):
                f.write("INSERT INTO theater (name, district,operator) VALUES (\"{}\",{},{});\n".format(theater_names.pop(),district,random.randint(1,3)))



#mov_id  2-6821
# 10 movies 8chang


## update_on_show
def generate_onshow():
    schedule = "2017-08-15 {}:00:00"
    with open("on_show.sql","w") as f:
        for theater in range(1,62):
            for movie in [random.randint(6000,6800) for i in range(10)]:
                for i in range(8):
                    f.write("INSERT INTO on_show (movie_id,thea_id,seat_limit,price,time_schedule) VALUES ({},{},50,15,\"{}\");\n".format(movie,theater,schedule.format(random.randint(0,23))))


## transaction

# on-show 11-4890
# user 1-1000
def generate_trans():
    trans_time = "2017-08-12 {}:00:00"
    with open("transaction_user_onshow.sql","w") as f:
        for on_show_id in range(11,4891):
            for person in random.choices(range(1,1000),k = random.randint(5,10)):
                quantity = random.randint(1,5)
                f.write("INSERT INTO transaction_user_onshow (user_id,on_show_id,tran_time,quantity,total_price) VALUES ({},{},\"{}\",{},{});\n".format(random.randint(1,1000),on_show_id,trans_time.format(random.randint(0,23)),quantity,quantity * 15))
                f.write("UPDATE on_show SET seat_limit = seat_limit - {} WHERE id = {};\n".format(quantity,on_show_id))










if __name__ == '__main__':
    #generate_user()
    #generator_theater()
    #generate_onshow()
    #generate_trans()
