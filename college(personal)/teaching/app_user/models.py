from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
def path_and_rename(instance,filename):
    uplaod_to = 'Images/'
    ext  = filename.split('.')[-1]
    if instance.user.username:
        filename = 'User_Profile_pic/{}.{}'.format(instance.user.username,ext)
    return os.path.join(uplaod_to,filename)
class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio  = models.CharField(max_length=150,blank = True)
    image_dp = models.ImageField(verbose_name="Profile pic" ,blank = True,null = True)

    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (teacher,'teacher'),
        (student,'student'),
        (parent,'parent'),
    ]
    user_types = models.CharField(max_length=10,choices=user_types,default=student)

    def __str__(self):
        return self.user.username