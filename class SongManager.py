import re
import json

#Function to display menu
def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a song")
    print("2. view a Song")
    print("3. Delete a song")
    print("4. Search for a song")
    print("5. Display all songs")
    print("6. Export songs to a text file")
    print("7. Import songs from a text file")
    print("8. Quit")
    
#Function to add a new song
def add_song(song):
    print("\nAdding a new song:")
    songtitle = input("Enter songtitle: ")
    Album = input("Enter Album name: ")
    Artist = input("Enter Artist Name:")
    additional_info = input("Enter additional information (optional): ")
    Song = {"SongTitle": songtitle, "Album": Album, "Artist": Artist, "Additional Info": additional_info}
    song[songtitle] = Artist
    print("songs added successfully!")

# Function to edit an existing song
def edit_Songlist(songlist):
    print("\nEditing an existing song:")
    Artist = input("Enter the songtitle of the Song you want to edit: ")
    if song in songlist:
        print("Existing details:")
        print(songlist[Songtitle])
        Songtitle = input("Enter new title: ")
        Artist = input("Enter Artistname: ")
        additional_info = input("Enter new additional information: ")
        songlist[Songtitle]["Album"] = Album
        songlist[Songtitle]["Artistname"] = Artist
        songlist[Songtitle]["Additional Info"] = additional_info
        print("song edited successfully!")
    else:
        print("song not found.")

# Function to delete a song
def delete_song(song):
    print("\nDeleting a song:")
    songtitle = input("Enter the songtitle of the song you want to delete: ")
    if songtitle in song:
        del songtitle[song]
        print("song deleted successfully!")
    else:
        print("song not found.")

# Function to search for a song
def search_song(songlist):
    print("\nSearching for a song:")
    songtitle = input("Enter the songtitle of the song you want to search for: ")
    if songtitle in songlist:
        print("song details:")
        print(songlist[songtitle])
    else:
        print("song not found.")

# Function to display all songs
def display_all_songlist(songlist):
    print("\nAll songlist:")
    for Album, songtitle in songlist.items():
        print("songtitle:", songtitle)
        print("Album:", Album)
        print("Artistname:", Artist)

# Function to export song to a text file
def export_songs(songlist):
    print("\nExporting song to a text file:")
    with open("song.txt", "w") as file:
        json.dump(songtitle, file)
    print("Contacts exported successfully!")

# Function to import song from a text file
def import_song(songtitle):
    print("\nImporting song from a text file:")
    try:
        with open("song.txt", "r") as file:
            song.update(json.load(file))
        print("song imported successfully!")
    except FileNotFoundError:
        print("No song file found.")
    except Exception as e:
        print("Error occurred while importing song:", e)

# Main function
def main():
    Songlist = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_song(Songlist)
        elif choice == "2":
            edit_song(Songlist)
        elif choice == "3":
            delete_song(Songlist)
        elif choice == "4":
            search_song(Songlist)
        elif choice == "5":
            display_all_song(Songlist)
        elif choice == "6":
            export_song(Songlist)
        elif choice == "7":
            import_song(Songlist)
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()