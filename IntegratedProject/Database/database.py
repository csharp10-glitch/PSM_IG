import sqlite3
# import sqlalchemy
# import PyQt5
# import kivy
# # import PyGUI
# # import PySide2
# import tkinter

import sqlite3
conn = sqlite3.connect('../../../CnT/Misc/hgt/data/eTerrain.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE terrain
             (date text, trans text, symbol text, lat real, long real, elev real)''')

# Insert a row of data
c.execute("INSERT INTO terrain VALUES ('2020-05-18','log','loc', 40, 114, 500)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

conn = sqlite3.connect('../../../CnT/Misc/hgt/data/eTerrain.db')
c = conn.cursor()

# # Never do this -- insecure!
# symbol = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('loc',)
c.execute('SELECT * FROM terrain WHERE symbol=?', t)
print(c.fetchone())

# # Larger example that inserts many records at a time
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

for row in c.execute('SELECT * FROM terrain ORDER BY elev'):
        print(row)