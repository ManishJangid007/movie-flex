import sqlite3

conn = sqlite3.connect("movies_data.db")
cur = conn.cursor()

def total_movies():
    cur.execute("select * from movies")
    return len(cur.fetchall())

def total_unwatched_movies():
    cur.execute("select * from movies where wuw_status = 'No'")
    return len(cur.fetchall())

def total_watched_movies():
    cur.execute("select * from movies where wuw_status = 'Yes'")
    return len(cur.fetchall())

def total_undownloaded_movies():
    cur.execute("select * from movies where download_status = 'No'")
    return len(cur.fetchall())

def total_downloaded_movies():
    cur.execute("select * from movies where download_status = 'Yes'")
    return len(cur.fetchall())

def total_hollywood_movies():
    cur.execute("select * from movies where origin = 'Hollywood'")
    return len(cur.fetchall())

def total_bollywood_movies():
    cur.execute("select * from movies where origin = 'Bollywood'")
    return len(cur.fetchall())

def total_tollywood_movies():
    cur.execute("select * from movies where origin = 'Tollywood'")
    return len(cur.fetchall())

def total_other_movies():
    cur.execute("select * from movies where origin = 'Other'")
    return len(cur.fetchall())

if __name__ == "__main__":
    print(total_movies())
