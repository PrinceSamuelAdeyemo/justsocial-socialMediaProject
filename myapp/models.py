from email.policy import default
from django.db import models
from django.conf import settings
import uuid
from datetime import datetime
from django.contrib.auth.models import User, auth


# Create your models here.
User = settings.AUTH_USER_MODEL

class Post(models.Model):
    # user_name = User.objects.get(username = user.username)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True)
    username = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100, null = True, blank = True)
    caption = models.TextField()
    postImage = models.ImageField(upload_to = "postImages")
    timeCreated = models.DateTimeField(default = datetime.now())
    noOfLikes = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, max_length = 20)
    id_user = models.IntegerField()
    posts = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True)
    profileImg = models.ImageField(upload_to = 'profileImages', default = 'picture_default.png')
    #username = models.ForeignKey(User_obj, on_delete = models.CASCADE, max_length = 20)
    first_name = models.CharField(max_length = 20)
    middle_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20)
    password = models.CharField(max_length = 20)
    phoneNum = models.CharField(max_length = 20)
    bio = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.user.username
    
    

    
class LikePost(models.Model):
    #post_username = models.ForeignKey(Post, on_delete = models.CASCADE)
    post_username = models.CharField(max_length = 100)
    post_id = models.CharField(max_length = 500)
    
    reaction_username = models.CharField(max_length = 100)
    reaction_date = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return self.reaction_username
    
    
class Follower(models.Model):
    user = models.CharField(max_length = 100)
    follower = models.CharField(max_length = 100, null = True, blank = True)
    
    def __str__(self):
        return self.user
    