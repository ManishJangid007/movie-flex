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

if len(movie_name) <= 0:
    messageLabel.config(text="*Enter Movie Name", fg=error_color)
    messageLabel.place(x=600, y=546)
    return

if watched_status == "Yes" or watched_status == "yes" or watched_status == "YES" or watched_status == "y" or watched_status == "Y" or watched_status == "No" or watched_status == "no" or watched_status == "NO" or watched_status == "n" or watched_status == "N":
    if watched_status == "Yes" or watched_status == "yes" or watched_status == "YES" or watched_status == "y" or watched_status == "Y":
        watched_status = "Yes"
    elif watched_status == "No" or watched_status == "no" or watched_status == "NO" or watched_status == "n" or watched_status == "N":
        watched_status = "No"
else:
    messageLabel.config(text="*Tell Us Watched Status", fg=error_color)
    messageLabel.place(x=580, y=546)
    return

if download_status == "Yes" or download_status == "yes" or download_status == "YES" or download_status == "y" or download_status == "Y" or download_status == "No" or download_status == "no" or download_status == "NO" or download_status == "n" or download_status == "N":
    if download_status == "Yes" or download_status == "yes" or download_status == "YES" or download_status == "y" or download_status == "Y":
        download_status = "Yes"
    elif download_status == "No" or download_status == "no" or download_status == "NO" or download_status == "n" or download_status == "N":
        download_status = "No"
else:
    messageLabel.config(text="*Tell Us Download Status", fg=error_color)
    messageLabel.place(x=573, y=546)
    return

if origin == "Hollywood" or origin == "hollywood" or origin == "Bollywood" or origin == "bollywood" or origin == "Tollywood" or origin == "tollywood" or origin == "Other" or origin == "other":
    if origin == "hollywood":
        origin = "Hollywood"
    elif origin == "bollywood":
        origin = "Bollywood"
    elif origin == "tollywood":
        origin = "Tollywood"
    elif origin == "other":
        origin = "Other"
else:
    messageLabel.config(text="*Enter the Origin", fg=error_color)
    messageLabel.place(x=610, y=546)
    return

if len(link) <= 0 or link == "null" or link == "Null" or link == "NULL":
    link = "Not Available"

if re.findall("[a-zA-Z]", release_day) or len(release_day) <= 0:
    messageLabel.config(text="*Enter Day of Release", fg=error_color)
    messageLabel.place(x=590, y=546)
    return

if re.findall("[a-zA-Z]", release_month) or len(release_month) <= 0:
    messageLabel.config(text="*Enter Month of Release", fg=error_color)
    messageLabel.place(x=580, y=546)
    return

if re.findall("[a-zA-Z]", release_year) or len(release_year) <= 3:
    messageLabel.config(text="*Enter Year of Release", fg=error_color)
    messageLabel.place(x=585, y=546)
    return

if len((release_year)) == 4 and int(release_year) >= 1000:
    if int(release_month) >= 1 and int(release_month) <= 12:
        max_days = 31
        if int(release_month) == 1:
            max_days = 31
        elif int(release_month) == 2:
            if (int(release_year) % 4) == 0:
                max_days = 29
            else:
                max_days = 28
        elif int(release_month) == 3:
            max_days = 31
        elif int(release_month) == 4:
            max_days = 30
        elif int(release_month) == 5:
            max_days = 31
        elif int(release_month) == 6:
            max_days = 30
        elif int(release_month) == 7:
            max_days = 31
        elif int(release_month) == 8:
            max_days = 31
        elif int(release_month) == 9:
            max_days = 30
        elif int(release_month) == 10:
            max_days = 31
        elif int(release_month) == 11:
            max_days = 30
        elif int(release_month) == 12:
            max_days = 31

        if int(release_day) >= 1 and int(release_day) <= max_days:
            pass
        else:
            messageLabel.config(text="*Enter Day of Release", fg=error_color)
            messageLabel.place(x=590, y=546)
            return
    else:
        messageLabel.config(text="*Enter Month of Release", fg=error_color)
        messageLabel.place(x=580, y=546)
        return
else:
    messageLabel.config(text="*Enter Year of Release", fg=error_color)
    messageLabel.place(x=585, y=546)
    return

if DataMachine().duplicate_entry(movie_name, release_day, release_month) == True:
    messageLabel.config(text="*Duplicate Entry", fg=error_color)
    messageLabel.place(x=615, y=546)
    return