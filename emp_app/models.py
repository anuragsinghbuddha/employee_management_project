from datetime import date
from email.policy import default
from unicodedata import name
from django.db import models




class Department(models.Model):
    name = models.CharField(max_length=30,null=True)
    location = models.CharField(max_length=30,null=True)


    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    #hire_date = models.POST['date_year'] + "-" + models.POST['date_month'] + "-" + models.POST['date_day']

    hire_date=models.DateField()
    #location=models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s " %(self.first_name,self.last_name,self.phone)
 