import sqlite3

connect = sqlite3.connect("db.db")
current = connect.cursor()

current.execute("CREATE TABLE user(id INTEGER PRIMARY KEY NOT NULL,"
                "todo TEXT,date DATE, name TEXT,password TEXT)")

current.execute("INSERT INTO user(name,password,todo,date) VALUES"
                "('todo','date','name','password')")

connect.commit()
