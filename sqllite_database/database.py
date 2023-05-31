import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')
# conn = sqlite3.connect(':memory:')

#create a cursor
c = conn.cursor()

#create a table
# c.execute("""CREATE TABLE customers(
#     first_name DATATYPE,
#     last_name DATATYPE,
#     email DATATYPE
#     )""")

#query the data base
c.execute("SELECT * FROM customers")
# print(c.fetchone())
# c.fetchmany(3)

items = c.fetchall()
for item in items:
    print(item)
many_customer = [
                    ('wes','Brown','wes@brown.com'),
                    ('steph','kuewa','steph@kuewa.com'),
                    ('kumar','lol','kumar@lol'),
                ]
#c.executemany("INSERT INTO customers VALUES(?,?,?)",many_customer)

c.execute("INSERT INTO customers VALUES('john','Elder','john@codemy.com')")


print("Command executes succesfully...")
#Datatypes
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#commit our command
conn.commit()

#close our connection
conn.close()


