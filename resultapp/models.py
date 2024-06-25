from django.db import models

class ResultChecker(models.Model):
    studentname=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.studentname
