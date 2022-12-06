import file_handler as fh
import classes
import recommend as rec
import input_handler as ih

global_movies = {}
fh.load_files(global_movies)

user = classes.User()
fh.load_user_data(user, global_movies)
ih.input_loop(global_movies, user)

for m in global_movies.values():
    m.calc_rating()

user.analyze_movies()

for i in range(5):
    recommended_movies = rec.classify(global_movies, user)
    recommended_movies.sort(key=lambda x: x.similarity_rating, reverse=False)

    for idx, m in enumerate(recommended_movies):
        m.rankings.append(idx)

for m in recommended_movies:
    for v in m.rankings:
        m.avg_ranking += v;

    m.avg_ranking = m.avg_ranking/len(m.rankings)

diff = 0

recommended_movies.sort(key=lambda x: x.avg_ranking, reverse=False)

for idx, m in enumerate(recommended_movies):
    if idx == 20:
        break

    print(m.id + " title: " + m.title + " date: " + str(m.date) + " " + str(m.rating) + " " + str(m.num_ratings) + " est rating: " + str(m.similarity_rating))

    predicted = m.similarity_rating
    m.calc_similarity(user)
    actual = m.similarity_rating

    diff += abs(predicted-actual)

    print("Actual: " + str(m.similarity_rating))


print("User information: " + "Avg_rating: " + str(user.avg_rating) + " Avg_ratings: " + str(user.avg_num_ratings) + " Avg Date: " + str(user.avg_date))
print()
print()
print("Model information: MOE: " + str(diff/20))