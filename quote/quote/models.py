from django.db import models

class User(models.Model):
    # Auto Primary Key id
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)


class Group(models.Model):
    # Auto Primary Key id
    group_name = models.CharField(max_length = 30)
    group_is_private = models.BooleanField(default = False)

class Quote(models.Model):
    # Auto Primary Key id
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.CharField(max_length = 200)
    quote_details = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 50)
    post_date = models.DateTimeField('date posted')

class Guess(models.Model):
    # Auto Primary Key id
    user_id =  models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE)
    guess = models.CharField(max_length = 50)
    is_correct = models.BooleanField(default = False)

class UserMembership(models.Model): 
    user_id = models.ManyToManyField(User)
    group_id = models.ManyToManyField(Group)
    is_admin = models.BooleanField(default = False)









