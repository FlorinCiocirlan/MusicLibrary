with open("library.txt") as file:                                            # Open the file from where we want to import music library datas from
    data = file.read()                                                       # This script just open it and store informations into a variable name "data"

list_of_list = []                                                            # this script creates a list named "list_of_list"

def convert_data_from_file(x):

    for a in x.splitlines():                                                 # it appends info from variable data into a big list
        list_of_list.append(a.split(","))                                    # this big list has 11 items in it
    return list_of_list                                                      # each item represent a line from our music library file

convert_data_from_file(data)

artist_name = []
album_name = []
release_year = []                                                            # We will store sorted info in these lists
music_genre = []
length_time = []


def sort_big_list():                                                         # This script sorts the data from the big list named "list_of_list"
      for eachItem in list_of_list:                                          # It appends certain data to a specific list -> check the list names
          artist_name.append(eachItem[0])                                    # Example: artist_name contains all the artist names from the file
          album_name.append(eachItem[1])                                     # eachItem represents every item from the big list
          release_year.append(eachItem[2])                                   # The value of eachItem[x] is appended to a specific list
          music_genre.append(eachItem[3])                                    # Where x represents the index
          length_time.append(eachItem[4])                                    # for certain elements that we want to store in a specific list
      return artist_name, album_name, release_year, music_genre, length_time

sort_big_list()

                    
def find_by_genre():    
    x = input("What genre would you like to see? ")                          # This function prints all abums by selected genre
    for eachGenre in list_of_list:
        if x in eachGenre[3]:                                       
            print(" ,".join(eachGenre))  
#find_by_genre()                                      


def albums_from_given_time():
    print("What years: ")
    year1, year2 = map(int, input().split("-"))   
    for time in list_of_list:                                                # This function prints all albums from a given time range
        if int(time[2]) >= year1 and int(time[2]) < year2:
            print(" ,".join(time))
albums_from_given_time()


def albums_from_given_name():
    a = []
    x = input("What album do you want? ")
    for name in list_of_list:
        for eachItem in name:                                                # This function prints all albums by a given name
            if x.lower() in eachItem.lower():
                a.append(name)
    return a
print(albums_from_given_name())


def albums_by_artist():
    a = []
    x = input("What artist do you want? ")
    for artist in list_of_list:
        for eachItem in artist:                                              # This function prints all albums by a given artist name
            if x.lower() in eachItem.lower():
                a.append(artist)
    return a
print(albums_by_artist())


def shortest_longest_album():
    a = []
    b = []
    for i in length_time:
        a.append(i.replace(":", ""))
    for i in a:
        b.append(int(i))
    b.sort()
    a = []                                                                    # This function prints the shortest and the longest album
    for i in b:
        a.append(str(i))
    b = []
    for i in a:
        b.append(i[:-2]+":"+i[-2:])
    for eachItem in list_of_list:   
        if b[0] in eachItem:   
            print("Shortest album is : "," ,".join(eachItem))
        if b[-1] in eachItem:
            print("Longest album is  : "," ,".join(eachItem))
#shortest_longest_album()