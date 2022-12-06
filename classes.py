import numpy

class Movie:
    def __init__(self, id):
        self.id = id
        self.rating = 0
        self.ratings = []
        self.num_ratings = 0

        self.title = ""
        self.date = ""
        self.imdb_id = ""

        self.genres = {}

        self.g_action = 0
        self.g_adv = 0
        self.g_ani = 0
        self.g_bio = 0
        self.g_child = 0
        self.g_comedy = 0
        self.g_crime = 0
        self.g_doc = 0
        self.g_drama = 0
        self.g_fantasy = 0
        self.g_film = 0
        self.g_horror = 0
        self.g_history = 0
        self.g_music = 0
        self.g_mys = 0
        self.g_rom = 0
        self.g_sci = 0
        self.g_thrill = 0
        self.g_war = 0
        self.g_west = 0

        self.rankings = []
        self.avg_ranking = 0


        self.similarity_rating = 0
        self.recommend = 0
    
    def calc_rating(self):
        self.num_ratings = len(self.ratings)
        self.rating = 0

        for i in self.ratings:
            self.rating += i

        self.rating = self.rating / self.num_ratings

    def calc_similarity(self, user):
        w1, w2, w3, w4 = .5, .0001, 5, 5


        date_diff = abs(user.avg_date - self.date)
        num_rating_diff = abs(user.avg_num_ratings - self.num_ratings)
        rating_diff = abs(user.avg_rating - self.rating)

        genre_diff = 0

        if self.g_action == 1:
            if user.genres["Action"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_adv == 1:
            if user.genres["Adventure"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_ani == 1:
            if user.genres["Animation"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_bio == 1:
            if user.genres["Biography"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_child == 1:
            if user.genres["Children"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_comedy == 1:
            if user.genres["Comedy"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_crime == 1:
            if user.genres["Crime"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_doc == 1:
            if user.genres["Documentary"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_drama == 1:
            if user.genres["Drama"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_fantasy == 1:
            if user.genres["Fantasy"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_film == 1:
            if user.genres["Film-Noir"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_horror == 1:
            if user.genres["Horror"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_history == 1:
            if user.genres["History"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_music == 1:
            if user.genres["Musical"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_mys == 1:
            if user.genres["Mystery"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_rom == 1:
            if user.genres["Romance"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_sci == 1:
            if user.genres["Sci-Fi"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_west == 1:
            if user.genres["Western"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_war == 1:
            if user.genres["War"].genre_score < user.avg_genre_score:
                genre_diff += 1
        if self.g_thrill == 1:
            if user.genres["Thriller"].genre_score < user.avg_genre_score:
                genre_diff += 1

        print(genre_diff)
        
        self.similarity_rating = (w1 * date_diff) + (w2 * num_rating_diff) + (w3 * rating_diff) + (w4 * genre_diff)
        return self.similarity_rating

    def get_data(self):
        data = [self.rating, self.num_ratings, self.date, self.g_action, self.g_adv, self.g_ani, self.g_bio, self.g_child, self.g_comedy, self.g_crime, self.g_doc, self.g_drama, self.g_fantasy, self.g_film, self.g_horror, self.g_history, self.g_music, self.g_mys, self.g_rom, self.g_sci, self.g_thrill, self.g_war, self.g_west]
        return data

    def __repr__(self):
        self.calc_rating()
        return "Title: " + self.title + " Ratings: " + str(self.num_ratings) + " Rating: " + str(self.rating) + " ID: " + self.id + " Date: " + str(self.date)

class Genre:
    def __init__(self, name):
        self.name = name
        self.ratings = []
        self.num_ratings = 0
        self.avg_rating = 0

        self.genre_score = 0
    
    def calc_average_rating(self):
        if self.num_ratings == 0:
            return

        for rating in self.ratings:
            self.avg_rating += rating

        self.avg_rating = self.avg_rating / self.num_ratings

class User:
    
    def __init__(self):
        self.movies = []
        self.ratings = []
        self.genres = {
            "Action": Genre("Action"),
            "Adventure": Genre("Adventure"),
            "Animation": Genre("Animation"),
            "Biography": Genre("Biography"),
            "Children": Genre("Children"),
            "Comedy": Genre("Comedy"),
            "Crime": Genre("Crime"),
            "Documentary": Genre("Documentary"),
            "Drama": Genre("Drama"),
            "Fantasy": Genre("Fantasy"),
            "Family": Genre("Family"),
            "Film-Noir": Genre("Film-Noir"),
            "Horror": Genre("Horror"),
            "History": Genre("History"),
            "Musical": Genre("Musical"),
            "Mystery": Genre("Mystery"),
            "Romance": Genre("Romance"),
            "Sci-Fi": Genre("Sci-Fi"),
            "Thriller": Genre("Thriller"),
            "War": Genre("War"),
            "Western": Genre("Western"),
        }

        self.avg_num_ratings = 0
        self.avg_rating = 0
        self.avg_date = 0
        self.avg_genre_score = 0
    
    def analyze_movies(self):
        # assign movies to genres
        skipped = 0

        for idx, movie in enumerate(self.movies):
            if self.ratings[idx] < 2:
                skipped += 1
                continue

            self.avg_num_ratings += movie.num_ratings
            self.avg_rating += movie.rating
            self.avg_date += movie.date
            
            if movie.g_action == 1:
                self.genres["Action"].ratings.append(self.ratings[idx])
                self.genres["Action"].num_ratings += 1
            if movie.g_adv == 1:
                self.genres["Adventure"].ratings.append(self.ratings[idx])
                self.genres["Adventure"].num_ratings += 1
            if movie.g_ani == 1:
                self.genres["Animation"].ratings.append(self.ratings[idx])
                self.genres["Animation"].num_ratings += 1
            if movie.g_bio == 1:
                self.genres["Biography"].ratings.append(self.ratings[idx])
                self.genres["Biography"].num_ratings += 1
            if movie.g_child == 1:
                self.genres["Children"].ratings.append(self.ratings[idx])
                self.genres["Children"].num_ratings += 1
            if movie.g_comedy == 1:
                self.genres["Comedy"].ratings.append(self.ratings[idx])
                self.genres["Comedy"].num_ratings += 1
            if movie.g_crime == 1:
                self.genres["Crime"].ratings.append(self.ratings[idx])
                self.genres["Crime"].num_ratings += 1
            if movie.g_doc == 1:
                self.genres["Documentary"].ratings.append(self.ratings[idx])
                self.genres["Documentary"].num_ratings += 1
            if movie.g_drama == 1:
                self.genres["Drama"].ratings.append(self.ratings[idx])
                self.genres["Drama"].num_ratings += 1
            if movie.g_fantasy == 1:
                self.genres["Fantasy"].ratings.append(self.ratings[idx])
                self.genres["Fantasy"].num_ratings += 1
            if movie.g_film == 1:
                self.genres["Film-Noir"].ratings.append(self.ratings[idx])
                self.genres["Film-Noir"].num_ratings += 1
            if movie.g_horror == 1:
                self.genres["Horror"].ratings.append(self.ratings[idx])
                self.genres["Horror"].num_ratings += 1
            if movie.g_history == 1:
                self.genres["History"].ratings.append(self.ratings[idx])
                self.genres["History"].num_ratings += 1
            if movie.g_music == 1:
                self.genres["Musical"].ratings.append(self.ratings[idx])
                self.genres["Musical"].num_ratings += 1
            if movie.g_mys == 1:
                self.genres["Mystery"].ratings.append(self.ratings[idx])
                self.genres["Mystery"].num_ratings += 1
            if movie.g_rom == 1:
                self.genres["Romance"].ratings.append(self.ratings[idx])
                self.genres["Romance"].num_ratings += 1
            if movie.g_sci == 1:
                self.genres["Sci-Fi"].ratings.append(self.ratings[idx])
                self.genres["Sci-Fi"].num_ratings += 1
            if movie.g_west == 1:
                self.genres["Western"].ratings.append(self.ratings[idx])
                self.genres["Western"].num_ratings += 1
            if movie.g_war == 1:
                self.genres["War"].ratings.append(self.ratings[idx])
                self.genres["War"].num_ratings += 1
            if movie.g_thrill == 1:
                self.genres["Thriller"].ratings.append(self.ratings[idx])
                self.genres["Thriller"].num_ratings += 1
    
        self.avg_num_ratings = self.avg_num_ratings/(len(self.movies) - skipped)
        self.avg_rating = self.avg_rating/(len(self.movies) - skipped)
        self.avg_date = round(self.avg_date/(len(self.movies) - skipped), 0)

        for genre in self.genres:
            self.genres[genre].calc_average_rating()
        
        self.calc_genre_score()
        
        for g in self.genres.values():
            self.avg_genre_score += g.genre_score

        self.avg_genre_score = self.avg_genre_score/19

    def calc_genre_score(self):
        total_ratings = len(self.ratings)
        w1, w2 = 1, 2

        for genre in self.genres.values():
            percent_of_ratings = genre.num_ratings / total_ratings
            avg_rating = genre.avg_rating

            genre.genre_score = (percent_of_ratings * w1) + (avg_rating * w2)

    def get_inputdata(self):
        data = []

        for movie in self.movies:
            data.append([movie.rating, movie.num_ratings, movie.date, movie.g_action, movie.g_adv, movie.g_ani, movie.g_bio, movie.g_child, movie.g_comedy, movie.g_crime, movie.g_doc, movie.g_drama, movie.g_fantasy, movie.g_film, movie.g_horror, movie.g_history, movie.g_music, movie.g_mys, movie.g_rom, movie.g_sci, movie.g_thrill, movie.g_war, movie.g_west])

        return data

    def get_inputclass(self):
        data = []

        for m in self.movies:
            t = m.calc_similarity(self)

            print(t)
            data.append(t)

        return data
    
    def get_inputclass_2(self):
        data = []

        for m in self.ratings:
            data.append(m)

        return data
    
    def debug_sim(self, global_movies):
        for m in global_movies:
            m.similarity_score = m.calc_similarity(self)
    