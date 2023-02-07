import random
import string

def generatePassword(length):
    return ''.join([random.choice(string.ascii_letters + string.punctuation ) for n in range(length)])