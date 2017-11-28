



def groups(user_id): # Primary key for User
    return # list of groups for specified user

def members(group_id): # Primary key for for Group
    return # list of first and last names of users in specified group

def create_group():
    return # Data params - user_id(s), group_name, group_is_private

def add_members():
    return # Data Params - group_id, user_id(s)

def delete_members():
    return # group_id, user_id(s)

def login():
    return # Data Params - username, passward

def post_quote():
    return # Data Params - Quote

def guess_quote(quote_id): # Primary key of quote
    return  # Data Params - user_id, guess, is_correct)

def delete_quote(quote_id): # Primary key of quote
    return # Data Params - user_id, quote

def new_user():
    return # Dara params - first_name, last_name, email, username, password

def show_guesses(user_id): # Primary key for user
    return # list of past guesses by specified user

def show_posts(user_id):   # Primary key for user
    return # list of past quotes posted by specified user

def unguessed_quotes(user_id): # Primary key for user
    return # list of quotes yet to be guessed



