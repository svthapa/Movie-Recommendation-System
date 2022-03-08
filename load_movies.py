
import os
import sys
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_rec.settings")

import django
django.setup()

from show_rec.models import Movie

def save_movie(movie_row):
    movie = Movie()
    movie.id = movie_row[0]
    movie.title = movie_row[1]
    movie.release_date = movie_row[2]
    movie.imdb_url = movie_row[3]
    
    movie.save()

if __name__ == "__main__":

    if len(sys.argv) == 2:
        print("reading from file ", str(sys.argv[1]))
        genre_cols = [
        "genre_unknown", "Action", "Adventure", "Animation", "Children", "Comedy",
        "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
        "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
        ]
        movies_cols = ['movieId', 'title', 'release_date', "video_release_date", "imdb_url"
            ] + genre_cols
        movies_df = pd.read_csv(sys.argv[1], sep = '|', names = movies_cols, encoding = 'latin-1')
        print(movies_df)

        movies_df.apply(save_movie, axis = 1)

        print("There are {} movies".format(Movie.objects.count()))

    else:
        print("Provide path")
