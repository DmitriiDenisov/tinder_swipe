import json
import requests

HOST = 'https://api.gotinder.com'
get_headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
    "Accept": "application/json"
}
headers = get_headers.copy()
headers['content-type'] = "application/json"


def get_bio_updates():
    r = requests.get(HOST + '/v1/activity/feed?direction=past&eventTypes=1023',
                     headers=headers
                     )
    return r.json()


def get_non_blurred_thumbnail_img():
    r = requests.get(HOST + '/v2/fast-match/preview',
                     headers=headers
                     )
    return r.json()


def report(person_id, cause, explanation=''):
    """
    There are three options for cause:
        0 : Other and requires an explanation
        1 : Feels like spam and no explanation
        4 : Inappropriate Photos and no explanation
    """
    try:
        url = HOST + '/report/%s' % person_id
        r = requests.post(url, headers=headers, data={
            "cause": cause, "text": explanation})
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not report:", e)


def unmatch(match_id):
    try:
        url = HOST + '/user/matches/%s' % match_id
        r = requests.delete(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not unmatch person:", e)


def set_webprofileusername(username):
    """
    Sets the username for the webprofile: https://www.gotinder.com/@YOURUSERNAME
    """
    try:
        url = HOST + '/profile/username'
        r = requests.put(url, headers=headers,
                         data=json.dumps({"username": username}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not set webprofile username:", e)


def reset_webprofileusername(username):
    """
    Resets the username for the webprofile
    """
    try:
        url = HOST + '/profile/username'
        r = requests.delete(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not delete webprofile username:", e)


def update_location(lat, lon):
    """
    Updates your location to the given float inputs
    Note: Requires a passport / Tinder Plus
    """
    try:
        url = HOST + '/passport/user/travel'
        r = requests.post(url, headers=headers, data=json.dumps({"lat": lat, "lon": lon}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not update your location:", e)


def reset_real_location():
    try:
        url = HOST + '/passport/user/reset'
        r = requests.post(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not update your location:", e)
