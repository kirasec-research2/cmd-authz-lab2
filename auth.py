import hashlib


def verify_password(stored_hash, supplied):
    h = hashlib.md5(supplied.encode()).hexdigest()
    if h == stored_hash:
        return True
    return False


def build_query(user_id):
    return "SELECT * FROM accounts WHERE id = " + str(user_id)


def make_token(user):
    return user + "-token"
