import file_handler as fh


def input_loop(global_movies, user):
    user_input = ""

    print("")
    print("1. Show movies you have rated.")
    print("2. Rate a new movie.")
    print("3. Delete a movie rating.")
    print("4. Exit.")
    print("")

    while True:
        user_input, rating = "", ""
        user_input = input("Please enter your selection: ")

        if user_input == "1":
            print_movies(user)
        elif user_input == "2":
            rate_movie(global_movies, user)
        elif user_input == "3":
            delete_movie(user)
        elif user_input == "4":
            return


def print_movies(user):
    for idx, m in enumerate(user.movies):
        print("")
        print("(" + m.id + ") " + m.title + " " + str(m.date) + ": Rating: " + str(user.ratings[idx]))
    print("")

def delete_movie(user):
    user_input = ""

    print_movies(user)
    print("")
    user_input = input("Please enter the id of the movie you wish to delete: ")

def rate_movie(global_movies, user):
    user_input, rating = "", ""

    while user_input != "exit":
        user_input = input("Please enter the name of the movie you wish to rate: ")

        if user_input == "exit":
            print_movies(user)
            break
        
        selected_movie = None

        for movie in global_movies.values():
            if movie.title == user_input:
                selected_movie = movie
                break
        
        if selected_movie == None:
            print("Movie not found.")
            continue

        while True:
            rating = input("Please rate this movie from 0.0 to 5.0, with increments of .5: ")

            if float(rating) < 0.0 or float(rating) > 10.0:
                print("Please enter a valid rating.")
                continue
            
            user.movies.append(selected_movie)
            user.ratings.append(float(rating))
            fh.save_user_data(user)
            break