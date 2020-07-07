from django.db import models

# Create your models here.


class Pending_Requests(models.Model):
    code = models.TextField()
    req_from = models.CharField(max_length=10)
    req_to = models.CharField(max_length=10)

class Done_Requests(models.Model):
    code = models.TextField()
    req_from = models.CharField(max_length=10)
    req_to = models.CharField(max_length=10)