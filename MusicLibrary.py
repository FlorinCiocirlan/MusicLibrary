# Open the file from where we want to import music library datas from
# This script just open it and store informations into a variable name "data"

with open("library.txt") as file:
    data = file.read()


# this script creates a list named "list_of_list"
# it appends info from variable data into a big list

# this big list has 11 items in it
# each item represent a line from our music library file

list_of_list = []


def convert_data_from_file(x):

    for a in x.splitlines():
        list_of_list.append(a.split(","))
    return list_of_list


convert_data_from_file(data)

# We will store sorted info in these lists

artist_name = []
album_name = []
release_year = []
music_genre = []
length_time = []

# This script sorts the data from the big list named "list_of_list"
# It appends certain data to a specific list -> check the list names

# Example: artist_name contains all the artist names from the file
# eachItem represents every item from the big list

# The value of eachItem[x] is appended to a specific list
# Where x represents the index
# for certain elements that we want to store in a specific list


def sort_big_list():
      for eachItem in list_of_list:
          artist_name.append(eachItem[0])
          album_name.append(eachItem[1])
          release_year.append(eachItem[2])
          music_genre.append(eachItem[3])
          length_time.append(eachItem[4])
      return artist_name, album_name, release_year, music_genre, length_time


sort_big_list()



# This function prints all abums by genre
# eachGenre iterates through the list_of_lists
# If the user input is in one of the albums
# The function prints out the certain albums


def find_by_genre(x):
    # x = input("What do you want to see?")
    for eachGenre in list_of_list:
        if x in eachGenre:
            print(eachGenre)


# This prints out every sorted list


print(data, "\nThese are the albums you own\n")

while True:
    user_input = input("What do you want to see? :")
    if user_input == "all albums":
        print(album_name)
    elif user_input == "all music":
        print(data)
    else:
        find_by_genre(user_input)
