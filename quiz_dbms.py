#   quiz application with dbms

import mysql.connector as my
from datetime import date

con = my.connect(host = "localhost",user = "root",passwd = "0176AL221002",database='quizapp')

cur = con.cursor()

#sql = "create table users (name varchar(20), erlno int primary key, email varchar(30), pwd varchar(8))"
#cur.execute(sql)

logged_in = False
log_in_user = ''

def register():
    name = input("Enter your name: ")
    erlno = input("Enter your enrollment number: ")
    email = input("Enter your email: ")
    pwd = input("Enter password: ")
    try:
        sql = "insert into users (name,erlno,email,pwd) values (%s,%s,%s,%s)"
        val =  (name,erlno,email,pwd)
        cur.execute(sql,val)
        con.commit()
    except:
        print("****ENROLLMENT NUMBER ALREADY EXSITS****")

    ch = int(input("****1> LOGIN    2> EXIT****"))
    if ch == 1:
        login()
    else:
        print("THANK YOU")
        exit()

def login():
    global logged_in
    global log_in_user
    erlno = input("****ENTER YOUR ENROLLMENT NUMBER****")
    sql = "select name,pwd from users where erlno = %s"
    val = (erlno,)
    cur.execute(sql,val)
    data = cur.fetchone()
    if data:
        pwd = input("****ENTER PASSWORD**** ")
        if pwd == data[1]:
            print(f"Welcome {data[0]}")
            logged_in = True
            log_in_user = erlno
        
    else:
        print("****WRONG ENROLLMENT NUMBER****")
        ch = int(input("****1> LOGIN    2> EXIT****"))
        if ch == 1:
            login()
        else:
            print("****THANK YOU****")
            exit()

    choices()

def choices():
    ch = int(input("****1> START GAME     2>CHANGE PASSWORD     3> EDIT PROFILE    4> SHOW PROFILE      5> REMOVE PROFILE    6> QUIT****"))
    if ch==1:
        game(logged_in,log_in_user)
    elif ch==2:
        changepwd(logged_in,log_in_user)
    elif ch==3:
        editprofile(logged_in,log_in_user)
    elif ch==4:
        showprofile(logged_in,log_in_user)
    elif ch==5:
        removeprofile(logged_in,log_in_user)
    else:
        print("****THANK YOU****")
        exit()


def game(status,user):
    if status:
        score = 0
        domain = ""
        ch = int(input("****CHOOSE DOMAIN****\n1> HTML\n2> PYTHON\n3> DBMS"))
        if ch==1:
            domain = "HTML"
        elif ch==2:
            domain = "Python"
        elif ch==3:
            domain = "DBMS"
        sql = "select ques,options,correct from qna where subject = %s order by RAND() limit 5"
        cur.execute(sql,(domain,))
        data = cur.fetchall()
        for i in data:
            print(f"QUESTION: {i[0]}\n{i[1]}")
            ans = int(input("ENTER YOUR ANSWER: "))
            if ans == int(i[2]):
                print("****CORRECT****")
                score += 1
            else:
                print("****INCORRECT****")
        print(f"****YOU SCORED {score}****")

        cur_date = date.today()
        sql = "insert into result values (%s,%s,%s,%s)"
        val = (user,score,domain,cur_date)
        cur.execute(sql,val)
        con.commit()

    else:
        print("****YOU ARE NOT LOGGED IN****")  
    
    choices()

def changepwd(status,user):
    if status:
        pwd = input("****ENTER NEW PASSWORD****")
        sql = "update users set pwd = %s where erlno = %s"
        val = (pwd,user)
        cur.execute(sql,val)
        print(f"****{user} YOUR PASSWORD HAS BEEN CHANGED****")
        con.commit()
    else:
        print("****YOU ARE NOT LOGGED IN****")
    choices()

def editprofile(status,user):
    if status:
        ch = int(input("****1>CHANGE NAME    2>CHANGE EMAIL****"))
        if ch==1:
            nm = input("****ENTER NEW NAME****")
            sql = "update users set name = %s where erlno = %s"
            val = (nm,user)
            cur.execute(sql,val)
            print("****NAME CHANGED SUCCESSFULLY****")
            con.commit()
        elif ch==2:
            mail = input("****ENTER NEW EMAIL****")
            sql = "update users set email = %s where erlno = %s"
            val = (mail,user)
            cur.execute(sql,val)
            print("****EMAIL CHANGED SUCCESSFULLY****")
            con.commit()
        else:
            print("****INVALID CHOICE****")
    else:
        print("****YOU ARE NOT LOGGED IN****")
    choices()


def showprofile(status,user):
    if status:
        sql = "select * from users where erlno = %s"
        val = (user,)
        cur.execute(sql,val)
        data = cur.fetchone()
        if len(data)>0:
            print(f"NAME : {data[0]}\nENROLLMENT NO. : {data[1]}\nEMAIL ID : {data[2]}")

        sql = "select score,subject,score_date from result where erlno = %s"
        val = (user,)
        cur.execute(sql,val)
        data = cur.fetchall()
        if data:
            print(f"****SCORES OF {user}****")
            for i in data:
                print(f"{i[0]},{i[1]},{i[2]}")
        else:
            print("****NO SCORE FOUND****")
    else:
        print("****YOU ARE NOT LOGGED IN****")
    choices()

def removeprofile(status,user):
    if status:
        ch = input("DO YOU WANT TO PERMANENTLY DELETE YOUR PROFILE? (Y/N) :")
        if ch.upper() == 'Y':
            sql = "delete from users where erlno = %s"
            val = (int(user),)
            cur.execute(sql,val)
            con.commit()
            print("****PROFILE DELETED SUCCESSFULLY****")
        else:
            pass
    else:
        print("****YOU ARE NOT LOGGED IN****")
    choices()


while True:
    print("****WELCOME USER****")
    ch = int(input("****1> REGISTER     2>LOGIN     3>QUIT****"))
    if ch == 1:
        register()
    elif ch==2:
        login()
    else:
        print("THANK YOU")
        exit()