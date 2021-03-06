import mysql.connector as ms
from pathlib import Path
from math import *

operations = [["3","sqrt","square root of"," " ],[" ", "**", "^", " "], [" ", "**", "to the power of", " "],
              ["3","sin","sine of"," "],["3","sin","sin of"," "],
              ["3","sin","sine"," " ], ["3","cos","cosine of"," "], ["3","cos","cosine"," " ],
              ["3","cos","cos of"," "], ["3","tan","tan of"," " ], [" ", "*", "multiplied by", " "], [" ", "*", "multiplied with", " "], 
              [" ", "/", "divided by", " "], ["2", "/", "divide","by"], ["1", "/", "divide","from"],
              ["2", "*", "multiply","with"], ["2", "*", "multiply","by"],[" ","*","x"," "], [" ", "+", "added by", " "], 
              [" ", "+", "added with", " "], [" ", "-", "subtracted by", " "], ["2", "+", "add","with"], ["2", "+", "add","to"],
              ["1", "-", "subtract","from"], ["2", "-", "subtract","by"], 
              [" ", ">=", "greater than or equal to", " "], [" ", ">", "is greater than", " "], 
              [" ", ">", "greater than", " "], [" ", "<=", "lesser than or equal to", " "], [" ", "<=", "less than or equal to", " "], [" ", "<", "is less than", " "], 
              [" ", "<", "less than", " "], [" ", "==", "is equal to", " "], [" ", "==", "equal to", " "], ]

def relative_to_bg(path: str) -> Path:
        return BG_PATH / Path(path)
OUTPUT_PATH = Path(__file__).parent
BG_PATH = OUTPUT_PATH / Path("./backgrounds")

def check_password(password):
    global con, cur
    con = ms.connect(host = "localhost", user = "root", passwd = password)
    cur = con.cursor()
    if con.is_connected():
        return True
    else:
        return False
        

def exists(database):
    cur.execute("show databases")
    data = cur.fetchall()
    for x in data:
        if database in x:
            return True
    return False

def create_table(tablename):
    cur.execute('use alphacalc')
    b = "create table "+ tablename+" (type varchar(1), translation varchar (10), operation_part_1 varchar(50), operation_part_2 varchar(50))"
    cur.execute(b)
    for x in operations:
        a = "insert into "+tablename+ " values ( '%s', '%s', '%s', '%s' )" %(x[0], x[1], x[2], x[3])
        cur.execute(a)
        con.commit()

def create_presets():
    create_table("operations") 

def user_login():
    if not exists('alphacalc'):
        cur.execute("create database alphacalc")
        cur.execute("use alphacalc")
        cur.execute('create table Memory (Date date, Time time, Expression varchar(50), Answer varchar(50))')
        create_presets()
