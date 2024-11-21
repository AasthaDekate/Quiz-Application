from random import sample

flag = False
user = ''

def registration():
    name = input("ENTER YOUR NAME : ")
    erl_no = input("ENTER ENROLLMENT NO. : ")
    email = input("ENTER YOUR EMAIL : ")
    pwd = input("SET PASSWORD : ")

    with open("register.txt","r+") as file:
        user_found = False
        for i in file:
            data = i.rstrip("\n").rstrip(" ").split(",")
            if erl_no == data[1]:
                print("****ALREADY REGISTERED****")
                user_found = True
                break
        if not user_found:
            file.write(name + "," + erl_no + "," + email + "," +pwd+'\n')
        
    ch = input("****1> LOGIN      2> QUIT****")
    if ch == "1":
        login()
    else:
        print("****THANK YOU****")


def login():
    global flag
    global user
    erl_no = input("ENTER YOUR ENROLLMENT NO. : ")
    pwd = input("ENTER YOUR PASSWORD : ")
    with open("register.txt","r") as file:
        for i in file:
            data = i.rstrip("\n").rstrip(" ").split(",")
            if data[1] == erl_no and data[3] == pwd:
                print("****LOGIN SUCCESSFULL****")
                flag = True
                user = erl_no
                break
                    
        if flag == False:
            print("****WRONG ENROLLMENT NO. OR PASSWORD****")
            login()

    game()

def game():
    global flag
    global user
    print("****CHOOSE DOMAIN****")
    domain = int(input("****1>HTML   2>PYTHON    3>DBMS****"))
    ch = ""
    score = 0
    que = []
    if domain == 1:
        ch = "HTML"
    elif domain == 2:
        ch = "Python"
    elif domain == 3:
        ch = "DBMS"
    else:
        print("****INVALID CHOICE****")
    with open("qna.txt","r") as file:
        for i in file:
            data = i.strip().split(", ")
            if data[-1] == ch:
                que.append(data)
    question = sample(que,5)

    for i in question:
        print(i[0],"\n",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\n")
        ans = int(input("YOUR ANSWER : "))
        if ans == int(i[5]):
            print("****CORRECT****")
            score += 1
        else:
            print("****INCORRECT****")
    
    print("YOUR SCORE IS : ",score)
    with open("result.txt","r+") as res:
        lines = res.readlines()
        res.seek(0)
        res.truncate()
        prt = False
        for i in lines:
            data = i.strip().split(",")
            if data[0] == user:
                data.append(str(score)+","+ch+'\n')
                res.write(",".join(data))
                prt = True
            else:
                res.write(i)
        if not prt:
            res.write('\n'+user+','+str(score)+','+ch+'\n')

    while True:
        print("****1. PLAY AGAIN    2.VIEW SCORES   3.QUIT****")
        ch = int(input("ENTER YOUR CHOICE : "))
        if ch==1:
            game()
        elif ch==2:
            result(user)
        else:
            print("****THANK YOU****")
            exit()


def result(player):
    with open("result.txt","r") as file:
        flag = False
        for i in file:
            data = i.strip().split(",")
            if data[0] == player:
                print(f"****SCORES OF {player}****")
                print(",".join(data[1:]))
                flag = True
                break
        if not flag:
            print("****NO RECORD FOUND****")


while True:
    print("****WELCOME TO THE GAME****")
    ch = int(input("****1> REGISTRATION      2> LOGIN    3> VIEW SCORES     4> QUIT****"))
    if ch == 1:
        registration()
    elif ch == 2:
        login()
    elif ch==3:
        player = input("ENTER ENROLLMENT NUMBER : ")
        result(player)
    else:
        print("****THANK YOU****")
        exit()
