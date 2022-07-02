from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='blog/images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('BlogHome')


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('BlogHome')


class Post(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=122, default="")
    content = RichTextField(blank=True, null=True)
    pub_date = models.DateField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='blog/images/')

    def __str__(self):
        return str(self.title) + ' by ' + str(self.author)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        # return reverse('ArticleDetail', args=(str(self.pk)))
        return reverse('BlogHome')


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     parent = models.
#     body = models.TextField()
#     date_added = models.DateTimeField(default=now)
#
#     def __str__(self):
#         return self.body.slice(12) + '... - ' + self.user
