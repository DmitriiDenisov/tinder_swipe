from datetime import date
from random import random
from time import sleep


def calculate_age(birthday_string):
    """
    Converts from '1997-03-25T22:49:41.151Z' to an integer (age)
    """
    birthyear = int(birthday_string[:4])
    birthmonth = int(birthday_string[5:7])
    birthday = int(birthday_string[8:10])
    today = date.today()
    return today.year - birthyear - ((today.month, today.day) < (birthmonth, birthday))


def pause():
    """
    In order to appear as a real Tinder user using the app...
    When making many API calls, it is important to pause a...
    realistic amount of time between actions to not make Tinder...
    suspicious!
    """
    nap_length = 3 * random()
    print('Napping for %f seconds...' % nap_length)
    sleep(nap_length)


NUMS = ["ⳊꚨI", "Oཏꗚ", "ອꚨI", "ອꚨl", "ອךI", "9ገI", "ꏿཏꕃ", "WhatsApp", "Whatsap"]


def check_sluts(rec):
    for num in NUMS:
        if rec['user'].get('jobs') and num in rec['user'].get('jobs')[0]['title']['name']:
            return True
        if num in rec['user']['name'] or num in rec['user']['bio']:
            return True
        if num in rec['user']['name'] or num in rec['user']['bio']:
            return True
        if num in rec.get('teaser')['string'] or num in rec.get('teaser')['string']:
            return True
    return False
