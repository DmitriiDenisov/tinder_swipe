import json
import requests

HOST = 'https://api.gotinder.com'
get_headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
    "Accept": "application/json"
}


class TinderAPI:
    def __init__(self, token):
        self.headers = get_headers.copy()
        self.headers['content-type'] = "application/json"
        self.headers.update({"X-Auth-Token": token})
        get_headers.update({"X-Auth-Token": token})

    def get_recommendations(self):
        """
        Returns a list of users that you can swipe on
        """
        try:
            r = requests.get('https://api.gotinder.com/user/recs', headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong with getting recomendations:", e)

    def get_updates(self, last_activity_date=""):
        """
        Returns all updates since the given activity date.
        The last activity date is defaulted at the beginning of time.
        Format for last_activity_date: "2017-07-09T10:28:13.392Z"
        """
        try:
            url = HOST + '/updates'
            r = requests.post(url,
                              headers=self.headers,
                              data=json.dumps({"last_activity_date": last_activity_date}))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong with getting updates:", e)

    def get_self(self):
        """
        Returns your own profile data
        """
        try:
            url = HOST + '/profile'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your data:", e)

    def change_preferences(self, **kwargs):
        """
        ex: change_preferences(age_filter_min=30, gender=0)
        kwargs: a dictionary - whose keys become separate keyword arguments and the values become values of these arguments
        age_filter_min: 18..46
        age_filter_max: 22..55
        age_filter_min <= age_filter_max - 4
        gender: 0 == seeking males, 1 == seeking females
        distance_filter: 1..100
        discoverable: true | false
        {"photo_optimizer_enabled":false}
        """
        try:
            url = HOST + '/profile'
            r = requests.post(url, headers=self.headers, data=json.dumps(kwargs))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not change your preferences:", e)

    def get_meta(self):
        """
        Returns meta data on yourself. Including the following keys:
        ['globals', 'client_resources', 'versions', 'purchases',
        'status', 'groups', 'products', 'rating', 'tutorials',
        'travel', 'notifications', 'user']
        """
        try:
            url = HOST + '/meta'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your metadata:", e)

    def get_meta_v2(self):
        """
        Returns meta data on yourself from V2 API. Including the following keys:
        ['account', 'client_resources', 'plus_screen', 'boost',
        'fast_match', 'top_picks', 'paywall', 'merchandising', 'places',
        'typing_indicator', 'profile', 'recs']
        """
        try:
            url = HOST + '/v2/meta'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your metadata:", e)

    def get_recs_v2(self):
        """
        This works more consistently then the normal get_recommendations becuase it seeems to check new location
        """
        try:
            url = HOST + '/v2/recs/core?locale=en-US'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            print('excepted')

    def get_person(self, id):
        """
        Gets a user's profile via their id
        """
        try:
            url = HOST + '/user/%s' % id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get that person:", e)

    def send_msg(self, match_id, msg):
        try:
            url = HOST + '/user/matches/%s' % match_id
            r = requests.post(url, headers=self.headers,
                              data=json.dumps({"message": msg}))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not send your message:", e)

    def superlike(self, person_id):
        try:
            url = HOST + '/like/%s/super' % person_id
            r = requests.post(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not superlike:", e)

    def like(self, person_id):
        try:
            url = HOST + '/like/%s' % person_id
            r = requests.get(url, headers=get_headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not like:", e)

    def dislike(self, person_id):
        try:
            url = HOST + '/pass/%s' % person_id
            r = requests.get(url, headers=get_headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not dislike:", e)

    def match_info(self, match_id):
        try:
            url = HOST + '/matches/%s' % match_id
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your match info:", e)

    def all_matches(self):
        try:
            url = HOST + '/v2/matches'
            r = requests.get(url, headers=self.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong. Could not get your match info:", e)
