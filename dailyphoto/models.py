
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 200,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="pic/",blank=True,null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    like_count = models.IntegerField(default=0)
    icons=models.CharField(max_length=1000,default='',blank=True)
    # icon_emotion=models.CharField(max_length=20, default='happy')
    icon_weather=models.CharField(max_length=20, default='sunny')



    def __str__(self):
        return self.subject

    # def time_string(self):
    #     now=timezone.now()
    #     return now
        
    
class Comment(models.Model):
    author       = models.ForeignKey(User , on_delete=models.CASCADE)
    post       = models.ForeignKey('Post', on_delete=models.CASCADE)
    parent     = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    # 대댓글 구현을 위해
    content    = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

class PersonalIconSet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion_is_setted=models.BooleanField(default=True)
    weather_is_setted=models.BooleanField(default=True)

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    #pk는 디폴트값으로 id Auto_increment  로 사용중 Question의 참조클라스가 id
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.content
    


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to= 'image/', blank=True)   #Pillow설치

    def __str__(self):
        return self.nickname





