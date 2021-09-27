import sqlite3

conn = sqlite3.connect("movies_data.db")
cur = conn.cursor()
cur.execute("select * from movies where wuw_status = 'Yes'")
data = cur.fetchall()
print(len(data))
print(data)

for movies in data:
    print(movies)

print(data[0][8])

# data[<row>][<column>]
# 1 movie name
# 2 release day
# 3 release month
# 4 release year
# 5 watched status
# 6 download status
# 7 link
# 8 origin
