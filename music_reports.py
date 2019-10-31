
with open("library.txt") as file:                                   # Open the file from where we want to import music library datas from
    data = file.read()                                              # This script just open it and store informations into a variable name "data"

list_of_list = []                                                   # this script creates a list named "list_of_list"

def convert_data_from_file(x):

    for a in x.splitlines():                                        # it appends info from variable data into a big list
        list_of_list.append(a.split(","))                           # this big list has 11 items in it
    return list_of_list                                             # each item represent a line from our music library file

convert_data_from_file(data)

artist_name = []
album_name = []
release_year = []                                                   # We will store sorted info in these lists
music_genre = []
length_time = []


def sort_big_list():                                                # This script sorts the data from the big list named "list_of_list"
      for eachItem in list_of_list:                                 # It appends certain data to a specific list -> check the list names
          artist_name.append(eachItem[0])                           # Example: artist_name contains all the artist names from the file
          album_name.append(eachItem[1])                            # eachItem represents every item from the big list
          release_year.append(eachItem[2])                          # The value of eachItem[x] is appended to a specific list
          music_genre.append(eachItem[3])                           # Where x represents the index
          length_time.append(eachItem[4])                           # for certain elements that we want to store in a specific list
      return artist_name, album_name, release_year, music_genre, length_time

sort_big_list()


def find_by_genre(x):                                               # This function prints all abums by genre
    for eachGenre in list_of_list:                                  # eachGenre iterates through the list_of_lists
        if x in eachGenre[3]:                                       # If the user input is in one of the albums
            print(eachGenre)                                        # The function prints out the certain albums


print(data, "\nThese are the albums you own\n")                     # This prints out every sorted list

def albums_from_given_time():
    x = input("From what year do you want to see the albums: ")     
    for time in list_of_list:                                       # This function prints all albums from a given time range
        if int(time[2]) >= int(x):
            print(time)
albums_from_given_time()


def albums_from_given_name():
    x = input("What album do you want? ")
    for name in list_of_list:
        for eachItem in name:                                       # This function prints all albums by a given name
            if x.lower() in eachItem.lower():
                print(name)
albums_from_given_name()


def albums_by_artist():
    x = input("What artist do you want? ")
    for artist in list_of_list:
        for eachItem in artist:                                     # This function prints all albums by a given artist name
            if x.lower() in eachItem.lower():
                print(artist)
albums_by_artist()


while True:
    user_input = input("What do you want to see? :")
    if user_input == "all albums":
        print(album_name)
    elif user_input == "all music":xs
    else:
        find_by_genre(user_input)


