
def groups(request, user_id): # Primary key for User
    pass # list of groups for specified user

def members(request, group_id): # Primary key for for Group
    pass # list of first and last names of users in specified group

def create_group(request):
    pass # Data params - user_id(s), group_name, group_is_private

def add_members(request):
    pass # Data Params - group_id, user_id(s)

def delete_members(request):
    pass # group_id, user_id(s)

def login(request):
    pass # Data Params - username, passward

def post_quote(request):
    pass # Data Params - Quote

def guess_quote(request, quote_id): # Primary key of quote
    pass  # Data Params - user_id, guess, is_correct)

def delete_quote(request, quote_id): # Primary key of quote
    pass # Data Params - user_id, quote

def new_user(request):
    pass # Dara params - first_name, last_name, email, username, password

def show_guesses(request, user_id): # Primary key for user
    pass # list of past guesses by specified user

def show_posts(request, user_id):   # Primary key for user
    pass # list of past quotes posted by specified user

def unguessed_quotes(request, user_id): # Primary key for user
    pass # list of quotes yet to be guessed



