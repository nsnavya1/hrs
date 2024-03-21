from django.db import models
from Administrator.models import *
from Guest.models import *


# Create your models here.
class tbl_roomdetails(models.Model):
    roomdetails_floor=models.CharField(max_length=50)
    roomdetails_count=models.CharField(max_length=50)
    roomtype =models.ForeignKey(tbl_roomtype, on_delete=models.CASCADE)
    hotel =models.ForeignKey(tbl_newhotel,null=True,on_delete=models.CASCADE)
    roomdetails_amount=models.CharField(max_length=50)
    roomdetails_occupancy=models.CharField(max_length=50)


class tbl_hotelfacility(models.Model):
    hotelfacility_name=models.CharField(max_length=50) 
    facility =models.ForeignKey(tbl_facility, on_delete=models.CASCADE)
    hotel =models.ForeignKey(tbl_newhotel,on_delete=models.CASCADE)

class tbl_mealpackages(models.Model):
    mealpackages_name=models.CharField(max_length=50)
    mealpackages_description=models.CharField(max_length=50)
    mealpackages_amount=models.CharField(max_length=50)
    hotel =models.ForeignKey(tbl_newhotel,null=True,on_delete=models.CASCADE)

class tbl_tourpackages(models.Model):
    tourpackages_name=models.CharField(max_length=50)
    tourpackages_description=models.CharField(max_length=50)
    tourpackages_amount=models.CharField(max_length=50)
    hotel =models.ForeignKey(tbl_newhotel,null=True,on_delete=models.CASCADE)
   