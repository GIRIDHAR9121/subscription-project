from django.db import models

class PotumerakaData(models.Model):
    name=models.CharField(max_length=50)
    sur_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    amount=models.IntegerField()
    payment_type=models.CharField(max_length=50)
    date=models.DateField()
    recieved_by=models.CharField(max_length=50)

class Expenditure(models.Model):
    exp_name=models.CharField(max_length=150)
    exp_incurred=models.IntegerField()



