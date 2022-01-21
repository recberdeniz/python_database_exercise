import sqlite3
import time
# This code module is written by @recberdeniz to exercise about database application for Python Programming
# Playlist class: This class includes database queries for operations;
# I added 9 different operations for this playlist database, explaining of the operations and functions for this module;
# Firstly, this class includes connection and disconnection functions for database
# If there is no database named as Playlist.db, make_connection function will create this database
# If Playlist has musics, show_playlist function shows all saved music information.
# Otherwise, this function dedicate that "Playlist is empty"
# add_music function can insert new music information to Playlist.db
# delete_music function can delete a music that you selected from Playlist.db
# With music_query function, it is possible to make a query accordingly music name
# Also other query functions can query the music that accordingly artist, language and genre
# calculate_totalrecord function can calculate total music length in the playlist
# user also can update the music duration with update_duration function
# clear_playlist function clears completely the playlist and remove all of music information

# Music class: This class includes music information and music information printing

class Music():

    def __init__(self, name, artist, album, production, year, duration, language, genre):
        self.name = name
        self.artist = artist
        self.album = album
        self.production = production
        self.year = year
        self.duration = duration
        self.language = language
        self.genre = genre

    def __str__(self):
        return "Song Name: {}\nArtist: {}\nAlbum: {}\nProduction: {}\nYear: {}\nDuration: {}\nLanguage: {}\nGenre: {}" \
            .format(self.name, self.artist, self.album, self.production, self.year, self.duration, self.language,
                    self.genre)


class Playlist():

    def __init__(self):

        self.make_connection()

    def make_connection(self):
        self.connection = sqlite3.connect("Playlist.db")
        self.cursor = self.connection.cursor()
        query = "Create Table If not exists Musics (name TEXT, artist TEXT, album TEXT, production TEXT, year INT, " \
                "duration TEXT, language TEXT, genre TEXT)"

        self.cursor.execute(query)
        self.connection.commit()

    def disconnect(self):

        self.connection.close()

    def show_playlist(self):

        query = "Select * From Musics"
        self.cursor.execute(query)
        Musics = self.cursor.fetchall()

        if len(Musics) == 0:
            print("Playlist is empty...")

        else:
            for i in Musics:
                music = Music(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(music)

    def music_query(self, name):

        query = "Select * From Musics where name = ?"
        self.cursor.execute(query, (name,))
        Musics = self.cursor.fetchall()

        if len(Musics) == 0:
            print("The music you are looking for is not in the playlist...")

        else:
            music = Music(Musics[0][0], Musics[0][1], Musics[0][2], Musics[0][3], Musics[0][4], Musics[0][5], \
                          Musics[0][6], Musics[0][7])
            print(music)

    def artist_query(self, artist):

        query = "Select * From Musics where artist = ?"
        self.cursor.execute(query, (artist,))
        Musics = self.cursor.fetchall()

        if len(Musics) == 0:
            print("The artist you are looking for is not in the playlist...")

        else:
            for i in Musics:
                music = Music(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(music)

    def language_query(self, language):

        query = "Select * From Musics where language = ?"
        self.cursor.execute(query, (language,))
        Musics = self.cursor.fetchall()

        if len(Musics) == 0:
            print("There is no music in the language you looking for in the playlist...")

        else:
            for i in Musics:
                music = Music(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(music)

    def genre_query(self, genre):

        query = "Select * From Musics where genre = ?"
        self.cursor.execute(query, (genre,))
        Musics = self.cursor.fetchall()

        if len(Musics) == 0:
            print("There is no music that music genre you looking for in the playlist...")

        else:
            for i in Musics:
                music = Music(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(music)

    def calculate_totalrecord(self):

        query = "Select * From Musics"
        self.cursor.execute(query)
        Musics = self.cursor.fetchall()

        if len(Musics) == 0:
            print("Playlist is empty, total record time has not calculated...")

        else:
            minute = 0
            second = 0
            hour = 0
            resf = 0
            resh = 0
            for i in Musics:
                duration = i[5]
                newd = duration.split('.')
                minute += int(newd[0])
                second += int(newd[1])
            if second >= 60:
                resf = second // 60
                second = second % 60
                minute += resf
            if minute >= 60:
                resh = minute // 60
                minute = minute % 60
                hour += resh

            print(hour, '.', minute, '.', second)

    def add_music(self, music):
        query = "Insert into Musics Values (?,?,?,?,?,?,?,?)"
        self.cursor.execute(query, (music.name, music.artist, music.album, music.production, music.year, \
                                    music.duration, music.language, music.genre))
        self.connection.commit()

    def delete_music(self, name):
        query = "Delete From Musics where name = ?"
        check_query = "Select * From Musics where name = ?"
        self.cursor.execute(check_query, (name,))
        Musics = self.cursor.fetchall()

        if len(Musics) !=0:
            self.cursor.execute(query, (name,))
            self.connection.commit()
            print("Music is removed from playlist")
        else:
            print("The music that you would like to delete is not into playlist")

    def clear_playlist(self):
        query = "Delete From Musics"
        self.cursor.execute(query)
        self.connection.commit()
        print("Playlist is cleared.")

    def update_duration(self, name, duration):
        query = "Select * From Musics where name = ?"
        self.cursor.execute(query, (name,))
        Musics = self.cursor.fetchall()

        if len(Musics) != 0:
            length = Musics[0][5]
            query2 = "Update Musics set duration = ? where duration = ?"
            self.cursor.execute(query2, (duration, length))
            self.connection.commit()
            print("Duration update process is finished.")

        else:
            print("The music that you inserted, do not found in playlist...")
            print("Please check the name of song...")


