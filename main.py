from config import TOKEN
from utils.features import check_sluts
from utils.main_apis import TinderAPI
from utils.features import calculate_age
import matplotlib.pyplot as plt
from skimage import io

plt.close('all')

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
        for photo in rec['user']['photos']:
            url = photo['url']
            fig = plt.figure()
            image = io.imread(url)
            plt.imshow(image)
            plt.show(block=False)
        print(f'Age:{calculate_age(rec["user"]["birth_date"])}')
        print(f'Bio:{rec["user"]["bio"]}')
        print('----------------------------------------------')
        decision = bool(int(input("Like:1, Dislike:0. Your decision: ")))
        if decision:
            resp = tinderApi.like(user_id)
            print("Likes Remaining:", resp['likes_remaining'])
        else:
            tinderApi.dislike(user_id)
        plt.close(fig)
        plt.close('all')
