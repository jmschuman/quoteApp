from django.db import models # should it be  "from quote.db import models"

class User(models.Model): # what does "models.Model" mean in this context
    user_id = models.CharField(max_length = 5) # Primary Key. How long should max_length be?
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    quotes_posted = models.IntegerField(default=0)
    quotes_guessed = models.IntegerField(default=0)

class Group(models.Model):
    group_id =  models.CharField(max_length = 5) # Primary Key
    group_name = models.CharField(max_length = 30)
    group_is_private = models.BooleanField(default = false)

class Quote(models.model):
    quote_id = models.CharField(max_length = 5) # Primary Key
    group_id = models.ForiegnKey(Group, on_delete=models.CASCADE) # I'm still confused on the meaning of "on_delete=models.CASCADE"
    user_id = models.ForiegnKey(User, on_delete=models.CASCADE)
    quote = models.CharField(max_length = 200)
    quote_details = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 50)
    post_date = models.DateTimeField('date posted')

class Guess(models.Model):
    guess_id = models.CharField(max_length = 5) # Primary Key
    user_id =  models.ForiegnKey(User, on_delete=models.CASCADE)
    group_id = models.ForiegnKey(Group, on_delete=models.CASCADE)
    quote_id = models.ForiegnKey(Quote, on_delete=models.CASCADE)
    guess = models.CharField(max_length = 50)
    is_correct = models.BooleanField(default = false)

class User_Membership(models.Model): # This was a related data table in the schema. Is it supposed to be a class in models?
    user_id = models.ForiegnKey(User, on_delete=models.CASCADE)
    group_id = models.ForiegnKey(Group, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default = false)









