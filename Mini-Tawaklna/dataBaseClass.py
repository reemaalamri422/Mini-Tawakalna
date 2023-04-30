import sqlite3

class dataBaseClass:
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    #c.execute("CREATE TABLE INDIVIDUALS (NAME TEXT NOT NULL , SEX TEXT NOT NULL ,ID TEXT  NOT \
    #NULL , BIRTH TEXT NOT NULL , TYPEOF_VAC TEXT NOT NULL , DATE_TIME TEXT NOT NULL ,PHONE_N INT NOT NULL)")

    def construct(self,name,sex,id,birth,vac,date,phone):
        dataBaseClass.c.execute("INSERT INTO INDIVIDUALS (NAME,SEX,ID,BIRTH,TYPEOF_VAC, DATE_TIME,PHONE_N)VALUES(?,?,?,?,?,?,?)",
                  (name,sex, id,birth,vac,date,phone))
        dataBaseClass.conn.commit()
    def cur():
        cursor= dataBaseClass.c.execute("SELECT ID FROM INDIVIDUALS")
        return cursor
    def closeCursor():
        dataBaseClass.c.close()
