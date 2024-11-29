import random
import string

def getFieldId():
    id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(13)])
    field_id = f'field_{id}'.lower()
    return field_id

