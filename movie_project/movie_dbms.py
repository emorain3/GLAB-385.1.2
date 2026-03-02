import json
import os



# ============================================================
# =================== PRETTY PRINT FUNCTIONs ==================
# ============================================================
# Formats each movie as a "movie card" with labeled values.
#
# Called Once The Program/while loop ends or when the user selects the View option

def print_movies(movies):
    print("\n========== MOVIE DATABASE ==========\n")

    for title, info in movies.items():
        print(f"🎬 {title}")
        print(f"   Year:     {info['year']}")
        print(f"   Genre:    {info['genre']}")
        print(f"   Director: {info['director']}")
        print(f"   Actors:   {', '.join(info['actors'])}")
        print("\n------------------------------------\n")

    print("============ END OF LIST ============\n")

def print_single_movie(movies, selected):
    
    print(f"🎬 {selected}")
    info = movies[selected]
    print(f"   Year:     {info['year']}")
    print(f"   Genre:    {info['genre']}")
    print(f"   Director: {info['director']}")
    print(f"   Actors:   {', '.join(info['actors'])}")
    print("\n------------------------------------\n")

# ============================================================
# ======================== SEARCH MOVIES =====================
# ============================================================
# Performs a simple search over the movie database.
# The search is case-insensitive and supports partial matches.

def search_movies(movies):
    query = input("Enter part or all of the movie title to search for: ").strip().lower()

    if not query:
        print("You must enter a search term.")
        return

    results = []

    for title in movies:
        if query in title.lower():
            results.append(title)

    if not results:
        print("No movies found matching your search.")
        return

    print("\n========== SEARCH RESULTS ==========\n")
    for title in results:
        print_single_movie(movies, title)
    print("============ END OF RESULTS ==========\n")



# ============================================================
# ======================= LOAD MOVIES ========================
# ============================================================
# Loads movie data from a JSON file if it exists.
# If the file is missing or unreadable, returns an empty dict.

def load_movies(filename="movies.json"):
    if not os.path.exists(filename):
        return {}

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read movie file. Starting with an empty database.")
        return {}


# ============================================================
# ======================= SAVE MOVIES ========================
# ============================================================
# Saves the current movie dictionary to a JSON file labelled "movie_dbms.json".
# Uses indentation for readability.

def save_movies(movies, filename="movies.json"):
    try:
        with open(filename, "w") as file:
            json.dump(movies, file, indent=4)
        print("Movie database saved successfully.")
    except IOError:
        print("Error: Could not save movie database.")

# ============================================================
# ===================== MOVIE DATABASE ========================
# ============================================================

movies = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}
movies.update(load_movies())

# # ============================================================ 
# # ======================= MAIN LOOP ========================== 
# # ============================================================ 
# # This loop keeps the program running until the user chooses to quit.
keep_asking = True
while keep_asking:

    # Prompt User for Action 
    action = input(
        "\nWhat would you like to do?\n"
        "  A - Add a new movie\n"
        "  E - Edit an existing movie\n"
        "  D - Delete a movie\n"
        "  V - View the movie database\n"
        "  S - Search for a movie\n"
        "  Q - Quit\n"
        "Enter your choice: "
    ).strip().upper()
# ------------------------------------------------------------ 
# ADD MOVIE OPTION 
# Triggered when the user selects A. 
# ------------------------------------------------------------

    if action == "A":
        print("You chose: Add a new movie")
        # (call your add-movie logic)
        temp_dict = {}
        name = input("ONE)Enter the movie name: ")

        year_input = input("TWO) Enter the release year: ").strip()
        if year_input.isdigit():
            temp_dict["year"] = int(year_input)
        else:
            print("Please enter a valid year (numbers only).")

        temp_dict["genre"] = input("THREE) Enter the movie genre: ")
        temp_dict["director"] = input("FOUR) Enter the movie director: ")

        actors_input = input("FIVE) Enter the actors as one comma-separated line): ")
        temp_dict["actors"] = [actor for actor in actors_input.split(",")]

        # add movie into database
        movies[name] = temp_dict
        # Check input
        print("Newest movie added: ", movies[name])



# ------------------------------------------------------------ 
# EDIT MOVIE OPTION 
# Triggered when the user selects E. 
# ------------------------------------------------------------

    # Allow User To Edit Movie
    elif action == "E":
        print("You chose: Edit a movie")
        movie_name = input("Enter the exact title of the movie you want to modify: ").strip()

        # Check for pressing enter without inputting a value
        if not movie_name: 
            print("You must enter a movie title.") 

        #  check if movie exists in our DB
        if movie_name not in movies:
            print("That movie is not in the database.")
        else:
            # get movie to edit - FIRST, determine what value to edit
            print( "\nWhich value would you like to edit?\n" 
                  " Y - Year\n" 
                  " G - Genre\n" 
                  " D - Director\n" 
                  " A - Actors\n" )

            field = input("Enter your choice: ").strip().upper()

            # Edit YEAR
            if field == "Y":
                new_year = input("Enter the new release year: ").strip()
                if new_year.isdigit():
                    movies[movie_name]["year"] = int(new_year)
                    print("Year updated successfully.")
                else:
                    print("Invalid year. No changes made.")

            # Edit GENRE
            elif field == "G":
                new_genre = input("Enter the new genre: ").strip()
                if new_genre:
                    movies[movie_name]["genre"] = new_genre
                    print("Genre updated successfully.")
                else:
                    print("Invalid input. No changes made.")

            # Edit DIRECTOR
            elif field == "D":
                new_director = input("Enter the new director: ").strip()
                if new_director:
                    movies[movie_name]["director"] = new_director
                    print("Director updated successfully.")
                else:
                    print("Invalid input. No changes made.")

            # Edit ACTORS
            elif field == "A":
                actors_input = input("Enter the new actors (comma-separated): ").strip()
                actors_list = [actor.strip() for actor in actors_input.split(",") if actor.strip()]
                if actors_list:
                    movies[movie_name]["actors"] = actors_list
                    print("Actors updated successfully.")
                else:
                    print("Invalid input. No changes made.")

            else:
                print("Invalid choice. No changes made.")


# ------------------------------------------------------------ 
# DELETE MOVIE OPTION 
# Triggered when the user selects D. 
# ------------------------------------------------------------

    # Allow User To Delete Movie
    elif action == "D":
        print("You chose: Delete a movie")
        movie_name = input("Which movie would you like to delete? Enter the exact title: ").strip()

        # Check for pressing enter without inputting a value
        if not movie_name: 
            print("You must enter a movie title.")
        
        #  check if movie exists in our DB - IF IT DOES, delete it. No Confirmation, no nothing. GET RID OF IT. 
        if movie_name not in movies:
            print("That movie is not in the database.")
        else:
            del movies[movie_name]
            print("Gone. HOPE YOU DIDN'T MIS-TYPE! AHHH!!!!!")

# ------------------------------------------------------------ 
# VIEW MOVIE OPTION 
# Triggered when the user selects V. 
# ------------------------------------------------------------

    # Allow User To View DB
    elif action == "V":
        print("You chose: View the database")
        view_choice = input( "\nHow would you like to view the database?\n" 
                            " A - View all movies\n" 
                            " O - View one movie\n" 
                            "Enter your choice: " ).strip().upper() 
        # View the entire database 
        if view_choice == "A": 
            print_movies(movies) 
            # View a single movie 
        elif view_choice == "O":
            movie_name = input("Enter the movie name: ").strip()
            if movie_name in movies:
                print_single_movie(movies, movie_name)
            else:
                print("That movie is not in the database.")

# ------------------------------------------------------------ 
# QUIT OPTION 
# Triggered when the user selects Q. 
# ------------------------------------------------------------
    # Allow User To Exit the Prompt Sequence - This will initiate a final display of the Current state of the DB
    elif action == "Q":
        keep_asking = False
        print("Exiting program.")
        break

# ------------------------------------------------------------ 
# SEARCH OPTION 
# Triggered when the user selects S. 
# Allows the user to search for movies by partial or full title. 
# ------------------------------------------------------------

    elif action == "S":
        print("You chose: Search the database")
        search_movies(movies)

    else:
        print("Invalid choice. Please enter A, E, D, V, S, or Q to quit.")




# OUTSIDE OF LOOP
print("---- THE FINAL DICTIONARY/DB CONTAINS THE FOLLOWING ----:")
print_movies(movies)
save_movies(movies)
