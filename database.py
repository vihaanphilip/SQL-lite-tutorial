import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# conn = sqlite3.connect(':memory:') # Create a database in RAM

# Create a cursor
c = conn.cursor()


#################
# Create a table
#################

#SQLite Datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# c.execute("""CREATE TABLE customers (
#             first_name text,
#             last_name text,
#             email text
#           )""")

###############################
# Insert one record into table
###############################

# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

# print("Command executed successfully...")

#################################
# Insert many records into table
#################################

# many_customers = [
#                     ('Wes', 'Brown', 'wes@brown.com'),
#                     ('Steph', 'Kueg', 'steph@mail.com'),
#                     ('Dan', 'Pas', 'dan@mail.com'),
#                 ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# print("Command executed successfully...")


#################################
# Query the database
#################################

c.execute("SELECT * FROM customers")
# print(c.fetchone()[0])
# c.fetchmany(3)

items = c.fetchall()

print("NAME" + "\t\tEMAIL")
print("-----" + "\t\t-----")
for item in items:
    print(item[0] + " " + item[1] + "\t" + item[2])

# print("Command executed successfully...")

# Commit our command
conn.commit()

#Close our connection
conn.close()