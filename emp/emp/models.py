from django.db import models



class Emp(models.Model):
    name=models.CharField(max_length=200)
    email_id=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    working=models.BooleanField(default=True,)
    department=models.CharField(max_length=100, null=True , blank=True)