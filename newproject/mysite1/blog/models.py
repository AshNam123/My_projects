from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class service(models.Model):
    user_id_ser = models.ForeignKey(User,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=150)
    service_provider = models.TextField()
    service_contact = models.CharField(max_length=20)
    service_cost = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.service_name
class query(models.Model):
    user_id_query = models.ForeignKey(User,on_delete=models.CASCADE)
    query_category = models.CharField(max_length=150)
    query_question = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.query_category
class answer(models.Model):
    user_id_ans = models.ForeignKey(query,null=True,on_delete=models.CASCADE)
    ans_query = models.TextField()
    unique_id = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.ans_query
class contact(models.Model):
    user_contact_id = models.ForeignKey(User,on_delete=models.CASCADE)
    user_nm = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.user_nm

