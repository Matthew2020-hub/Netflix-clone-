# from _typeshed import Self
from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user
from core.utils import auto_save_current_user

User = get_user_model()

# Create your models here.
#Post Model

class Post(models.Model):
    text = models.CharField(max_length=144, blank=True, null=True)
    image = models.ImageField(upload_to='post_images') #BASE_DIR ->media ->post_images
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    # status = models.ForeignKey(on_delete=models.PROTECT,db_constraint=False)
    def __str__(self):
        return str(self.pk)

    # def save(self, *args, **kwargs):
    #     user = get_current_user()
    #     if not self.id:
        # if user and not user.pk:
        #     user = None
        # if not self.pk:
        #     self.user = user
        # super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Post, self).save(*args, **kwargs)
        # Post.save()

#Comment Model
class Comment(models.Model):
    text = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
#Likes Model
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)
    liked_on =models.DateTimeField(auto_now_add =True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.is_like)


# followers model
class Follow(models.Model):
    users = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='follow_follower', on_delete= models.CASCADE)
    is_follow = models.BooleanField(default=True)
    followed_on = models.DateTimeField(auto_now_add =True)
    updated_on = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f"{self.user} --> {self.follower}"

