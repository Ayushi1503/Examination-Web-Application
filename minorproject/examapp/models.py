from django.db import models

class Questions(models.Model):
    que_no = models.IntegerField()
    que = models.TextField()
    answ = models.TextField()
    
class Answers(models.Model):
    ans_no = models.IntegerField()
    ans = models.TextField()
