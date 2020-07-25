import sqlite3

with sqlite3.connect('presenceservice.db') as connection:
    c = connection.cursor()
    #c.execute('CREATE TABLE userreg_details(username TEXT, email TEXT, password TEXT)')
    c.execute('INSERT INTO userreg_details VALUES("Sandeep", "s@g.com", "1234")')
