import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from database_data import DataMachine
from datetime import date
import DashboardData
from monthSrtring import month_string
from filter import filter_result

root = Tk()
root.title("Movie Flex")
root.geometry("1170x670")
root.resizable(False, False)

# Colors
backgroundColor = "#ffffff"
orange = "#f47754"
light_orange = "#fab5a1"
blue = "#3babdc"
purple = "#8a65ab"
pink = "#d565a6"
red_light = "#f26f72"
red_dark = "#ea3b4c"
grey_font = "#d3d3d3"
yellow_light = "#e8bd73"
yellow_dark = "#eab957"

# Font
font = "Bahnschrift"
font_color = "#ffffff"
font_darkcolor = "#4c4c4d"
input_font_color = "#1e1e1e"
error_color = "#ff1f1f"
black_font = "#231f20"

# Pngs
backgroundPng = ImageTk.PhotoImage(Image.open("assets/background.png"))
menuPanelPng = ImageTk.PhotoImage(Image.open("assets/menuPanel.png"))
hollywoodButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/hollywood.png"))
tollywoodButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/tollywood.png"))
bollywoodButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/bollywood.png"))
othersButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/other.png"))
addMovieButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/addmovie.png"))
unwatchedButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/unwatched.png"))
watchedButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/watched.png"))
toDownloadButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/toDownload.png"))
downloadedButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/downloaded.png"))
dashBoardButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/dashboard.png"))
allMovieButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/allMovies.png"))
movieFlexLabelPng = ImageTk.PhotoImage(Image.open("assets/movieFlexLabel.png"))
mfLogoPng = ImageTk.PhotoImage(Image.open("assets/mflogo.png"))
addPanelPng = ImageTk.PhotoImage(Image.open("assets/addpanel.png"))
addButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/addButton.png"))

dashBoardPanelPng = ImageTk.PhotoImage(Image.open("assets/dashboardPanel.png"))
unwatchedPanelPng = ImageTk.PhotoImage(Image.open("assets/unwatchedPanel.png"))
toDownloadPanelPng = ImageTk.PhotoImage(Image.open("assets/toDownload.png"))
watchedPanelPng = ImageTk.PhotoImage(Image.open("assets/watchedPanel.png"))
downloadedPanelPng = ImageTk.PhotoImage(Image.open("assets/downloadedPanel.png"))
allMoviePanelPng = ImageTk.PhotoImage(Image.open("assets/allmoviesPanel.png"))
hollywoodPanelPng = ImageTk.PhotoImage(Image.open("assets/hollywoodPanel.png"))
bollywoodPanelPng = ImageTk.PhotoImage(Image.open("assets/bollywoodPanel.png"))
tollywoodPanelPng = ImageTk.PhotoImage(Image.open("assets/tollywoodPanel.png"))
otherPanelPng = ImageTk.PhotoImage(Image.open("assets/othersPanel.png"))

nextButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/next.png"))
backButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/backButton.png"))
editButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/editButton.png"))

editPagePng = ImageTk.PhotoImage(Image.open("assets/editPanelPng.png"))
updateButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/updateButtonPng.png"))
cancelButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/cancel.png"))
deleteButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/deleteButton.png"))

nextDarkButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/next_with_dark.png"))
backDarkButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/back_with_dark.png"))
editDarkButtonPng = ImageTk.PhotoImage(Image.open("assets/buttons/edit_dark_button.png"))

background = Label(root, bd=0, image=backgroundPng)
background.place(x=0, y=0)

# DashBoard Panel


def dashboard_panel_func(date=date):
    global dashboardPanelFrame
    dashboardPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    dashboardPanelFrame.place(x=310, y=2)

    dashboardPanel = Label(dashboardPanelFrame, bd=0, bg=backgroundColor, image=dashBoardPanelPng)
    dashboardPanel.place(x=-217, y=11)

    unwatchedMoviesLabel = Label(dashboardPanelFrame, text="Unwatched Movies", bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"))
    unwatchedMoviesLabel.place(x=85, y=239)
    unwatchedMoviesEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=pink, fg=font_color, font=(font, 20, "normal"), justify="center")
    unwatchedMoviesEntry.place(x=337, y=240.3)
    unwatchedMoviesEntry.insert(0, DashboardData.total_unwatched_movies())

    moviestodownloadLabel = Label(dashboardPanelFrame, text="Movies to Download", bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"))
    moviestodownloadLabel.place(x=85, y=349)
    moviestodownloadEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=pink, fg=font_color, font=(font, 20, "normal"), justify="center")
    moviestodownloadEntry.place(x=355, y=350.6)
    moviestodownloadEntry.insert(0, DashboardData.total_undownloaded_movies())

    watchedmoviesLabel = Label(dashboardPanelFrame, text="Watched Movies", bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"))
    watchedmoviesLabel.place(x=85, y=459)
    watchedmoviesEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=pink, fg=font_color, font=(font, 20, "normal"), justify="center")
    watchedmoviesEntry.place(x=314, y=461.3)
    watchedmoviesEntry.insert(0, DashboardData.total_watched_movies())

    downloadedmoviesLabel = Label(dashboardPanelFrame, text="Downloaded Movies", bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"))
    downloadedmoviesLabel.place(x=85, y=569)
    downloadedmoviesEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=pink, fg=font_color, font=(font, 20, "normal"), justify="center")
    downloadedmoviesEntry.place(x=357, y=572)
    downloadedmoviesEntry.insert(0, DashboardData.total_downloaded_movies())

    raw_date = str(date.today())
    date = raw_date.split("-")
    day = date[2]
    month = date[1]
    year = date[0]

    dayLabel = Label(dashboardPanelFrame, text=day, bd=0, bg=pink, fg=font_darkcolor, font=(font, 18, "bold"))
    dayLabel.place(x=550, y=63)

    monthLabel = Label(dashboardPanelFrame, text=month, bd=0, bg=pink, fg=font_darkcolor, font=(font, 18, "bold"))
    monthLabel.place(x=755, y=63)

    yearLabel = Label(dashboardPanelFrame, text=year, bd=0, bg=pink, fg=font_darkcolor, font=(font, 18, "bold"))
    yearLabel.place(x=648, y=322)

    totalLabel = Label(dashboardPanelFrame, text="Total", bd=0, bg=pink, fg=font_color, font=(font, 18, "normal"))
    totalLabel.place(x=640, y=115)

    totalMoviesEntry = Entry(dashboardPanelFrame, width=8, bd=0, bg=pink, fg=font_color, font=(font, 30, "normal"), justify="center")
    totalMoviesEntry.place(x=578, y=160)
    totalMoviesEntry.insert(0, DashboardData.total_movies())

    moviesLabel = Label(dashboardPanelFrame, text="Movies", bd=0, bg=pink, fg=font_color, font=(font, 18, "normal"))
    moviesLabel.place(x=628, y=225)

    hollywoodLabel = Label(dashboardPanelFrame, text="Hollywood", bd=0, bg=pink, fg=font_color, font=(font, 16, "normal"))
    hollywoodLabel.place(x=680, y=393)
    hollywoodEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"), justify="center")
    hollywoodEntry.place(x=557, y=390.3)
    hollywoodEntry.insert(0, DashboardData.total_hollywood_movies())

    bollywoodLabel = Label(dashboardPanelFrame, text="Bollywood", bd=0, bg=pink, fg=font_color, font=(font, 16, "normal"))
    bollywoodLabel.place(x=549, y=448)
    bollywoodEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"), justify="center")
    bollywoodEntry.place(x=678, y=445.5)
    bollywoodEntry.insert(0, DashboardData.total_bollywood_movies())

    tollwoodLabel = Label(dashboardPanelFrame, text="Tollywood", bd=0, bg=pink, fg=font_color, font=(font, 16, "normal"))
    tollwoodLabel.place(x=680, y=503)
    tollwoodEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"), justify="center")
    tollwoodEntry.place(x=557, y=500.5)
    tollwoodEntry.insert(0, DashboardData.total_tollywood_movies())

    otherLabel = Label(dashboardPanelFrame, text="Other", bd=0, bg=pink, fg=font_color, font=(font, 16, "normal"))
    otherLabel.place(x=588, y=557)
    otherEntry = Entry(dashboardPanelFrame, width=6, bd=0, bg=purple, fg=font_color, font=(font, 20, "normal"), justify="center")
    otherEntry.place(x=676, y=555.8)
    otherEntry.insert(0, DashboardData.total_other_movies())

# Add Movie Panel


def add_panel_func():
    global addPanelFrame
    addPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    addPanelFrame.place(x=310, y=2)

    addPanel = Label(addPanelFrame, bd=0, bg=backgroundColor, image=addPanelPng)
    addPanel.place(x=-100, y=11)

    nameLabel = Label(addPanelFrame, text="Name", bd=0, bg=orange, fg=font_color, font=(font, 22, "normal"))
    nameLabel.place(x=90, y=114)

    nameEntry = Entry(addPanelFrame, width=16, bd=0, bg=light_orange, fg=input_font_color, font=(font, 22, "normal"),
                      justify="center")
    nameEntry.place(x=193, y=116)

    watchedornotLabel = Label(addPanelFrame, text="Watched or Not", bd=0, bg=orange, fg=font_color,
                              font=(font, 22, "normal"))
    watchedornotLabel.place(x=90, y=217)

    watchedornotEntry = Entry(addPanelFrame, width=6, bd=0, bg=light_orange, fg=input_font_color,
                              font=(font, 22, "normal"), justify="center")
    watchedornotEntry.place(x=319, y=220)

    yesnoLabel0 = Label(addPanelFrame, text="Yes / No", bd=0, bg=orange, fg=font_color, font=(font, 11, "normal"))
    yesnoLabel0.place(x=339, y=263)

    downloadedornotLabel = Label(addPanelFrame, text="Downloaded or Not", bd=0, bg=orange, fg=font_color,
                                 font=(font, 22, "normal"))
    downloadedornotLabel.place(x=90, y=323)

    downloadedornotEntry = Entry(addPanelFrame, width=6, bd=0, bg=light_orange, fg=input_font_color,
                                 font=(font, 22, "normal"), justify="center")
    downloadedornotEntry.place(x=368.3, y=326)

    yesnoLabel1 = Label(addPanelFrame, text="Yes / No", bd=0, bg=orange, fg=font_color, font=(font, 11, "normal"))
    yesnoLabel1.place(x=388, y=369)

    originLabel = Label(addPanelFrame, text="Origin", bd=0, bg=orange, fg=font_color, font=(font, 22, "normal"))
    originLabel.place(x=90, y=430)

    originEntry = Entry(addPanelFrame, width=16, bd=0, bg=light_orange, fg=input_font_color, font=(font, 22, "normal"),
                        justify="center")
    originEntry.place(x=199.5, y=432)

    originOptionLabel = Label(addPanelFrame, text="Options :- Hollywood / Bollywood / Tollywood / Other", bd=0,
                              bg=orange, fg=font_color, font=(font, 11, "normal"))
    originOptionLabel.place(x=110, y=475)

    sourcelinkLabel = Label(addPanelFrame, text="Source / Link", bd=0, bg=orange, fg=font_color,
                            font=(font, 22, "normal"))
    sourcelinkLabel.place(x=90, y=535)

    sourcelinkEntry = Entry(addPanelFrame, width=10, bd=0, bg=light_orange, fg=input_font_color,
                            font=(font, 22, "normal"), justify="center")
    sourcelinkEntry.place(x=297.5, y=538)
    sourcelinkEntry.insert(0, "Null")

    optionalLabel = Label(addPanelFrame, text="*Optional", bd=0, bg=orange, fg=font_color, font=(font, 11, "normal"))
    optionalLabel.place(x=342, y=580)

    dayLabel = Label(addPanelFrame, text="Day", bd=0, bg=orange, fg=font_color, font=(font, 22, "normal"))
    dayLabel.place(x=599, y=169)

    dayEntry = Entry(addPanelFrame, width=6, bd=0, bg=light_orange, fg=input_font_color, font=(font, 22, "normal"),
                     justify="center")
    dayEntry.place(x=677, y=172)
    dayEntry.insert(0, "00")

    monthLabel = Label(addPanelFrame, text="Month", bd=0, bg=orange, fg=font_color, font=(font, 22, "normal"))
    monthLabel.place(x=580, y=259)

    monthEntry = Entry(addPanelFrame, width=6, bd=0, bg=light_orange, fg=input_font_color, font=(font, 22, "normal"),
                       justify="center")
    monthEntry.place(x=693, y=261)
    monthEntry.insert(0, "00")

    yearLabel = Label(addPanelFrame, text="Year", bd=0, bg=orange, fg=font_color, font=(font, 22, "normal"))
    yearLabel.place(x=590, y=346)

    yearEntry = Entry(addPanelFrame, width=6, bd=0, bg=light_orange, fg=input_font_color, font=(font, 22, "normal"),
                      justify="center")
    yearEntry.place(x=680, y=348)
    yearEntry.insert(0, "0000")

    messageLabel = Label(addPanelFrame, text="Message", bd=0, bg=blue, fg=font_color, font=(font, 15, "normal"))
    messageLabel.place(x=650, y=546)

    def add_movies_func():
        movie_name = nameEntry.get()
        watched_status = watchedornotEntry.get()
        download_status = downloadedornotEntry.get()
        origin = originEntry.get()
        link = sourcelinkEntry.get()
        release_day = dayEntry.get()
        release_month = monthEntry.get()
        release_year = yearEntry.get()

        messageLabel.config(text="Message", fg=font_color)
        messageLabel.place(x=650, y=546)

        filtered_data = filter_result(movie_name, watched_status, download_status, origin, link, release_day, release_month, release_year, duplicate_check=True)

        if filtered_data[0]:
            try:
                DataMachine().add_movie(movie_name, release_day, release_month, release_year, filtered_data[1], filtered_data[2], filtered_data[4], filtered_data[3])
                messageLabel.config(text="Added Successfully", fg=font_color)
                messageLabel.place(x=600, y=546)

                nameEntry.delete(0, END)
                watchedornotEntry.delete(0, END)
                downloadedornotEntry.delete(0, END)
                originEntry.delete(0, END)
                sourcelinkEntry.delete(0, END)
                sourcelinkEntry.insert(0, "Null")
                dayEntry.delete(0, END)
                dayEntry.insert(0, "00")
                monthEntry.delete(0, END)
                monthEntry.insert(0, "00")
                yearEntry.delete(0, END)
                yearEntry.insert(0, "0000")
                return
            except:
                messageLabel.config(text="Failed", fg=error_color)
                messageLabel.place(x=650, y=546)
                return

        else:
            messageLabel.config(text=filtered_data[1], fg=error_color)
            messageLabel.place(x=573, y=546)

    addButton = Button(addPanelFrame, bd=0, bg=light_orange, activebackground=light_orange, image=addButtonPng, command=add_movies_func)
    addButton.place(x=634, y=468)

# Edit Page


def edit_page(frame, m_id):
    edit_page_frame = LabelFrame(frame, bd=0, bg=backgroundColor, width=865, height=665)
    edit_page_frame.place(x=0, y=0)

    conn = sqlite3.connect("movies_data.db")
    cur = conn.cursor()
    cur.execute("select * from movies where m_id=:m_id", {
        "m_id": m_id
    })
    data = cur.fetchall()

    current_movie = 0
    movie_name = 1
    release_day = 2
    release_month = 3
    release_year = 4
    watched_status = 5
    download_status = 6
    link = 7
    origin = 8

    editPage = Label(edit_page_frame, bd=0, bg=backgroundColor, image=editPagePng)
    editPage.place(x=-22, y=15)

    nameLabel = Label(edit_page_frame, text="Name", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    nameLabel.place(x=50, y=48)
    nameEntry = Entry(edit_page_frame, bd=0, width=16, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    nameEntry.place(x=178, y=50)
    nameEntry.insert(0, data[current_movie][movie_name])

    originLabel = Label(edit_page_frame, text="Origin", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    originLabel.place(x=50, y=120)
    originEntry = Entry(edit_page_frame, bd=0, width=16, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    originEntry.place(x=178, y=124)
    originEntry.insert(0, data[current_movie][origin])

    releaseDayLabel = Label(edit_page_frame, text="Release Day", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    releaseDayLabel.place(x=50, y=195)
    releaseDayEntry = Entry(edit_page_frame, bd=0, width=10, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    releaseDayEntry.place(x=281, y=200)
    releaseDayEntry.insert(0, data[current_movie][release_day])

    releaseMonthLabel = Label(edit_page_frame, text="Release Month", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    releaseMonthLabel.place(x=50, y=272)
    releaseMonthEntry = Entry(edit_page_frame, bd=0, width=8, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    releaseMonthEntry.place(x=319, y=275)
    releaseMonthEntry.insert(0, data[current_movie][release_month])

    releaseYearLabel = Label(edit_page_frame, text="Release Year", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    releaseYearLabel.place(x=50, y=349)
    releaseYearEntry = Entry(edit_page_frame, bd=0, width=10, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    releaseYearEntry.place(x=287, y=350)
    releaseYearEntry.insert(0, data[current_movie][release_year])

    linkLabel = Label(edit_page_frame, text="Link", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    linkLabel.place(x=50, y=426)
    linkEntry = Entry(edit_page_frame, bd=0, width=17, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    linkEntry.place(x=157, y=425)
    linkEntry.insert(0, data[current_movie][link])

    watchedLabel = Label(edit_page_frame, text="Watched", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    watchedLabel.place(x=560, y=52)
    watchedEntry = Entry(edit_page_frame, bd=0, width=5, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    watchedEntry.place(x=730, y=54)
    watchedEntry.insert(0, data[current_movie][watched_status])

    downloadedLabel = Label(edit_page_frame, text="Downloaded", bd=0, bg=yellow_dark, fg=black_font, font=(font, 25, "normal"))
    downloadedLabel.place(x=503, y=121)
    downloadedEntry = Entry(edit_page_frame, bd=0, width=5, bg=yellow_light, fg=black_font, font=(font, 25, "normal"), justify="center")
    downloadedEntry.place(x=730, y=124)
    downloadedEntry.insert(0, data[current_movie][download_status])

    messageLabel = Label(edit_page_frame, text="Message", bd=0, bg=yellow_light, fg=black_font, font=(font, 18, "normal"))
    messageLabel.place(x=615, y=235)

    def delete_button_func():
        DataMachine().delete_movie(m_id)
        edit_page_frame.destroy()
        frame.destroy()
        dashboard_panel_func()

    deleteButton = Button(edit_page_frame, bd=0, bg=yellow_dark, activebackground=yellow_dark, image=deleteButtonPng, command=delete_button_func)
    deleteButton.place(x=595, y=380)

    def update_button_func():
        messageLabel.config(text="Message", fg=black_font)
        messageLabel.place(x=615, y=235)
        filter_data = filter_result(nameEntry.get(), watchedEntry.get(), downloadedEntry.get(), originEntry.get(), linkEntry.get(), releaseDayEntry.get(), releaseMonthEntry.get(), releaseYearEntry.get())
        if filter_data[0]:
            DataMachine().update_name(m_id, nameEntry.get())
            DataMachine().update_origin(m_id, filter_data[3])
            DataMachine().update_release_date(m_id, releaseDayEntry.get(), releaseMonthEntry.get(), releaseYearEntry.get())
            DataMachine().update_link(m_id, filter_data[4])
            DataMachine().update_wuw_status(m_id, filter_data[1])
            DataMachine().update_download_status(m_id, filter_data[2])
            edit_page_frame.destroy()
            frame.destroy()
            dashboard_panel_func()
        else:
            messageLabel.config(text=filter_data[1], fg=error_color)
            messageLabel.place(x=540, y=235)

    updateButton = Button(edit_page_frame, bd=0, bg=yellow_light, activebackground=yellow_light, image=updateButtonPng, command=update_button_func)
    updateButton.place(x=280, y=550)

    def cancel_button_func():
        edit_page_frame.destroy()

    cancelButton = Button(edit_page_frame, bd=0, bg=yellow_light, activebackground=yellow_light, image=cancelButtonPng, command=cancel_button_func)
    cancelButton.place(x=460, y=550)

# Unwatched Panel


def unwatched_panel_func():
    global unwatchedPanelFrame
    unwatchedPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    unwatchedPanelFrame.place(x=310, y=2)

    unwatchedPanel = Label(unwatchedPanelFrame, bd=0, bg=backgroundColor, image=unwatchedPanelPng)
    unwatchedPanel.place(x=-22, y=15)

    conn = sqlite3.connect("movies_data.db")
    cur = conn.cursor()
    cur.execute("select * from movies where wuw_status = 'No'")
    global data
    data = cur.fetchall()
    rowcount = len(data)
    conn.close()

    if rowcount == 0:
        smily = Label(unwatchedPanelFrame, text="Nothing Found :)", bd=0, bg=red_light, fg=font_color, font=(font, 30, "normal"))
        smily.place(x=280, y=250)

        emptyLabel = Label(unwatchedPanelFrame, text="It's Empty Here !", bd=0, bg=red_dark, fg=font_color,
                      font=(font, 20, "normal"))
        emptyLabel.place(x=330, y=550)
        return

    # data[<row>][<column>]

    global maxLength
    maxLength = rowcount - 1
    global current_movie
    current_movie = 0
    global next_movie
    next_movie = current_movie + 1
    global movieName
    movieName = 1
    global release_day
    release_day = 2
    global release_month
    release_month = 3
    global release_year
    release_year = 4
    global download_status
    download_status = 6
    global link
    link = 7
    global origin
    origin = 8

    movieLabel = Label(unwatchedPanelFrame, text=data[current_movie][movieName], bd=0, bg=red_light, fg=font_color, font=(font, 35, 'normal'))
    movieLabel.place(x=78, y=100)

    originLabel = Label(unwatchedPanelFrame, text="Origin : " + data[current_movie][origin], bd=0, bg=red_light, fg=font_color, font=(font, 30, 'normal'))
    originLabel.place(x=110, y=175)

    releaseDateLabel = Label(unwatchedPanelFrame,
                             text="Release Date : " + str(data[current_movie][release_day]) + " " + month_string(str(data[current_movie][release_month])) + " " + str(data[current_movie][release_year]),
                             bd=0, bg=red_light,
                             fg=font_color,
                             font=(font, 30, 'normal'))
    releaseDateLabel.place(x=110, y=235)


    downloadStatusLabel = Label(unwatchedPanelFrame, text="Downloaded : " + data[current_movie][download_status], bd=0, bg=red_light, fg=font_color, font=(font, 30, 'normal'))
    downloadStatusLabel.place(x=110, y=290)

    linkLabel = Label(unwatchedPanelFrame, text="Link : ", bd=0, bg=red_light, fg=font_color, font=(font, 30, 'normal'))
    linkLabel.place(x=110, y=350)

    linkEntry = Entry(unwatchedPanelFrame, bd=0, bg=red_light, width=25, fg=font_color, font=(font, 30, 'normal'), justify="left")
    linkEntry.place(x=220, y=350)
    linkEntry.insert(0, data[current_movie][link])

    counterEntry = Entry(unwatchedPanelFrame, bd=0, bg=red_light, width=10, fg=font_color, font=(font, 35, 'normal'), justify="right")
    counterEntry.place(x=560, y=450)
    counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

    upNextLabel = Label(unwatchedPanelFrame, text="Up Next", bd=0, bg=red_dark, fg=font_color, font=(font, 20, 'normal'))
    upNextLabel.place(x=78, y=530)

    try:
        nextMovieLabel = Label(unwatchedPanelFrame, text=data[next_movie][movieName], bd=0, bg=red_dark, fg=grey_font,
                               font=(font, 16, 'normal'))
        nextMovieLabel.place(x=97, y=575)

        nextMovieYearLabel = Label(unwatchedPanelFrame, text=data[next_movie][release_year], bd=0, bg=red_dark,
                                   fg=grey_font, font=(font, 16, 'normal'))
        nextMovieYearLabel.place(x=97, y=610)
    except:
        pass

    def back_button_func():
        global data
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global download_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie > 0:
                current_movie -= 1
                movieLabel.config(text=data[current_movie][movieName])
                originLabel.config(text="Origin : " + data[current_movie][origin])
                releaseDateLabel.config(text="Release Date : " + str(data[current_movie][release_day]) + " " + month_string(
                    str(data[current_movie][release_month])) + " " + str(data[current_movie][release_year]))
                downloadStatusLabel.config(text="Downloaded : " + data[current_movie][download_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie > 1:
                next_movie -= 1
                nextMovieLabel.config(text=data[next_movie][movieName])
                nextMovieYearLabel.config(text=data[next_movie][release_year])

    backButtonFrame = LabelFrame(unwatchedPanelFrame, bd=0, height=50, width=100, bg=red_dark)
    backButtonFrame.place(x=590, y=565)
    backButton = Button(backButtonFrame, bd=0, bg=red_dark, activebackground=red_dark, image=backButtonPng, command=back_button_func)
    backButton.place(x=0, y=0)

    def next_button_func():
        global data
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global download_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie < maxLength:
                current_movie += 1
                movieLabel.config(text=data[current_movie][movieName])
                originLabel.config(text="Origin : " + data[current_movie][origin])
                releaseDateLabel.config(text="Release Date : " + str(data[current_movie][release_day]) + " " + month_string(str(data[current_movie][release_month])) + " " + str(data[current_movie][release_year]))
                downloadStatusLabel.config(text="Downloaded : " + data[current_movie][download_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie < maxLength:
                next_movie += 1
                nextMovieLabel.config(text=data[next_movie][movieName])
                nextMovieYearLabel.config(text=data[next_movie][release_year])
            else:
                nextMovieLabel.config(text="Finished !")
                nextMovieYearLabel.config(text="")


    nextButtonFrame = LabelFrame(unwatchedPanelFrame, bd=0, height=50, width=100, bg=red_dark)
    nextButtonFrame.place(x=710, y=565)
    nextButton = Button(nextButtonFrame, bd=0, bg=red_dark, activebackground=red_dark, image=nextButtonPng, command=next_button_func)
    nextButton.place(x=0, y=0)

    def edit_button_func():
        edit_page(unwatchedPanelFrame, data[current_movie][0])

    editButton = Button(unwatchedPanelFrame, bd=0, bg=red_light, activebackground=red_light, image=editButtonPng, command=edit_button_func)
    editButton.place(x=710, y=35)

# To Download Panel


def todownload_panel_func():
    global todownloadPanelFrame
    todownloadPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    todownloadPanelFrame.place(x=310, y=2)

    todownloadPanel = Label(todownloadPanelFrame, bd=0, bg=backgroundColor, image=toDownloadPanelPng)
    todownloadPanel.place(x=-22, y=15)

    conn = sqlite3.connect("movies_data.db")
    cur = conn.cursor()
    cur.execute("select * from movies where download_status = 'No'")
    global data2
    data2 = cur.fetchall()
    rowcount = len(data2)
    conn.close()

    if rowcount == 0:
        smily = Label(todownloadPanelFrame, text="Nothing Found :)", bd=0, bg=yellow_dark, fg=black_font, font=(font, 30, "normal"))
        smily.place(x=280, y=250)

        emptyLabel = Label(todownloadPanelFrame, text="It's Empty Here !", bd=0, bg=yellow_light, fg=black_font,
                      font=(font, 20, "normal"))
        emptyLabel.place(x=330, y=550)
        return

    # data[<row>][<column>]

    global maxLength
    maxLength = rowcount - 1
    global current_movie
    current_movie = 0
    global next_movie
    next_movie = current_movie + 1
    global movieName
    movieName = 1
    global release_day
    release_day = 2
    global release_month
    release_month = 3
    global release_year
    release_year = 4
    global watched_status
    watched_status = 5
    global link
    link = 7
    global origin
    origin = 8

    movieLabel = Label(todownloadPanelFrame, text=data2[current_movie][movieName], bd=0, bg=yellow_dark, fg=black_font,
                           font=(font, 35, 'normal'))
    movieLabel.place(x=78, y=100)

    originLabel = Label(todownloadPanelFrame, text="Origin : " + data2[current_movie][origin], bd=0, bg=yellow_dark,
                            fg=black_font, font=(font, 30, 'normal'))
    originLabel.place(x=110, y=175)

    releaseDateLabel = Label(todownloadPanelFrame,
                                text="Release Date : " + str(data2[current_movie][release_day]) + " " + month_string(
                                str(data2[current_movie][release_month])) + " " + str(
                                data2[current_movie][release_year]),
                                bd=0, bg=yellow_dark,
                                fg=black_font,
                                font=(font, 30, 'normal'))
    releaseDateLabel.place(x=110, y=235)

    watchedStatusLabel = Label(todownloadPanelFrame, text="Watched : " + data2[current_movie][watched_status],
                                    bd=0, bg=yellow_dark, fg=black_font, font=(font, 30, 'normal'))
    watchedStatusLabel.place(x=110, y=290)

    linkLabel = Label(todownloadPanelFrame, text="Link : ", bd=0, bg=yellow_dark, fg=black_font,
                          font=(font, 30, 'normal'))
    linkLabel.place(x=110, y=350)

    linkEntry = Entry(todownloadPanelFrame, bd=0, bg=yellow_dark, width=25, fg=black_font, font=(font, 30, 'normal'),
                          justify="left")
    linkEntry.place(x=220, y=350)
    linkEntry.insert(0, data2[current_movie][link])

    counterEntry = Entry(todownloadPanelFrame, bd=0, bg=yellow_dark, width=10, fg=black_font, font=(font, 35, 'normal'),
                             justify="right")
    counterEntry.place(x=560, y=450)
    counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

    upNextLabel = Label(todownloadPanelFrame, text="Up Next", bd=0, bg=yellow_light, fg=black_font,
                            font=(font, 20, 'normal'))
    upNextLabel.place(x=78, y=530)

    try:
        nextMovieLabel = Label(todownloadPanelFrame, text=data2[next_movie][movieName], bd=0, bg=yellow_light,
                                fg=font_darkcolor,
                                font=(font, 16, 'normal'))
        nextMovieLabel.place(x=97, y=575)

        nextMovieYearLabel = Label(todownloadPanelFrame, text=data2[next_movie][release_year], bd=0, bg=yellow_light,
                                   fg=font_darkcolor, font=(font, 16, 'normal'))
        nextMovieYearLabel.place(x=97, y=610)
    except:
        pass

    def back_button_func():
        global data2
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global watched_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie > 0:
                current_movie -= 1
                movieLabel.config(text=data2[current_movie][movieName])
                originLabel.config(text="Origin : " + data2[current_movie][origin])
                releaseDateLabel.config(
                    text="Release Date : " + str(data2[current_movie][release_day]) + " " + month_string(
                    str(data2[current_movie][release_month])) + " " + str(data2[current_movie][release_year]))
                watchedStatusLabel.config(text="Watched : " + data2[current_movie][watched_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data2[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie > 1:
                next_movie -= 1
                nextMovieLabel.config(text=data2[next_movie][movieName])
                nextMovieYearLabel.config(text=data2[next_movie][release_year])

    backButtonFrame = LabelFrame(todownloadPanelFrame, bd=0, height=50, width=100, bg=yellow_light)
    backButtonFrame.place(x=590, y=565)
    backButton = Button(backButtonFrame, bd=0, bg=yellow_light, activebackground=yellow_light, image=backDarkButtonPng,
                        command=back_button_func)
    backButton.place(x=0, y=0)

    def next_button_func():
        global data2
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global watched_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie < maxLength:
                current_movie += 1
                movieLabel.config(text=data2[current_movie][movieName])
                originLabel.config(text="Origin : " + data2[current_movie][origin])
                releaseDateLabel.config(
                    text="Release Date : " + str(data2[current_movie][release_day]) + " " + month_string(
                        str(data2[current_movie][release_month])) + " " + str(data2[current_movie][release_year]))
                watchedStatusLabel.config(text="Watched : " + data2[current_movie][watched_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data2[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie < maxLength:
                next_movie += 1
                nextMovieLabel.config(text=data2[next_movie][movieName])
                nextMovieYearLabel.config(text=data2[next_movie][release_year])
            else:
                nextMovieLabel.config(text="Finished !")
                nextMovieYearLabel.config(text="")

    nextButtonFrame = LabelFrame(todownloadPanelFrame, bd=0, height=50, width=100, bg=yellow_light)
    nextButtonFrame.place(x=710, y=565)
    nextButton = Button(nextButtonFrame, bd=0, bg=yellow_light, activebackground=yellow_light, image=nextDarkButtonPng,
                            command=next_button_func)
    nextButton.place(x=0, y=0)

    def edit_button_func():
        edit_page(todownloadPanelFrame, data2[current_movie][0])

    editButton = Button(todownloadPanelFrame, bd=0, bg=yellow_dark, activebackground=yellow_dark, image=editDarkButtonPng,
                        command=edit_button_func)
    editButton.place(x=710, y=35)


# Watched Panel


def watched_panel_func():
    global watchedPanelFrame
    watchedPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    watchedPanelFrame.place(x=310, y=2)

    watchedPanel = Label(watchedPanelFrame, bd=0, bg=backgroundColor, image=watchedPanelPng)
    watchedPanel.place(x=-22, y=15)

    conn = sqlite3.connect("movies_data.db")
    cur = conn.cursor()
    cur.execute("select * from movies where wuw_status = 'Yes'")
    global data3
    data3 = cur.fetchall()
    rowcount = len(data3)
    conn.close()

    if rowcount == 0:
        smily = Label(watchedPanelFrame, text="Nothing Found :)", bd=0, bg=red_light, fg=font_color, font=(font, 30, "normal"))
        smily.place(x=280, y=250)

        emptyLabel = Label(watchedPanelFrame, text="It's Empty Here !", bd=0, bg=red_dark, fg=font_color,
                      font=(font, 20, "normal"))
        emptyLabel.place(x=330, y=550)
        return

    # data[<row>][<column>]

    global maxLength
    maxLength = rowcount - 1
    global current_movie
    current_movie = 0
    global next_movie
    next_movie = current_movie + 1
    global movieName
    movieName = 1
    global release_day
    release_day = 2
    global release_month
    release_month = 3
    global release_year
    release_year = 4
    global download_status
    download_status = 6
    global link
    link = 7
    global origin
    origin = 8

    movieLabel = Label(watchedPanelFrame, text=data3[current_movie][movieName], bd=0, bg=red_light, fg=font_color, font=(font, 35, 'normal'))
    movieLabel.place(x=78, y=100)

    originLabel = Label(watchedPanelFrame, text="Origin : " + data3[current_movie][origin], bd=0, bg=red_light, fg=font_color, font=(font, 30, 'normal'))
    originLabel.place(x=110, y=175)

    releaseDateLabel = Label(watchedPanelFrame,
                             text="Release Date : " + str(data3[current_movie][release_day]) + " " + month_string(str(data3[current_movie][release_month])) + " " + str(data3[current_movie][release_year]),
                             bd=0, bg=red_light,
                             fg=font_color,
                             font=(font, 30, 'normal'))
    releaseDateLabel.place(x=110, y=235)


    downloadStatusLabel = Label(watchedPanelFrame, text="Downloaded : " + data3[current_movie][download_status], bd=0, bg=red_light, fg=font_color, font=(font, 30, 'normal'))
    downloadStatusLabel.place(x=110, y=290)

    linkLabel = Label(watchedPanelFrame, text="Link : ", bd=0, bg=red_light, fg=font_color, font=(font, 30, 'normal'))
    linkLabel.place(x=110, y=350)

    linkEntry = Entry(watchedPanelFrame, bd=0, bg=red_light, width=25, fg=font_color, font=(font, 30, 'normal'), justify="left")
    linkEntry.place(x=220, y=350)
    linkEntry.insert(0, data3[current_movie][link])

    counterEntry = Entry(watchedPanelFrame, bd=0, bg=red_light, width=10, fg=font_color, font=(font, 35, 'normal'), justify="right")
    counterEntry.place(x=560, y=450)
    counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

    upNextLabel = Label(watchedPanelFrame, text="Up Next", bd=0, bg=red_dark, fg=font_color, font=(font, 20, 'normal'))
    upNextLabel.place(x=78, y=530)

    try:
        nextMovieLabel = Label(watchedPanelFrame, text=data3[next_movie][movieName], bd=0, bg=red_dark, fg=grey_font,
                               font=(font, 16, 'normal'))
        nextMovieLabel.place(x=97, y=575)

        nextMovieYearLabel = Label(watchedPanelFrame, text=data3[next_movie][release_year], bd=0, bg=red_dark,
                                   fg=grey_font, font=(font, 16, 'normal'))
        nextMovieYearLabel.place(x=97, y=610)
    except:
        pass

    def back_button_func():
        global data3
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global download_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie > 0:
                current_movie -= 1
                movieLabel.config(text=data3[current_movie][movieName])
                originLabel.config(text="Origin : " + data3[current_movie][origin])
                releaseDateLabel.config(text="Release Date : " + str(data3[current_movie][release_day]) + " " + month_string(
                    str(data3[current_movie][release_month])) + " " + str(data3[current_movie][release_year]))
                downloadStatusLabel.config(text="Downloaded : " + data3[current_movie][download_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data3[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie > 1:
                next_movie -= 1
                nextMovieLabel.config(text=data3[next_movie][movieName])
                nextMovieYearLabel.config(text=data3[next_movie][release_year])

    backButtonFrame = LabelFrame(watchedPanelFrame, bd=0, height=50, width=100, bg=red_dark)
    backButtonFrame.place(x=590, y=565)
    backButton = Button(backButtonFrame, bd=0, bg=red_dark, activebackground=red_dark, image=backButtonPng, command=back_button_func)
    backButton.place(x=0, y=0)

    def next_button_func():
        global data3
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global download_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie < maxLength:
                current_movie += 1
                movieLabel.config(text=data3[current_movie][movieName])
                originLabel.config(text="Origin : " + data3[current_movie][origin])
                releaseDateLabel.config(text="Release Date : " + str(data3[current_movie][release_day]) + " " + month_string(str(data3[current_movie][release_month])) + " " + str(data3[current_movie][release_year]))
                downloadStatusLabel.config(text="Downloaded : " + data3[current_movie][download_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data3[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie < maxLength:
                next_movie += 1
                nextMovieLabel.config(text=data3[next_movie][movieName])
                nextMovieYearLabel.config(text=data3[next_movie][release_year])
            else:
                nextMovieLabel.config(text="Finished !")
                nextMovieYearLabel.config(text="")


    nextButtonFrame = LabelFrame(watchedPanelFrame, bd=0, height=50, width=100, bg=red_dark)
    nextButtonFrame.place(x=710, y=565)
    nextButton = Button(nextButtonFrame, bd=0, bg=red_dark, activebackground=red_dark, image=nextButtonPng, command=next_button_func)
    nextButton.place(x=0, y=0)

    def edit_button_func():
        edit_page(watchedPanelFrame, data3[current_movie][0])

    editButton = Button(watchedPanelFrame, bd=0, bg=red_light, activebackground=red_light, image=editButtonPng, command=edit_button_func)
    editButton.place(x=710, y=35)


# Downloaded Panel


def downloaded_panel_func():
    global downloadedPanelFrame
    downloadedPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    downloadedPanelFrame.place(x=310, y=2)

    downloadedPanel = Label(downloadedPanelFrame, bd=0, bg=backgroundColor, image=downloadedPanelPng)
    downloadedPanel.place(x=-22, y=15)

    conn = sqlite3.connect("movies_data.db")
    cur = conn.cursor()
    cur.execute("select * from movies where download_status = 'Yes'")
    global data4
    data4 = cur.fetchall()
    rowcount = len(data4)
    conn.close()

    if rowcount == 0:
        smily = Label(downloadedPanelFrame, text="Nothing Found :)", bd=0, bg=yellow_dark, fg=black_font, font=(font, 30, "normal"))
        smily.place(x=280, y=250)

        emptyLabel = Label(downloadedPanelFrame, text="It's Empty Here !", bd=0, bg=yellow_light, fg=black_font,
                      font=(font, 20, "normal"))
        emptyLabel.place(x=330, y=550)
        return

    # data[<row>][<column>]

    global maxLength
    maxLength = rowcount - 1
    global current_movie
    current_movie = 0
    global next_movie
    next_movie = current_movie + 1
    global movieName
    movieName = 1
    global release_day
    release_day = 2
    global release_month
    release_month = 3
    global release_year
    release_year = 4
    global watched_status
    watched_status = 5
    global link
    link = 7
    global origin
    origin = 8

    movieLabel = Label(downloadedPanelFrame, text=data4[current_movie][movieName], bd=0, bg=yellow_dark, fg=black_font,
                           font=(font, 35, 'normal'))
    movieLabel.place(x=78, y=100)

    originLabel = Label(downloadedPanelFrame, text="Origin : " + data4[current_movie][origin], bd=0, bg=yellow_dark,
                            fg=black_font, font=(font, 30, 'normal'))
    originLabel.place(x=110, y=175)

    releaseDateLabel = Label(downloadedPanelFrame,
                                text="Release Date : " + str(data4[current_movie][release_day]) + " " + month_string(
                                str(data4[current_movie][release_month])) + " " + str(
                                data4[current_movie][release_year]),
                                bd=0, bg=yellow_dark,
                                fg=black_font,
                                font=(font, 30, 'normal'))
    releaseDateLabel.place(x=110, y=235)

    watchedStatusLabel = Label(downloadedPanelFrame, text="Watched : " + data4[current_movie][watched_status],
                                    bd=0, bg=yellow_dark, fg=black_font, font=(font, 30, 'normal'))
    watchedStatusLabel.place(x=110, y=290)

    linkLabel = Label(downloadedPanelFrame, text="Link : ", bd=0, bg=yellow_dark, fg=black_font,
                          font=(font, 30, 'normal'))
    linkLabel.place(x=110, y=350)

    linkEntry = Entry(downloadedPanelFrame, bd=0, bg=yellow_dark, width=25, fg=black_font, font=(font, 30, 'normal'),
                          justify="left")
    linkEntry.place(x=220, y=350)
    linkEntry.insert(0, data4[current_movie][link])

    counterEntry = Entry(downloadedPanelFrame, bd=0, bg=yellow_dark, width=10, fg=black_font, font=(font, 35, 'normal'),
                             justify="right")
    counterEntry.place(x=560, y=450)
    counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

    upNextLabel = Label(downloadedPanelFrame, text="Up Next", bd=0, bg=yellow_light, fg=black_font,
                            font=(font, 20, 'normal'))
    upNextLabel.place(x=78, y=530)

    try:
        nextMovieLabel = Label(downloadedPanelFrame, text=data4[next_movie][movieName], bd=0, bg=yellow_light,
                                fg=font_darkcolor,
                                font=(font, 16, 'normal'))
        nextMovieLabel.place(x=97, y=575)

        nextMovieYearLabel = Label(downloadedPanelFrame, text=data4[next_movie][release_year], bd=0, bg=yellow_light,
                                   fg=font_darkcolor, font=(font, 16, 'normal'))
        nextMovieYearLabel.place(x=97, y=610)
    except:
        pass

    def back_button_func():
        global data4
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global watched_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie > 0:
                current_movie -= 1
                movieLabel.config(text=data4[current_movie][movieName])
                originLabel.config(text="Origin : " + data4[current_movie][origin])
                releaseDateLabel.config(
                    text="Release Date : " + str(data4[current_movie][release_day]) + " " + month_string(
                    str(data4[current_movie][release_month])) + " " + str(data4[current_movie][release_year]))
                watchedStatusLabel.config(text="Watched : " + data4[current_movie][watched_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data4[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie > 1:
                next_movie -= 1
                nextMovieLabel.config(text=data4[next_movie][movieName])
                nextMovieYearLabel.config(text=data4[next_movie][release_year])

    backButtonFrame = LabelFrame(downloadedPanelFrame, bd=0, height=50, width=100, bg=yellow_light)
    backButtonFrame.place(x=590, y=565)
    backButton = Button(backButtonFrame, bd=0, bg=yellow_light, activebackground=yellow_light, image=backDarkButtonPng,
                        command=back_button_func)
    backButton.place(x=0, y=0)

    def next_button_func():
        global data4
        global maxLength
        global current_movie
        global next_movie
        global movieName
        global release_day
        global release_month
        global release_year
        global watched_status
        global link
        global origin

        if maxLength != 0:
            next_movie = current_movie + 1

            if current_movie < maxLength:
                current_movie += 1
                movieLabel.config(text=data4[current_movie][movieName])
                originLabel.config(text="Origin : " + data4[current_movie][origin])
                releaseDateLabel.config(
                    text="Release Date : " + str(data4[current_movie][release_day]) + " " + month_string(
                        str(data4[current_movie][release_month])) + " " + str(data4[current_movie][release_year]))
                watchedStatusLabel.config(text="Watched : " + data4[current_movie][watched_status])
                linkEntry.delete(0, END)
                linkEntry.insert(0, data4[current_movie][link])
                counterEntry.delete(0, END)
                counterEntry.insert(0, str(current_movie + 1) + " of " + str(rowcount))

            if next_movie < maxLength:
                next_movie += 1
                nextMovieLabel.config(text=data4[next_movie][movieName])
                nextMovieYearLabel.config(text=data4[next_movie][release_year])
            else:
                nextMovieLabel.config(text="Finished !")
                nextMovieYearLabel.config(text="")

    nextButtonFrame = LabelFrame(downloadedPanelFrame, bd=0, height=50, width=100, bg=yellow_light)
    nextButtonFrame.place(x=710, y=565)
    nextButton = Button(nextButtonFrame, bd=0, bg=yellow_light, activebackground=yellow_light, image=nextDarkButtonPng,
                            command=next_button_func)
    nextButton.place(x=0, y=0)

    def edit_button_func():
        edit_page(downloadedPanelFrame, data4[current_movie][0])

    editButton = Button(downloadedPanelFrame, bd=0, bg=yellow_dark, activebackground=yellow_dark, image=editDarkButtonPng,
                        command=edit_button_func)
    editButton.place(x=710, y=35)

# All Movies Panel


def allmovies_panel_func():
    global allMoviePanelFrame
    allMoviePanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    allMoviePanelFrame.place(x=310, y=2)

    allMoviePanel = Label(allMoviePanelFrame, bd=0, bg=backgroundColor, image=allMoviePanelPng)
    allMoviePanel.place(x=6, y=11)

# Hollywood Panel


def hollywood_panel_func():
    global hollywoodPanelFrame
    hollywoodPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    hollywoodPanelFrame.place(x=310, y=2)

    hollywoodPanel = Label(hollywoodPanelFrame, bd=0, bg=backgroundColor, image=hollywoodPanelPng)
    hollywoodPanel.place(x=6, y=11)

# Bollywood Panel


def bollywood_panel_func():
    global bollywoodPanelFrame
    bollywoodPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    bollywoodPanelFrame.place(x=310, y=2)

    bollywoodPanel = Label(bollywoodPanelFrame, bd=0, bg=backgroundColor, image=bollywoodPanelPng)
    bollywoodPanel.place(x=6, y=11)

# Tollywood Panel


def tollywood_panel_func():
    global tollywoodPanelFrame
    tollywoodPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    tollywoodPanelFrame.place(x=310, y=2)

    tollywoodPanel = Label(tollywoodPanelFrame, bd=0, bg=backgroundColor, image=tollywoodPanelPng)
    tollywoodPanel.place(x=6, y=11)

# Others Panel


def other_panel_func():
    global otherPanelFrame
    otherPanelFrame = LabelFrame(root, bd=0, bg=backgroundColor, width=865, height=665)
    otherPanelFrame.place(x=310, y=2)

    otherPanel = Label(otherPanelFrame, bd=0, bg=backgroundColor, image=otherPanelPng)
    otherPanel.place(x=6, y=11)


dashboard_panel_func()


def remove_panel():
    global dashboardPanelFrame
    global addPanelFrame
    global unwatchedPanelFrame
    global todownloadPanelFrame
    global watchedPanelFrame
    global downloadedPanelFrame
    global allMoviePanelFrame
    global hollywoodPanelFrame
    global bollywoodPanelFrame
    global tollywoodPanelFrame
    global otherPanelFrame

    try:
        dashboardPanelFrame.destroy()
    except:
        pass
    try:
        addPanelFrame.destroy()
    except:
        pass
    try:
        unwatchedPanelFrame.destroy()
    except:
        pass
    try:
        todownloadPanelFrame.destroy()
    except:
        pass
    try:
        watchedPanelFrame.destroy()
    except:
        pass
    try:
        downloadedPanelFrame.destroy()
    except:
        pass
    try:
        allMoviePanelFrame.destroy()
    except:
        pass
    try:
        hollywoodPanelFrame.destroy()
    except:
        pass
    try:
        bollywoodPanelFrame.destroy()
    except:
        pass
    try:
        tollywoodPanelFrame.destroy()
    except:
        pass
    try:
        otherPanelFrame.destroy()
    except:
        pass

# Menu Panel


menuPanel = Label(root, bd=0, bg=backgroundColor, image=menuPanelPng)
menuPanel.place(x=2, y=2)

mfLogo = Label(root, bd=0, bg=backgroundColor, image=mfLogoPng)
mfLogo.place(x=45, y=35)

movieFlexLabel = Label(root, bd=0, bg=backgroundColor, image=movieFlexLabelPng)
movieFlexLabel.place(x=110, y=42)


def show_dashboard_panel():
    remove_panel()
    dashboard_panel_func()


dashBoardButton = Button(root, bd=0, bg=backgroundColor, image=dashBoardButtonPng, activebackground=backgroundColor, command=show_dashboard_panel)
dashBoardButton.place(x=62, y=103)


def show_addmovie_panel():
    remove_panel()
    add_panel_func()


addMovieButton = Button(root, bd=0, bg=backgroundColor, image=addMovieButtonPng, activebackground=backgroundColor, command=show_addmovie_panel)
addMovieButton.place(x=62, y=163)


def show_unwatched_panel():
    remove_panel()
    unwatched_panel_func()


unwatchedButton = Button(root, bd=0, bg=backgroundColor, image=unwatchedButtonPng, activebackground=backgroundColor, command=show_unwatched_panel)
unwatchedButton.place(x=62, y=223)


def show_todownload_panel():
    remove_panel()
    todownload_panel_func()


toDownloadButton = Button(root, bd=0, bg=backgroundColor, image=toDownloadButtonPng, activebackground=backgroundColor, command=show_todownload_panel)
toDownloadButton.place(x=62, y=283)


def show_watched_panel():
    remove_panel()
    watched_panel_func()


watchedButton = Button(root, bd=0, bg=backgroundColor, image=watchedButtonPng, activebackground=backgroundColor, command=show_watched_panel)
watchedButton.place(x=62, y=343)


def show_downloaded_panel():
    remove_panel()
    downloaded_panel_func()


downloadedButton = Button(root, bd=0, bg=backgroundColor, image=downloadedButtonPng, activebackground=backgroundColor, command=show_downloaded_panel)
downloadedButton.place(x=62, y=403)


def show_allmovies_panel():
    remove_panel()
    allmovies_panel_func()


allMoviesButton = Button(root, bd=0, bg=backgroundColor, image=allMovieButtonPng, activebackground=backgroundColor, command=show_allmovies_panel)
allMoviesButton.place(x=62, y=463)


def show_hollywood_panel():
    remove_panel()
    hollywood_panel_func()


hollywoodButton = Button(root, bd=0, bg=backgroundColor, image=hollywoodButtonPng, activebackground=backgroundColor, command=show_hollywood_panel)
hollywoodButton.place(x=32, y=525)


def show_bollywood_panel():
    remove_panel()
    bollywood_panel_func()


bollywoodButton = Button(root, bd=0, bg=backgroundColor, image=bollywoodButtonPng, activebackground=backgroundColor, command=show_bollywood_panel)
bollywoodButton.place(x=155, y=525)


def show_tollywood_panel():
    remove_panel()
    tollywood_panel_func()


tollywoodButton = Button(root, bd=0, bg=backgroundColor, image=tollywoodButtonPng, activebackground=backgroundColor, command=show_tollywood_panel)
tollywoodButton.place(x=32, y=584)


def show_other_panel():
    remove_panel()
    other_panel_func()

othersButton = Button(root, bd=0, bg=backgroundColor, image=othersButtonPng, activebackground=backgroundColor, command=show_other_panel)
othersButton.place(x=155, y=584)

root.mainloop()