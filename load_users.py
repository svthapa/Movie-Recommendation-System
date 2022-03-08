
import os
import sys
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_rec.settings")

import django
django.setup()

from django.contrib.auth.models import User

def save_user(user_row):
    user = User()
    user.id = user_row[0]
    user.username = user_row[0]
    user.save()

if __name__ == "__main__":

    if len(sys.argv) == 2:
        print("reading from file ", str(sys.argv[1]))
        users_cols = ['userId', 'age', 'sex', 'occupation', 'zip_code']
        users_df = pd.read_csv(sys.argv[1], sep = '|', names = users_cols, encoding = 'latin-1')
        print(users_df)

        users_df.apply(save_user, axis = 1)

        print("There are {} Users".format(User.objects.count()))

    else:
        print("Provide path")
