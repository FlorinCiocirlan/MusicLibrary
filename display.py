
print("Welcome to Music Library!")
print("""Press 1 to view all music
Press 2 if you want to choose by genre
Press 3 to choose albums by time range
Press 4 to see the longest and shortest album 
Press 5 to choose albums by artist
Press 6 to choose by album name
Press 7 to get a full report of music library
Press 8 to add an album

""")

from MusicLibrary import *





while True:
    user_input = input("What would you like to do ?")
    if user_input == "1":
        print("\n")
        print(data)
        print("\n")
    elif user_input == "2":
        find_by_genre()
    elif user_input == "3":
        albums_from_given_time()
    elif user_input == "4":
        shortest_longest_album()
    elif user_input == "5":
        albums_by_artist()
    elif user_input == "6":
        albums_from_given_name()
    elif user_input == "7":
        get_report()
    elif user_input == "8":
        add_album()
        