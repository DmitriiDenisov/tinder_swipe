from config import TOKEN
from utils.features import check_sluts
from utils.main_apis import TinderAPI

# https://github.com/MMcintire96/python_TinderAPI
tinderApi = TinderAPI(TOKEN)

# Get Tinder Recommendations of people around you
# recommendations = main_apis.get_recommendations()
recommendations_v2 = tinderApi.get_recs_v2()

# Get updates since certain date
tinderApi.get_updates("2021-04-24T10:28:13.392Z")

for rec in recommendations_v2['data']['results']:
    user_id = rec['user']['_id']
    if rec.get('distance_mi') * 1.6 > 50:
        # but if city is Dubai => continue
        if rec['user'].get('city') and rec['user'].get('city').get('name') in ['Dubai', 'Дубай']:
            pass
        else:
            tinderApi.dislike(user_id)
    elif rec['user'].get('city') and rec['user'].get('city').get('name') != 'Dubai':
        tinderApi.dislike(user_id)
    elif check_sluts(rec):
        tinderApi.dislike(user_id)
    else:
        resp = tinderApi.like(user_id)
        print("Likes Remaining:", resp['likes_remaining'])
