#quiz application
#Aastha Dekate 0176AL221002

from random import *

#key : username, value : previous highest score
user = {"aastha":3}

def login():
    user_name = input("ENTER USER NAME : ")
    if user_name.lower() not in user:
        user[user_name.lower()] = 0
        print(f"WELCOME {user_name}!")
    else:
        print(f"WELCOME {user_name}, YOUR HIGHEST SCORE IS {user[user_name.lower()]}!")
    cur_score = game()
    if cur_score > user[user_name.lower()]:
        user[user_name.lower()] = cur_score
        print(f"****YOUR NEW HIGH SCORE IS {cur_score}****")
    else:
        print(f"****YOUR SCORE IS {cur_score}****")



def game():
    score = 0
    print("****SELECT DOMAIN****\n****1. HTML****\n****2. DBMS****\n****3. PYTHON****\n")
    x = int(input())
    #HTML
    if x == 1:
        print("****DOMAIN : HTML****")
        q_html = {"Q>> WHAT IS a TAG?": "1> ASSIGNMENT TAG\n2> ANCHOR TAG\n3> ALIGN TAG\n4> NONE",
        "Q>> WHAT DOES HTML STAND FOR?": "1> Hyperlinks and Text Markup Language\n2> Home Tool Markup Language\n3> Hyper Text Markup Language\n4> High Text Machine Language",
        "Q>> WHICH TAG IS USED TO CREATE A PARAGRAPH IN HTML?": "1> <br>\n2> <p>\n3> <h1>\n4> <a>",
        "Q>> WHICH TAG IS USED TO CREATE A LINK IN HTML?": "1> <img>\n2> <div>\n3> <a>\n4> <span>",
        "Q>> HOW DO YOU CREATE A NUMBERED LIST IN HTML?": "1> <ul>\n2> <ol>\n3> <li>\n4> <dl>",
        "Q>> WHICH TAG IS USED TO INSERT AN IMAGE IN HTML?": "1> <image>\n2> <img>\n3> <pic>\n4> <photo>",
        "Q>> WHICH TAG IS USED TO CREATE A LINE BREAK?": "1> <br>\n2> <lb>\n3> <break>\n4> <line>",
        "Q>> WHAT IS THE PURPOSE OF THE <title> TAG?": "1> Define page body\n2> Set page title\n3> Add an image\n4> Create a link",
        "Q>> WHICH ATTRIBUTE IS USED TO PROVIDE A UNIQUE IDENTIFIER FOR AN ELEMENT?": "1> class\n2> id\n3> name\n4> href",
        "Q>> WHAT DOES THE <b> TAG DO?": "1> Makes text bold\n2> Creates a button\n3> Adds a background color\n4> Creates a line break",
        "Q>> WHICH TAG IS USED TO CREATE A HORIZONTAL LINE?": "1> <hr>\n2> <hl>\n3> <line>\n4> <break>",
        "Q>> WHICH ATTRIBUTE IS USED TO OPEN A LINK IN A NEW TAB?": "1> new=\"true\"\n2> target=\"_blank\"\n3> link=\"new\"\n4> window=\"new\"",
        "Q>> WHICH TAG IS USED FOR CREATING A DROPDOWN LIST?": "1> <list>\n2> <select>\n3> <dropdown>\n4> <menu>",
        "Q>> WHAT IS THE TAG FOR THE LARGEST HEADING?": "1> <h6>\n2> <h1>\n3> <header>\n4> <title>",
        "Q>> WHICH ATTRIBUTE IS USED TO PROVIDE ALTERNATIVE TEXT FOR AN IMAGE?": "1> title\n2> alt\n3> name\n4> caption",
        "Q>> WHICH TAG IS USED TO DEFINE AN UNORDERED LIST?": "1> <ol>\n2> <ul>\n3> <list>\n4> <li>",
        "Q>> WHAT IS THE CORRECT SYNTAX FOR A COMMENT IN HTML?": "1> /* Comment */\n2> <!-- Comment -->\n3> // Comment\n4> # Comment",
        "Q>> WHAT DOES THE <a> TAG DEFINE?": "1> An audio file\n2> A link\n3> An anchor\n4> A paragraph",
        "Q>> WHAT IS THE PURPOSE OF THE <meta> TAG?": "1> Include media\n2> Add metadata\n3> Create navigation\n4> Style the page",
        "Q>> WHICH TAG IS USED FOR ADDING A TABLE ROW?": "1> <td>\n2> <tr>\n3> <table>\n4> <row>"}

        a_html = {"Q>> WHAT IS a TAG?": 2,
        "Q>> WHAT DOES HTML STAND FOR?": 3,
        "Q>> WHICH TAG IS USED TO CREATE A PARAGRAPH IN HTML?": 2,
        "Q>> WHICH TAG IS USED TO CREATE A LINK IN HTML?": 3,
        "Q>> HOW DO YOU CREATE A NUMBERED LIST IN HTML?": 2,
        "Q>> WHICH TAG IS USED TO INSERT AN IMAGE IN HTML?": 2,
        "Q>> WHICH TAG IS USED TO CREATE A LINE BREAK?": 1,
        "Q>> WHAT IS THE PURPOSE OF THE <title> TAG?": 2,
        "Q>> WHICH ATTRIBUTE IS USED TO PROVIDE A UNIQUE IDENTIFIER FOR AN ELEMENT?": 2,
        "Q>> WHAT DOES THE <b> TAG DO?": 1,
        "Q>> WHICH TAG IS USED TO CREATE A HORIZONTAL LINE?": 1,
        "Q>> WHICH ATTRIBUTE IS USED TO OPEN A LINK IN A NEW TAB?": 2,
        "Q>> WHICH TAG IS USED FOR CREATING A DROPDOWN LIST?": 2,
        "Q>> WHAT IS THE TAG FOR THE LARGEST HEADING?": 2,
        "Q>> WHICH ATTRIBUTE IS USED TO PROVIDE ALTERNATIVE TEXT FOR AN IMAGE?": 2,
        "Q>> WHICH TAG IS USED TO DEFINE AN UNORDERED LIST?": 2,
        "Q>> WHAT IS THE CORRECT SYNTAX FOR A COMMENT IN HTML?": 2,
        "Q>> WHAT DOES THE <a> TAG DEFINE?": 2,
        "Q>> WHAT IS THE PURPOSE OF THE <meta> TAG?": 2,
        "Q>> WHICH TAG IS USED FOR ADDING A TABLE ROW?": 2}

        q = sample(list(q_html.items()),5)
        for i in range(len(q)):
            print(q[i][0],"\n",q[i][1])
            ans = int(input())
            if ans == int(a_html[q[i][0]]):
                score += 1
                print("****CORRECT ANSWER****")
            else:
                print("****INCORRECT ANSWER****")
        
    
    #DBMS
    elif x == 2:
        print("****DOMAIN : DBMS****")
        q_dbms = {"Q>> WHAT DOES DBMS STAND FOR?": "1> Data Binding and Management System\n2> Database Management System\n3> Data Backup Management Software\n4> Database Backup and Maintenance System",
        "Q>> WHICH SQL STATEMENT IS USED TO RETRIEVE DATA FROM A DATABASE?": "1> SELECT\n2> DELETE\n3> INSERT\n4> UPDATE",
        "Q>> WHAT IS A PRIMARY KEY?": "1> A key that is never used\n2> A unique identifier for a record\n3> A key to open the database\n4> A password",
        "Q>> WHICH COMMAND IS USED TO REMOVE A TABLE FROM A DATABASE?": "1> DELETE TABLE\n2> REMOVE TABLE\n3> DROP TABLE\n4> CLEAR TABLE",
        "Q>> WHAT DOES `NULL` REPRESENT IN A DATABASE?": "1> Zero value\n2> Empty value\n3> Duplicate value\n4> A non-existent value",
        "Q>> WHICH SQL STATEMENT IS USED TO MODIFY DATA IN A TABLE?": "1> UPDATE\n2> MODIFY\n3> CHANGE\n4> ALTER",
        "Q>> WHAT IS A FOREIGN KEY?": "1> A key that doesn't belong\n2> A key used to link two tables\n3> A duplicate key\n4> A password",
        "Q>> WHICH COMMAND IS USED TO ADD A NEW RECORD IN A DATABASE TABLE?": "1> ADD\n2> INSERT INTO\n3> NEW\n4> CREATE",
        "Q>> WHICH OF THE FOLLOWING IS NOT A DATABASE MODEL?": "1> Hierarchical\n2> Relational\n3> Object-Oriented\n4> Linear",
        "Q>> WHICH FUNCTION IS USED TO COUNT THE NUMBER OF ROWS IN A DATABASE?": "1> COUNT()\n2> SUM()\n3> TOTAL()\n4> ADD()",
        "Q>> WHAT IS THE PURPOSE OF THE `JOIN` OPERATION IN SQL?": "1> To delete tables\n2> To add new rows\n3> To link data from multiple tables\n4> To update data",
        "Q>> WHAT IS A UNIQUE KEY?": "1> It is the same as a primary key\n2> It ensures all values are unique in a column\n3> It allows duplicates\n4> It has no role",
        "Q>> WHAT DOES `SQL` STAND FOR?": "1> Simple Query Language\n2> Structured Query Language\n3> Strong Query Language\n4> System Query Language",
        "Q>> WHAT IS THE COMMAND TO CREATE A NEW TABLE IN SQL?": "1> CREATE NEW TABLE\n2> MAKE TABLE\n3> CREATE TABLE\n4> NEW TABLE",
        "Q>> WHICH CLAUSE IS USED TO FILTER RECORDS IN SQL?": "1> WHERE\n2> HAVING\n3> FILTER\n4> GROUP BY",
        "Q>> WHICH SQL STATEMENT IS USED TO DELETE DATA FROM A TABLE?": "1> DROP\n2> REMOVE\n3> DELETE\n4> CLEAR",
        "Q>> WHAT IS A `VIEW` IN SQL?": "1> A virtual table based on a query\n2> A physical table\n3> A type of key\n4> A stored procedure",
        "Q>> WHAT IS `NORMALIZATION` IN DBMS?": "1> To reduce redundancy\n2> To add more columns\n3> To make the database slower\n4> To delete rows",
        "Q>> WHICH KEYWORD IS USED TO SORT THE RESULT-SET IN SQL?": "1> ORDER BY\n2> SORT BY\n3> ARRANGE\n4> ALIGN",
        "Q>> WHICH SQL COMMAND IS USED TO CHANGE THE STRUCTURE OF A TABLE?": "1> MODIFY\n2> UPDATE\n3> ALTER\n4> CHANGE"}

        a_dbms = {"Q>> WHAT DOES DBMS STAND FOR?": 2,
        "Q>> WHICH SQL STATEMENT IS USED TO RETRIEVE DATA FROM A DATABASE?": 1,
        "Q>> WHAT IS A PRIMARY KEY?": 2,
        "Q>> WHICH COMMAND IS USED TO REMOVE A TABLE FROM A DATABASE?": 3,
        "Q>> WHAT DOES `NULL` REPRESENT IN A DATABASE?": 4,
        "Q>> WHICH SQL STATEMENT IS USED TO MODIFY DATA IN A TABLE?": 1,
        "Q>> WHAT IS A FOREIGN KEY?": 2,
        "Q>> WHICH COMMAND IS USED TO ADD A NEW RECORD IN A DATABASE TABLE?": 2,
        "Q>> WHICH OF THE FOLLOWING IS NOT A DATABASE MODEL?": 4,
        "Q>> WHICH FUNCTION IS USED TO COUNT THE NUMBER OF ROWS IN A DATABASE?": 1,
        "Q>> WHAT IS THE PURPOSE OF THE `JOIN` OPERATION IN SQL?": 3,
        "Q>> WHAT IS A UNIQUE KEY?": 2,
        "Q>> WHAT DOES `SQL` STAND FOR?": 2,
        "Q>> WHAT IS THE COMMAND TO CREATE A NEW TABLE IN SQL?": 3,
        "Q>> WHICH CLAUSE IS USED TO FILTER RECORDS IN SQL?": 1,
        "Q>> WHICH SQL STATEMENT IS USED TO DELETE DATA FROM A TABLE?": 3,
        "Q>> WHAT IS A `VIEW` IN SQL?": 1,
        "Q>> WHAT IS `NORMALIZATION` IN DBMS?": 1,
        "Q>> WHICH KEYWORD IS USED TO SORT THE RESULT-SET IN SQL?": 1,
        "Q>> WHICH SQL COMMAND IS USED TO CHANGE THE STRUCTURE OF A TABLE?": 3}

        q = sample(list(q_dbms.items()),5)
        for i in range(len(q)):
            print(q[i][0],"\n",q[i][1])
            ans = int(input())
            if ans == int(a_dbms[q[i][0]]):
                score += 1
                print("****CORRECT ANSWER****")
            else:
                print("****INCORRECT ANSWER****")

    
    #PYTHON
    elif x == 3:
        print("****DOMAIN : PYTHON****")
        q_python = {"Q>> WHICH OF THE FOLLOWING IS A VALID VARIABLE NAME IN PYTHON?": "1> 1variable\n2> my_var\n3> @var\n4> -var",
        "Q>> WHAT DOES THE `print()` FUNCTION DO?": "1> Adds two numbers\n2> Displays output on the screen\n3> Creates a list\n4> Deletes a variable",
        "Q>> WHICH OPERATOR IS USED FOR EXPONENTIATION IN PYTHON?": "1> **\n2> ^\n3> //\n4> %",
        "Q>> WHICH FUNCTION IS USED TO GET THE LENGTH OF A STRING?": "1> length()\n2> len()\n3> size()\n4> getLength()",
        "Q>> WHAT IS THE OUTPUT OF `print(5 // 2)` IN PYTHON?": "1> 2\n2> 2.5\n3> 3\n4> 1",
        "Q>> WHICH OF THE FOLLOWING IS A DATA TYPE IN PYTHON?": "1> integer\n2> string\n3> float\n4> All of the above",
        "Q>> WHAT IS THE CORRECT WAY TO CREATE A FUNCTION IN PYTHON?": "1> def myFunction():\n2> function myFunction()\n3> create myFunction()\n4> func myFunction()",
        "Q>> WHICH OF THE FOLLOWING IS A RESERVED KEYWORD IN PYTHON?": "1> try\n2> define\n3> assign\n4> loop",
        "Q>> WHICH FUNCTION IS USED TO CONVERT A STRING INTO AN INTEGER?": "1> int()\n2> str()\n3> float()\n4> string()",
        "Q>> WHAT DOES `list.append()` DO?": "1> Add an item to the list\n2> Remove an item from the list\n3> Sort the list\n4> Copy the list",
        "Q>> HOW DO YOU WRITE A COMMENT IN PYTHON?": "1> // Comment\n2> /* Comment */\n3> # Comment\n4> <!-- Comment -->",
        "Q>> WHAT WILL BE THE OUTPUT OF `5 % 2` IN PYTHON?": "1> 0\n2> 1\n3> 2\n4> 5",
        "Q>> WHICH FUNCTION IS USED TO GET USER INPUT IN PYTHON 3?": "1> input()\n2> scan()\n3> get_input()\n4> read()",
        "Q>> HOW DO YOU CREATE A LIST IN PYTHON?": "1> []\n2> {}\n3> ()\n4> <>",
        "Q>> WHICH OF THE FOLLOWING IS A COMPARISON OPERATOR IN PYTHON?": "1> =\n2> ==\n3> !=\n4> Both 2 and 3",
        "Q>> WHAT IS A DICTIONARY IN PYTHON?": "1> A list of numbers\n2> A collection of key-value pairs\n3> A type of loop\n4> A function",
        "Q>> WHICH MODULE IS USED FOR RANDOM NUMBER GENERATION IN PYTHON?": "1> math\n2> os\n3> random\n4> sys",
        "Q>> HOW DO YOU ACCESS THE ELEMENTS OF A LIST IN PYTHON?": "1> Using keys\n2> Using index numbers\n3> Using parentheses\n4> Using colons",
        "Q>> WHAT IS THE OUTPUT OF `len([1, 2, 3])`?": "1> 1\n2> 2\n3> 3\n4> 4",
        "Q>> WHICH STATEMENT IS USED FOR LOOPING OVER A RANGE OF NUMBERS?": "1> while\n2> repeat\n3> range\n4> for"}

        a_python = {"Q>> WHICH OF THE FOLLOWING IS A VALID VARIABLE NAME IN PYTHON?": 2,
        "Q>> WHAT DOES THE `print()` FUNCTION DO?": 2,
        "Q>> WHICH OPERATOR IS USED FOR EXPONENTIATION IN PYTHON?": 1,
        "Q>> WHICH FUNCTION IS USED TO GET THE LENGTH OF A STRING?": 2,
        "Q>> WHAT IS THE OUTPUT OF `print(5 // 2)` IN PYTHON?": 1,
        "Q>> WHICH OF THE FOLLOWING IS A DATA TYPE IN PYTHON?": 4,
        "Q>> WHAT IS THE CORRECT WAY TO CREATE A FUNCTION IN PYTHON?": 1,
        "Q>> WHICH OF THE FOLLOWING IS A RESERVED KEYWORD IN PYTHON?": 1,
        "Q>> WHICH FUNCTION IS USED TO CONVERT A STRING INTO AN INTEGER?": 1,
        "Q>> WHAT DOES `list.append()` DO?": 1,
        "Q>> HOW DO YOU WRITE A COMMENT IN PYTHON?": 3,
        "Q>> WHAT WILL BE THE OUTPUT OF `5 % 2` IN PYTHON?": 2,
        "Q>> WHICH FUNCTION IS USED TO GET USER INPUT IN PYTHON 3?": 1,
        "Q>> HOW DO YOU CREATE A LIST IN PYTHON?": 1,
        "Q>> WHICH OF THE FOLLOWING IS A COMPARISON OPERATOR IN PYTHON?": 4,
        "Q>> WHAT IS A DICTIONARY IN PYTHON?": 2,
        "Q>> WHICH MODULE IS USED FOR RANDOM NUMBER GENERATION IN PYTHON?": 3,
        "Q>> HOW DO YOU ACCESS THE ELEMENTS OF A LIST IN PYTHON?": 2,
        "Q>> WHAT IS THE OUTPUT OF `len([1, 2, 3])`?": 3,
        "Q>> WHICH STATEMENT IS USED FOR LOOPING OVER A RANGE OF NUMBERS?": 4}

        q = sample(list(q_python.items()),5)
        for i in range(len(q)):
            print(q[i][0],"\n",q[i][1])
            ans = int(input())
            if ans == int(a_python[q[i][0]]):
                score += 1
                print("****CORRECT ANSWER****")
            else:
                print("****INCORRECT ANSWER****")

    
    else:
        print("****INVALID DOMAIN NUMBER****")

    

    print(f"****YOU SCORED {score}****")
    print("****1. PLAY AGAIN****\n****2. QUIT****")
    ch = int(input())
    if ch == 1:
        game()
    else:
        print("****THANK YOU FOR PLAYING****")
        return score

login()