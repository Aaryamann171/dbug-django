from django.db import models

# Create your models here.


class ReviewRequest(models.Model):
    code = models.TextField()
    req_from = models.CharField(max_length=10)
    req_to = models.CharField(max_length=10)
