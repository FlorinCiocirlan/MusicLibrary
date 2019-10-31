# Open the file from where we want to import music library datas from
# This script just open it and store informations into a variable name "data"
from collections import Counter


def read():
    with open("library.txt") as file:
        data = file.read()
        return data


data = read()

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


def find_by_genre():
    x = input("What genre would you like to see ?")
    for eachGenre in list_of_list:
        if x in eachGenre[3]:
            new_output = " ".join(str(i) for i in eachGenre)
            print(new_output)


# This prints out every sorted list


#


def add_album():
    details = ["artist name", "name", "release year", "genre", "length"]
    try:
        x = [input(" What is the %s of the album ? " % i) for i in details]
    except ValueError:
        " Please insert certain data for specific field"
    f = open("library.txt", "+a")
    f.write("\n")
    f.write(",".join(x).title())
    print(data)


def albums_from_given_time():
    print("What years: ")
    year1, year2 = map(int, input().split("-"))
    for time in list_of_list:
        if year1 <= int(time[2]) < year2:
            print(" ,".join(time))


def albums_from_given_name():
    a = []
    x = input("What album do you want? ")
    for name in list_of_list:
        for eachItem in name:
            if x.lower() in eachItem.lower():
                a.append(name)
    print(albums_from_given_name())
    return a


def albums_by_artist():
    a = []
    x = input("What artist do you want? ")
    for artist in list_of_list:
        for eachItem in artist_name:
            if x.lower() in artist[0].lower():
                a.append(artist)
    print(",".join(str(eachItem) for eachItem in artist))
    return a


def shortest_longest_album():
    print("Shortest album is : " + album_name[shortest_album_position()])
    print("Longest album is  : " + album_name[longest_album_position()])


def convert_time_from_text(time):
    hour = time[:time.find(":")]
    minutes = time[time.find(":") + 1:]
    total_time = int(hour) * 60 + int(minutes)
    return total_time


def length_time_to_seconds():
    length_time_seconds = []
    for time in length_time:
        length_time_seconds.append(convert_time_from_text(time))
    return length_time_seconds


def shortest_album_position():
    temp = length_time_to_seconds()
    return temp.index(min(temp))


def longest_album_position():
    temp = length_time_to_seconds()
    return temp.index(max(temp))


def oldest_album_position():
    pos = 0
    minim = int(release_year[0])
    for year in release_year:
        if minim > int(year):
            minim = int(year)
            pos = release_year.index(year)
    return pos


def youngest_album_position():
    pos = 0
    maxim = int(release_year[0])
    for year in release_year:
        if maxim < int(year):
            maxim = int(year)
            pos = release_year.index(year)
    return pos


def get_report():
    report = "This is the report:\n"
    longest_album = album_name[longest_album_position()]
    shortest_album = album_name[shortest_album_position()]
    oldest_album = album_name[oldest_album_position()]
    youngest_album = album_name[youngest_album_position()]
    all_albums_count = len(album_name)

    report = report + "Longest album is: " + longest_album + "\n"
    report = report + "Shortest album is: " + shortest_album + "\n"
    report = report + "Oldest album is: " + oldest_album + "\n"
    report = report + "Youngest album is: " + youngest_album + "\n"
    report = report + "Total number of albums: " + str(all_albums_count) + "\n"
    report = report + "Number of albums by genre: " + str(Counter(music_genre)) + "\n"

    print(report)
