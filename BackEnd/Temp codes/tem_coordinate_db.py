import sqlite3
#generating data worth 31 days, assuming coordinate are collected every second 
#DO NOT EXECUTE THIS CODE, IT WILL CREATE A DB FILE OF 300MB
#creating connection to the database
conn = sqlite3.connect('example3.db')
#connecting cursor
c = conn.cursor()
#creating columns
c.execute('''CREATE TABLE IF NOT EXISTS bus_locations
             (bus1lat, bus1long, bus1bearing,
              bus2lat, bus2long, bus2bearing,
              bus3lat, bus3long, bus3bearing,
              bus4lat, bus4long,  bus4bearing)''')

loc = [15.88977155]*12

#pushing data in db file
for i in range (2678400):
    c.execute('INSERT INTO bus_locations (bus1lat, bus1long, bus2long, bus2lat, bus3long, bus3lat, bus4lat, bus4long, bus1bearing, bus2bearing, bus3bearing,bus4bearing) VALUES (?,?,?,?,?,?,?, ?, ?, ?, ?, ?)', loc)

#saving changes and closing connection
conn.commit()
conn.close()