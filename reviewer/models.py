from django.db import models

class Pending_Requests(models.Model):
    code = models.TextField()
    req_from = models.CharField(max_length=10)
    req_to = models.CharField(max_length=10)
    comments = models.TextField()

class Done_Requests(models.Model):
    code = models.TextField()
    req_from = models.CharField(max_length=10)
    req_to = models.CharField(max_length=10)
    comments = models.TextField()
    reviews_added = models.TextField(null=True)