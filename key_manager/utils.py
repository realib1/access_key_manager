import string
import random


def generate_key():
    prefix = "AKM"
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=22)).upper()
    return prefix + suffix

