# This part is also written to exercise about database application for Python Programming
# This part is the main code part of the Playlist database application
# First part is written as a module of Playlist.db
# Before using these two code parts, check folder directory and mark directory as source roots to use first part as
# a source module
# To mark directory as source roots; right click to the file directory where the two code parts
# and then choose mark directory as source roots in PyCharm compiler
from playlist_module import *

print("""
************************************
Welcome to Playlist Database Program

Operations:
1) Show playlist
2) Add a new music
3) Delete a music
4) Music query
5) Artist query
6) Language query
7) Genre query
8) Total music duration calculation
9) Update music duration
10) Clean playlist

To exit the program please press 'q'
************************************
""")

playlist = Playlist()

while True:
    operation = input("Please choose an operation:")

    if operation == 'q':
        print("Playlist program is shutting down...")
        time.sleep(2)
        break

    elif operation == '1':
        playlist.show_playlist()

    elif operation == '2':
        print("Please insert music information which you would like to add into playlist:")
        name = input("Music name:")
        artist = input("Artist:")
        album = input("Album:")
        production = input("Production:")
        year = int(input("Year:"))
        duration = float(input("Duration:"))
        language = input("Language:")
        genre = input("Genre:")
        new_music = Music(name, artist, album, production, year, duration, language, genre)
        print("Music is adding...")
        time.sleep(2)
        playlist.add_music(new_music)
        print("Music added")

    elif operation == '3':
        print("Please insert name of music that you would like to delete from your playlist:")
        name = input("Music name:")
        response = input("Are you sure? (Y/N)")
        if response == 'Y':
            print("Music that you inserted is deleting...")
            time.sleep(2)
            playlist.delete_music(name)

    elif operation == '4':
        print("Please insert name of music that you would like to looking for:")
        name = input("Music name:")
        print("Music is queried...")
        time.sleep(2)
        playlist.music_query(name)

    elif operation == '5':
        print("Please insert name of artist that you would like to looking for:")
        name = input("Artist name:")
        print("Artist is queried...")
        time.sleep(2)
        playlist.artist_query(name)

    elif operation == '6':
        print("Please insert a language that you would like to looking for:")
        name = input("Language:")
        print("Language is queried...")
        time.sleep(2)
        playlist.language_query(name)

    elif operation == '7':
        print("Please insert a genre that you would like to looking for:")
        name = input("Genre:")
        print("Genre is queried...")
        time.sleep(2)
        playlist.genre_query(name)

    elif operation == '8':
        print("Total Playlist Length is calculating...")
        time.sleep(2)
        print("H / M / S")
        playlist.calculate_totalrecord()

    elif operation == '9':
        name = input("Which song's duration would you like to update:")
        duration = input("Please insert a current duration:")
        print("Update process is started...")
        time.sleep(2)
        playlist.update_duration(name, duration)

    elif operation == '10':
        print("Playlist cleaning operation is ready.")
        response = input("Are you sure that clean all playlist? (Y/N)")
        if response == 'Y':
            print("Playlist cleaning operation is working...")
            time.sleep(2)
            playlist.clear_playlist()

    else:
        print("Invalid operation...")
