from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    '''用户表'''

    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'




class Tasks(models.Model):
    id = models.AutoField(primary_key = True)
    create_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    git_name = models.CharField(max_length=128, db_index=True)

    def __str__(self):
        return self.git_name

    class Meta:
        ordering = ['create_time']
        verbose_name = '任务'



class TeskResults(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=32)
    blog = models.CharField(max_length=64)
    public_repo_num = models.IntegerField(default=0)
    following_num = models.IntegerField(default=0)
    follower_num = models.IntegerField(default=0)
    public_gists_num = models.IntegerField(default = 0)
    task_id = models.CharField(max_length=128, db_index=True)