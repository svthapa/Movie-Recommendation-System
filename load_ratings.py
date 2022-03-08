
import os
import sys
import pandas as pd
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_rec.settings")

import django
django.setup()

from show_rec.models import Movie
from show_rec.models import Review
from django.contrib.auth.models import User

def save_review(review_row):
    review = Review()
    review.user_id = User.objects.get(id = review_row[0])
    review.movie = Movie.objects.get(id = review_row[1])
    review.user_name = User.objects.get(id = review_row[0])
    review.rating = review_row[2]

    review.save()

if __name__ == "__main__":

    if len(sys.argv) == 2:
        print("reading from file ", str(sys.argv[1]))
        columns_name = ['userId',"movieId","rating","timestamp"]
        ratings_df = pd.read_csv(sys.argv[1], sep = '\t', names =columns_name)
        print(ratings_df)

        ratings_df.apply(save_review, axis = 1)

        print("There are {} reviews".format(Review.objects.count()))

    else:
        print("Provide path")
