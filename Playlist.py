from Song import Song
import random
class Playlist:
  def __init__(self):
    self.__first_song = []


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    self.__first_song.append(Song(title))
    



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    counter = -1
    for song in self.__first_song:
      counter = counter +1 
      if song.get_title() == title:
        return counter
    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    counter = -1
    for song in self.__first_song:
      counter = counter +1 
      if song.get_title() == title:
        self.__first_song.pop(counter)
      

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    return len(self.__first_song)


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    counter = 0 
    for song in self.__first_song:
      counter = counter + 1
      print(f'{counter}. {song.get_title()}')


#----------------------------
#STretch CHaLlanGe!!!
  def shuffle(self):
    random.shuffle(self.__first_song)
        

  