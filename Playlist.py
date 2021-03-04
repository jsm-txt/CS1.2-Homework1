from Song import Song
import random
class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song
    



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current = self.__first_song

    found = False
    counter = 0

    while current != None and not found:

      if current.get_title() == title:
        found = True
        current.__title = None
      else:
        current = current.get_next_song()
        counter += 1

    if found:
      return counter
    else:
      return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current = self.__first_song
    song = self.find_song(title)

    if current == None:
      print('The playlist is empty.')
    
    if song == -1:
      return ('Song not found')
    else:

      if song == 0:
        after_song = current.get_next_song()
        current = None
        self.__first_song = after_song
      if song == 1:
        before_song =current
        removing = before_song.get_next_song()
        after_song =removing.get_next_song()
        before_song = before_song.set_next_song(after_song)
      else:
        for i in range(song-1):
          current = current.get_next_song()
        before_song =current
        removing = before_song.get_next_song()
        after_song =removing.get_next_song()
        before_song = before_song.set_next_song(after_song)
      print('song removed')

      
       
      


  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    current = self.__first_song
    if current == None:
      return -1
    else:
      counter = 1
      while(current.get_next_song()):
        current = current.get_next_song()
        counter +=1
      return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current = self.__first_song
    
    if current == None:
      print('The playlist is empty.')
    else:
      for i in range(self.length()):
        print(f'{i+1}.{current.get_title()}')

        current = current.get_next_song()


#----------------------------
#STretch CHaLlanGe!!!
  def shuffle(self):
    pass

  