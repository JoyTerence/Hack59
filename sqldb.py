#!/usr/bin/python

import sqlite3

class db:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        print "Opened database successfully";

    def create(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS HOTEL
           (NAME TEXT PRIMARY KEY     NOT NULL,
           ONE            INT     NOT NULL,
           TWO            INT     NOT NULL,
           THREE            INT     NOT NULL,
           FOUR            INT     NOT NULL);''')
        print "Table created successfully";

    def insert(self, hotel, a, b, c, d):
        self.cursor = self.conn.execute("SELECT NAME FROM HOTEL WHERE NAME = ?", (hotel))
        data = self.cursor.fetchall()
        if len(data)==0:
            self.conn.execute("INSERT INTO HOTEL VALUES (?, ?, ?, ?, ?);", (hotel, int(a), int(b), int(c), int(d)))
            self.conn.commit()
        else:
            self.cursor = self.conn.execute("SELECT ONE, TWO, THREE, FOUR FROM HOTEL WHERE NAME=?", (hotel))
            for row in self.cursor:
                tup =  [row[0], row[1], row[2], row[3]]
            tup[0] += a
            tup[1] += b
            tup[2] += c
            tup[3] += d
            self.conn.execute("UPDATE HOTEL SET one=?, TWO=?, THREE=?, FOUR=? WHERE NAME=?", (tup[0], tup[1], tup[2], tup[3], hotel))
            self.conn.commit()
        print "Records created successfully";
        
    def select(self):
        self.cursor = self.conn.execute("SELECT NAME, ONE, TWO, THREE, FOUR  from HOTEL ")
        tup = []
        for row in self.cursor:
            tup.append([str(row[0]), row[1], row[2], row[3],  row[4]])
        return tup

    def close(self):
        self.conn.close()
#!/usr/bin/python

import sqlite3

class db:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        print "Opened database successfully";

    def create(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS HOTEL
           (NAME TEXT PRIMARY KEY     NOT NULL,
           ONE            INT     NOT NULL,
           TWO            INT     NOT NULL,
           THREE            INT     NOT NULL,
           FOUR            INT     NOT NULL);''')
        print "Table created successfully";

    def insert(self, hotel, a, b, c, d):
        print hotel
        self.cursor = self.conn.execute("SELECT * FROM HOTEL WHERE NAME = ?", (hotel, ))
        data = self.cursor.fetchall()
        print data
        if len(data)==0:
            self.conn.execute("INSERT INTO HOTEL VALUES (?, ?, ?, ?, ?);", (hotel, int(a), int(b), int(c), int(d)))
            self.conn.commit()
        else:
            self.cursor = self.conn.execute("SELECT ONE, TWO, THREE, FOUR FROM HOTEL WHERE NAME=?", (hotel,))
            for row in self.cursor:
                tup =  [row[0], row[1], row[2], row[3]]
            tup[0] += a
            tup[1] += b
            tup[2] += c
            tup[3] += d
            self.conn.execute("UPDATE HOTEL SET one=?, TWO=?, THREE=?, FOUR=? WHERE NAME=?", (tup[0], tup[1], tup[2], tup[3], hotel))
            self.conn.commit()
        print "Records created successfully";
        
    def select(self):
        self.cursor = self.conn.execute("SELECT NAME, ONE, TWO, THREE, FOUR  from HOTEL ")
        tup = []
        for row in self.cursor:
            tup.append([str(row[0]), row[1], row[2], row[3],  row[4]])
        return tup

    def close(self):
        self.conn.close()
