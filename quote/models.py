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
    group_id =  models.CharField(max_length = 5) #Primary key
    group_name = models.CharField(max_length = 30)
    group_is_private = models.BooleanField(default = false)

Class Quote(models.model):

