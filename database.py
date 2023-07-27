import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# conn = sqlite3.connect(':memory:') # Create a database in RAM

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
            first_name DATATYPE,
            last_name DATATYPE,
            email DATATYPE
          )""")

#SQLite Datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB