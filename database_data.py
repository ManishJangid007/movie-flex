import sqlite3


class DataMachine:
    def __init__(self):
        self.conn = sqlite3.connect('movies_data.db')
        self.cur = self.conn.cursor()

    def add_movie(self, name, release_day, release_month, release_year, wuw_status, download_status, link, origin):
        try:
            self.cur.execute(
                "insert into movies ('name', 'release_day', 'release_month', 'release_year', 'wuw_status', 'download_status', 'link', 'origin') "
                "values(:name, :release_day, :release_month, :release_year, :wuw_status, :download_status, :link, :origin)", {
                    "name": name,
                    "release_day": release_day,
                    "release_month": release_month,
                    "release_year": release_year,
                    "wuw_status": wuw_status,
                    "download_status": download_status,
                    "link": link,
                    "origin": origin
                })
            self.conn.commit()
            msg = "Movie Added :)"
            return msg
        except:
            msg = "Failed to Add Movie :("
            return msg

    def update_name(self, m_id, name):
        try:
            self.cur.execute("UPDATE movies SET name=:name WHERE m_id=:m_id", {
                "name": name,
                "m_id": m_id
            })
            self.conn.commit()
            msg = "Updated :)"
            return msg
        except:
            msg = "Failed to Update"
            return msg

    def update_release_date(self, m_id, release_day, release_month, release_year):
        try:
            self.cur.execute(
                "UPDATE movies SET release_day=:release_day, release_month=:release_month, release_year=:release_year WHERE m_id = :m_id",
                {
                    "release_day": release_day,
                    "release_month": release_month,
                    "release_year": release_year,
                    "m_id": m_id
                })
            self.conn.commit()
            msg = "Updated :)"
            return msg
        except:
            msg = "Failed to Update :)"
            return msg

    def update_wuw_status(self, m_id, status):
        try:
            self.cur.execute("UPDATE movies SET wuw_status=:status WHERE m_id = :m_id", {
                "status": status,
                "m_id": m_id
            })
            self.conn.commit()
            msg = "Updated :)"
            return msg
        except:
            msg = "Failed to Update :("
            return msg

    def update_download_status(self, m_id, status):
        try:
            self.cur.execute("UPDATE movies SET download_status=:status WHERE m_id=:m_id", {
                "status": status,
                "m_id": m_id
            })
            self.conn.commit()
            msg = "Updated :)"
            return msg
        except:
            msg = "Failed to Update"
            return msg

    def update_link(self, m_id, link):
        try:
            self.cur.execute("UPDATE movies SET link = :link WHERE m_id = :m_id", {
                "link": link,
                "m_id": m_id
            })
            self.conn.commit()
            msg = "Updated :)"
            return msg
        except:
            msg = "Failed to Update"
            return msg

    def update_origin(self, m_id, origin):
        try:
            self.cur.execute("UPDATE movies SET origin=:origin WHERE m_id=:m_id", {
                "origin": origin,
                "m_id": m_id
            })
            self.conn.commit()
            msg = "Updated :)"
            return msg
        except:
            msg = "Failed to Update :)"
            return msg

    def delete_movie(self, m_id):
        try:
            self.cur.execute("DELETE FROM movies WHERE m_id=:m_id", {
                "m_id": m_id
            })
            self.conn.commit()
            msg = "Movie Deleted"
            return msg
        except:
            msg = "Failed to Delete Movie"
            return msg

    def duplicate_entry(self, name, release_day, release_month):
        self.cur.execute("SELECT * FROM movies WHERE name=:name and release_day=:release_day and release_month=:release_month", {
            "release_day": release_day,
            "release_month": release_month,
            "name": name
        })
        rowcount = len(self.cur.fetchall())
        if rowcount == 0:
            return False
        else:
            return True
