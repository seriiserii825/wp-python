import random
import string


def getGroupId():
    id = "".join(
        [random.choice(string.ascii_letters + string.digits) for n in range(13)]
    )
    field_id = f"group_{id}".lower()
    return field_id
