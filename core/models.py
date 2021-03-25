from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class blogpost(models.Model):
    STATUS_CHOICES=(("draft","Draft"),("published",'Publish'))
    status=models.CharField(choices=STATUS_CHOICES, max_length=50,default='draft')
    title=models.CharField(max_length=100, help_text='Enter the title of the post', unique=True)
    content=models.TextField(help_text='Write your post here')
    img=models.URLField(max_length=300,help_text='Enter the url for the image')
    slug=models.SlugField(unique_for_date='publish',max_length=150,help_text='Enter the slug for this post.')
    publish=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    created_on=models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering:['id','publish']

    def __str__(self):
        return self.title
    
class comment(models.Model):
    Sno=models.AutoField(primary_key=True)
    cmt_content=models.TextField(help_text='Enter comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(blogpost, on_delete=models.CASCADE)
    parent=models.ForeignKey("self",on_delete=models.CASCADE, null=True)
    date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=['date']

    def __str__(self):
        return self.cmt_content[0:100]+ '  by  ' + self.user.username


class usermessage(models.Model):
    email=models.EmailField(help_text='Enter email',unique=True)
    first_name=models.CharField(max_length=50,help_text='Enter your first name')
    last_name=models.CharField(max_length=50,help_text='Enter your last name')
    msg=models.TextField(help_text='Enter your message for us')
    date=models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering:['id','date']

    def __str__(self):
        return self.first_name +' ' + self.email


class newsletter(models.Model):
    email=models.EmailField(max_length=150, help_text='Enter your email',unique=True)
    date=models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering:['id']

    def __str__(self):
        return self.email