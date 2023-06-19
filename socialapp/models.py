from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100,blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    favourite=models.ManyToManyField(User,related_name='favourite',blank=True)
    created_date=models.DateTimeField(max_length=50,auto_now_add=True)
    body=models.CharField(max_length=500)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail',args=[self.id,self.slug])

    def total_likes(self):
        return self.likes.count()

@receiver(pre_save,sender=Article)
def pre_save_slug(sender,**kwargs):
    slug1=slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug1

class Images(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    def __str__(self):
        return self.article.title + " Images "

#multiple comments posiable on single post is called ForeignKey
#multiple comments posiable on single user is called ForeignKey

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reply=models.ForeignKey('Comment',null=True,on_delete=models.CASCADE,related_name='replies')
    content=models.TextField(max_length=200)
