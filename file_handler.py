import classes
import csv
import re

def load_files(movies):
    # opens user rating file
    r_file = open("data/movielens/ratings.csv")

    for line in r_file:
        line_split = line.split(",")

        m_id = line_split[1]
        m_rating = line_split[2]

        if m_id in movies:
            movies[m_id].ratings.append(float(m_rating))
        else:
            movies[m_id] = classes.Movie(m_id)
            movies[m_id].ratings.append(float(m_rating))

    r_file.close()
    # open movie data file
    m_csv_file = open("data/movielens/movies.csv", newline='')
    m_file = csv.reader(m_csv_file)

    for line in m_file:
        m_id = line[0]

        if m_id not in movies.keys():
            continue

        if len(movies[m_id].ratings) < 50:
            del movies[m_id]
            continue

        m_title_line = line[1]
        m_date_obj = re.search(r"[(][1-2][0-9]{3}[)]", m_title_line)

        if m_date_obj == None:
            del movies[m_id]
            continue
        else:
            
            m_date = int(m_date_obj.group(0).replace("(", "").replace(")", ""))
            m_title_line = m_title_line.replace(m_date_obj.group(0), "").strip()

        # splits genre on | char and stores as a list in movie object
        m_genres = line[2].strip()
        genre_split_line = m_genres.split('|')

        if m_id in movies:
            movies[m_id].title = m_title_line
            
            if "Action" in genre_split_line:
                movies[m_id].g_action = 1
            if "Adventure" in genre_split_line:
                movies[m_id].g_adv = 1
            if "Animation" in genre_split_line:
                movies[m_id].g_ani = 1
            if "Biography" in genre_split_line:
                movies[m_id].g_bio = 1
            if "Children" in genre_split_line:
                movies[m_id].g_child = 1
            if "Comedy" in genre_split_line:
                movies[m_id].g_comedy = 1
            if "Crime" in genre_split_line:
                movies[m_id].g_crime = 1
            if "Documentary" in genre_split_line:
                movies[m_id].g_doc = 1
            if "Drama" in genre_split_line:
                movies[m_id].g_drama = 1
            if "Fantasy" in genre_split_line:
                movies[m_id].g_fantasy = 1
            if "Film-Noir" in genre_split_line:
                movies[m_id].g_film = 1
            if "Horror" in genre_split_line:
                movies[m_id].g_horror = 1
            if "History" in genre_split_line:
                movies[m_id].g_history = 1
            if "Musical" in genre_split_line:
                movies[m_id].g_music = 1
            if "Mystery" in genre_split_line:
                movies[m_id].g_mys = 1
            if "Romance" in genre_split_line:
                movies[m_id].g_rom = 1
            if "Sci-Fi" in genre_split_line:
                movies[m_id].g_sci = 1
            if "Western" in genre_split_line:
                movies[m_id].g_west = 1
            if "War" in genre_split_line:
                movies[m_id].g_war = 1
            if "Thriller" in genre_split_line:
                movies[m_id].g_thrill = 1
            

            movies[m_id].date = m_date

    m_csv_file.close()

def d_load_files(movies):
    imdb_basics_file =  open("data/imdb/data.tsv")

    imdb_id, imdb_title, imdb_date = "", "", ""

    id = 0
    
    for line in imdb_basics_file:
        split_line = line.split("\t")

        # skips first line
        if split_line[0] == "tconst":
            continue
        
        if split_line[1] != "movie":
            continue

        imdb_id = split_line[0].replace("tt", "")
        imdb_title = split_line[2]

        if (split_line[5] == "\\N"):
            continue

        imdb_date = split_line[5]
        genre_split_line = split_line[8].strip('\n').split(",")

        if genre_split_line[0] == "\\N":
            continue

        new_movie = classes.Movie(id)

        new_movie.id = imdb_id
        new_movie.imdb_id = imdb_id
        new_movie.title = imdb_title
        new_movie.date = int(imdb_date)
        
        movies[imdb_id] = new_movie
        
        for g in genre_split_line:
            movies[imdb_id].genres[g] = 1

        if "Action" in genre_split_line:
            movies[imdb_id].g_action = 1
        if "Adventure" in genre_split_line:
            movies[imdb_id].g_adv = 1
        if "Animation" in genre_split_line:
            movies[imdb_id].g_ani = 1
        if "Biography" in genre_split_line:
            movies[imdb_id].g_bio = 1
        if "Children" in genre_split_line:
            movies[imdb_id].g_child = 1
        if "Comedy" in genre_split_line:
            movies[imdb_id].g_comedy = 1
        if "Crime" in genre_split_line:
            movies[imdb_id].g_crime = 1
        if "Documentary" in genre_split_line:
            movies[imdb_id].g_doc = 1
        if "Drama" in genre_split_line:
            movies[imdb_id].g_drama = 1
        if "Fantasy" in genre_split_line:
            movies[imdb_id].g_fantasy = 1
        if "Film-Noir" in genre_split_line:
            movies[imdb_id].g_film = 1
        if "Horror" in genre_split_line:
            movies[imdb_id].g_horror = 1
        if "History" in genre_split_line:
            movies[imdb_id].g_history = 1
        if "Musical" in genre_split_line:
            movies[imdb_id].g_music = 1
        if "Mystery" in genre_split_line:
            movies[imdb_id].g_mys = 1
        if "Romance" in genre_split_line:
            movies[imdb_id].g_rom = 1
        if "Sci-Fi" in genre_split_line:
            movies[imdb_id].g_sci = 1
        if "Thriller" in genre_split_line:
            movies[imdb_id].g_thrill = 1
        if "War" in genre_split_line:
            movies[imdb_id].g_war = 1
        if "Western" in genre_split_line:
            movies[imdb_id].g_west = 1

        new_movie.id = imdb_id
        new_movie.imdb_id = imdb_id
        new_movie.title = imdb_title
        new_movie.date = int(imdb_date)
        
        movies[imdb_id] = new_movie

        id += 1
        print(id)

    imdb_basics_file.close()


    imdb_ratings_file = open("data/imdb/data2.tsv")

    imdb_id, imdb_rating, imdb_numrating = "",0,0

    for line in imdb_ratings_file:
        split_line = line.split("\t")
        
        if split_line[0] == "tconst":
            continue

        imdb_id = split_line[0].strip().replace("tt","")

        if imdb_id not in movies:
            continue


        imdb_rating = float(split_line[1])

        if int(split_line[2]) < 500:
            del movies[imdb_id]
            continue

        imdb_numrating = int(split_line[2])

        movies[imdb_id].rating = imdb_rating
        movies[imdb_id].num_ratings = imdb_numrating

    for m in list(movies):
        if movies[m].num_ratings < 500:
            del movies[m]
        
def load_user_data(user, global_movies):
    u_file = open("data/usermovies.txt")

    for line in u_file:
        line_split = line.split(",")

        m_id = line_split[0]
        m_rating = line_split[1]

        user.movies.append(global_movies[m_id]) 
        user.ratings.append(float(m_rating))

def save_user_data(user):
    u_file = open("data/usermovies.txt", "w")

    for idx, m in enumerate(user.movies):
        u_file.write(m.id + "," + str(user.ratings[idx]) + "\n")