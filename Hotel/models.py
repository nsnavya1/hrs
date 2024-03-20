from django.db import models
from Administrator.models import *
from Guest.models import *


# Create your models here.
class tbl_roomdetails(models.Model):
    roomdetails_floor=models.CharField(max_length=50)
    roomdetails_count=models.CharField(max_length=50)
    roomtype =models.ForeignKey(tbl_roomtype, on_delete=models.CASCADE)
    #hotel =models.ForeignKey(tbl_newhotel,null=True,on_delete=models.CASCADE)
    #roomdetails_type=models.CharField(max_length=50)
    roomdetails_amount=models.CharField(max_length=50)
    roomdetails_occupancy=models.CharField(max_length=50)
   