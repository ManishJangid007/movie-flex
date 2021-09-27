import re
from database_data import DataMachine


def filter_result(movie_name, watched_status, download_status, origin, link, release_day, release_month, release_year, duplicate_check=False):
    if len(movie_name) <= 0:
        return False, "*Enter Movie Name"

    if watched_status == "Yes" or watched_status == "yes" or watched_status == "YES" or watched_status == "y" or watched_status == "Y" or watched_status == "No" or watched_status == "no" or watched_status == "NO" or watched_status == "n" or watched_status == "N":
        if watched_status == "Yes" or watched_status == "yes" or watched_status == "YES" or watched_status == "y" or watched_status == "Y":
            watched_status = "Yes"
        elif watched_status == "No" or watched_status == "no" or watched_status == "NO" or watched_status == "n" or watched_status == "N":
            watched_status = "No"
    else:
        return False, "*Tell Us Watched Status"

    if download_status == "Yes" or download_status == "yes" or download_status == "YES" or download_status == "y" or download_status == "Y" or download_status == "No" or download_status == "no" or download_status == "NO" or download_status == "n" or download_status == "N":
        if download_status == "Yes" or download_status == "yes" or download_status == "YES" or download_status == "y" or download_status == "Y":
            download_status = "Yes"
        elif download_status == "No" or download_status == "no" or download_status == "NO" or download_status == "n" or download_status == "N":
            download_status = "No"
    else:
        return False, "*Tell Us Download Status"

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
        return False, "*Enter the Origin"

    if len(link) <= 0 or link == "null" or link == "Null" or link == "NULL" or link == "Not Available" or link == "not available" or link == "NOT AVAILABLE":
        link = "Not Available"

    if re.findall("[a-zA-Z]", release_day) or len(release_day) <= 0:
        return False, "*Enter Day of Release"

    if re.findall("[a-zA-Z]", release_month) or len(release_month) <= 0:
        return False, "*Enter Month of Release"

    if re.findall("[a-zA-Z]", release_year) or len(release_year) <= 3:
        return False, "*Enter Year of Release"

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
                return False, "*Enter Day of Release"
        else:
            return False, "*Enter Month of Release"
    else:
        return False, "*Enter Year of Release"

    if duplicate_check:
        if DataMachine().duplicate_entry(movie_name, release_day, release_month):
            return False, "*Duplicate Entry"

    return True, watched_status, download_status, origin, link
